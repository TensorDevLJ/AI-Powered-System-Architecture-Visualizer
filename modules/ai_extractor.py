import json
import re
import os

class AIExtractor:
    """Step 5: AI Extraction Module (Pluggable with Enhanced NER)"""
    
    EXTRACTION_PROMPT = """You are a system architecture expert. Analyze the following text and extract ONLY the system components and their relationships.

IMPORTANT RULES:
1. Extract component names (like "API Gateway", "Load Balancer", "User Service", "Database")
2. Extract relationships showing how components connect
3. Return ONLY valid JSON, no explanations
4. Focus on architectural components, not features or concepts

From the text below, extract:
- System components (services, databases, caches, queues, etc.)
- Relationships between components (how they communicate)

Return EXACTLY this JSON format:
{{
  "components": ["Component1", "Component2", "Component3"],
  "relationships": [
    {{"from": "Component1", "to": "Component2", "type": "request"}},
    {{"from": "Component2", "to": "Component3", "type": "query"}}
  ]
}}

Text to analyze:
{text}

Return ONLY the JSON object, nothing else."""
    
    # Component patterns for NER-style extraction
    COMPONENT_PATTERNS = [
        # Explicit components
        r'\b(API Gateway|Load Balancer|CDN|Message Queue|Cache|Web Server|App Server)\b',
        r'\b(\w+)\s+(Service|Server|Database|DB|Cache|Queue|Broker)\b',
        
        # Technology names
        r'\b(Redis|MongoDB|MySQL|PostgreSQL|Kafka|RabbitMQ|Elasticsearch|Cassandra)\b',
        r'\b(Nginx|Apache|HAProxy|Envoy)\b',
        
        # Cloud services
        r'\b(AWS\s+\w+|S3|EC2|Lambda|DynamoDB|SQS|SNS)\b',
        r'\b(Google\s+\w+|Cloud Storage|BigQuery|Pub/Sub)\b',
        
        # Architecture patterns
        r'\b(Frontend|Backend|Client|Server|Worker|Consumer|Producer)\b',
    ]
    
    # Relationship patterns
    RELATIONSHIP_PATTERNS = [
        (r'(\w+(?:\s+\w+)?)\s+(?:sends?|forwards?|routes?)\s+(?:to|requests?)\s+(\w+(?:\s+\w+)?)', 'request'),
        (r'(\w+(?:\s+\w+)?)\s+(?:queries?|reads?)\s+(?:from\s+)?(\w+(?:\s+\w+)?)', 'query'),
        (r'(\w+(?:\s+\w+)?)\s+(?:writes?|stores?)\s+(?:to|in)\s+(\w+(?:\s+\w+)?)', 'write'),
        (r'(\w+(?:\s+\w+)?)\s+(?:connects?|communicates?)\s+(?:with|to)\s+(\w+(?:\s+\w+)?)', 'connects'),
        (r'(\w+(?:\s+\w+)?)\s+→\s+(\w+(?:\s+\w+)?)', 'request'),
    ]
    
    def extract(self, text, provider):
        """
        Extract architecture using selected AI provider
        """
        if provider == "huggingface":
            return self._extract_huggingface(text)
        elif provider == "cohere":
            return self._extract_cohere(text)
        elif provider == "gemini":
            return self._extract_gemini(text)
        else:
            return self._extract_fallback(text)
    
    def _extract_gemini(self, text):
        """Extract using Google Gemini"""
        try:
            import google.generativeai as genai
            
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                print("GEMINI_API_KEY not set, using enhanced fallback")
                return self._extract_fallback(text)
            
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = self.EXTRACTION_PROMPT.format(text=text[:4000])
            response = model.generate_content(prompt)
            
            result_text = response.text
            result_text = self._clean_json_response(result_text)
            
            data = json.loads(result_text)
            
            # Validate and enhance with pattern extraction
            return self._enhance_extraction(data, text)
            
        except Exception as e:
            print(f"Gemini extraction error: {e}")
            return self._extract_fallback(text)
    
    def _extract_cohere(self, text):
        """Extract using Cohere"""
        try:
            import cohere
            
            api_key = os.getenv('COHERE_API_KEY')
            if not api_key:
                print("COHERE_API_KEY not set, using enhanced fallback")
                return self._extract_fallback(text)
            
            co = cohere.Client(api_key)
            
            prompt = self.EXTRACTION_PROMPT.format(text=text[:4000])
            response = co.generate(
                model='command',
                prompt=prompt,
                max_tokens=1500,
                temperature=0.3
            )
            
            result_text = response.generations[0].text
            result_text = self._clean_json_response(result_text)
            
            data = json.loads(result_text)
            
            # Validate and enhance
            return self._enhance_extraction(data, text)
            
        except Exception as e:
            print(f"Cohere extraction error: {e}")
            return self._extract_fallback(text)
    
    def _extract_huggingface(self, text):
        """Extract using HuggingFace (enhanced rule-based for demo)"""
        return self._extract_fallback(text)
    
    def _extract_fallback(self, text):
        """
        Enhanced rule-based extraction using NER-style patterns and dependency detection
        """
        components = set()
        relationships = []
        
        # Step 1: Extract components using patterns (NER-style)
        for pattern in self.COMPONENT_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    # For patterns with groups, join them
                    component = ' '.join(filter(None, match)).strip()
                else:
                    component = match.strip()
                
                if len(component) > 2:  # Filter very short matches
                    components.add(component)
        
        # Step 2: Add common components if text mentions them (keyword detection)
        text_lower = text.lower()
        common_components = {
            'client': 'Client',
            'user': 'Client',
            'frontend': 'Frontend',
            'api': 'API Gateway',
            'gateway': 'API Gateway',
            'load balanc': 'Load Balancer',
            'database': 'Database',
            'cache': 'Cache',
            'queue': 'Message Queue',
            'cdn': 'CDN',
            'storage': 'Storage',
            'authentication': 'Auth Service',
            'notification': 'Notification Service',
            'search': 'Search Service',
            'analytics': 'Analytics Service'
        }
        
        for keyword, component in common_components.items():
            if keyword in text_lower:
                components.add(component)
        
        # Step 3: Extract relationships using patterns (dependency extraction)
        for pattern, rel_type in self.RELATIONSHIP_PATTERNS:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                if len(match) == 2:
                    from_comp = match[0].strip().title()
                    to_comp = match[1].strip().title()
                    
                    if from_comp and to_comp and len(from_comp) > 2 and len(to_comp) > 2:
                        relationships.append({
                            'from': from_comp,
                            'to': to_comp,
                            'type': rel_type
                        })
        
        # Step 4: Generate default relationships based on common patterns
        component_list = list(components)
        
        if not relationships and len(component_list) > 1:
            relationships = self._generate_default_relationships(component_list, text_lower)
        
        # Step 5: If still no components, use ultra-basic defaults
        if not components:
            components = {
                "Client", "API Gateway", "Load Balancer", 
                "Application Server", "Database", "Cache"
            }
            relationships = [
                {"from": "Client", "to": "API Gateway", "type": "request"},
                {"from": "API Gateway", "to": "Load Balancer", "type": "forward"},
                {"from": "Load Balancer", "to": "Application Server", "type": "route"},
                {"from": "Application Server", "to": "Database", "type": "query"},
                {"from": "Application Server", "to": "Cache", "type": "check"}
            ]
        
        return {
            "components": list(components),
            "relationships": relationships
        }
    
    def _generate_default_relationships(self, components, text_lower):
        """Generate default relationships based on component types (architecture patterns)"""
        relationships = []
        
        # Categorize components by type
        clients = [c for c in components if any(x in c.lower() for x in ['client', 'user', 'frontend'])]
        gateways = [c for c in components if 'gateway' in c.lower() or 'api' in c.lower()]
        balancers = [c for c in components if 'balanc' in c.lower()]
        services = [c for c in components if 'service' in c.lower() or 'server' in c.lower()]
        databases = [c for c in components if any(x in c.lower() for x in ['database', 'db', 'mongo', 'sql', 'postgres', 'mysql', 'cassandra'])]
        caches = [c for c in components if any(x in c.lower() for x in ['cache', 'redis'])]
        queues = [c for c in components if any(x in c.lower() for x in ['queue', 'kafka', 'rabbit', 'sqs'])]
        cdns = [c for c in components if 'cdn' in c.lower()]
        
        # Generate flow: Client → Gateway → Balancer → Services → Database/Cache/Queue
        
        # Client to Gateway
        for client in clients:
            for gateway in gateways:
                relationships.append({"from": client, "to": gateway, "type": "request"})
        
        # Client to CDN (for static content)
        for client in clients:
            for cdn in cdns:
                relationships.append({"from": client, "to": cdn, "type": "request"})
        
        # Gateway to Balancer or Services
        for gateway in gateways:
            if balancers:
                relationships.append({"from": gateway, "to": balancers[0], "type": "forward"})
            elif services:
                relationships.append({"from": gateway, "to": services[0], "type": "route"})
        
        # Balancer to Services
        for balancer in balancers:
            for service in services:
                relationships.append({"from": balancer, "to": service, "type": "route"})
        
        # Services to Databases/Caches/Queues
        for service in services:
            for db in databases:
                relationships.append({"from": service, "to": db, "type": "query"})
            for cache in caches:
                relationships.append({"from": service, "to": cache, "type": "check"})
            for queue in queues:
                relationships.append({"from": service, "to": queue, "type": "publish"})
        
        return relationships
    
    def _enhance_extraction(self, data, text):
        """Enhance AI extraction with pattern-based extraction"""
        ai_components = set(data.get('components', []))
        ai_relationships = data.get('relationships', [])
        
        # Add pattern-based components
        fallback_data = self._extract_fallback(text)
        pattern_components = set(fallback_data['components'])
        
        # Merge components (union of both)
        all_components = ai_components | pattern_components
        
        # Keep AI relationships if they exist, otherwise use pattern-based
        if not ai_relationships:
            ai_relationships = fallback_data['relationships']
        
        return {
            "components": list(all_components),
            "relationships": ai_relationships
        }
    
    def _clean_json_response(self, text):
        """
        Clean JSON response from AI (remove markdown, extra text)
        """
        # Remove markdown code blocks
        text = re.sub(r'```json\s*', '', text)
        text = re.sub(r'```\s*', '', text)
        
        # Find JSON object
        json_match = re.search(r'\{[\s\S]*\}', text)
        if json_match:
            return json_match.group(0)
        
        return text
