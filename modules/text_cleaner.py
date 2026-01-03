import re
from collections import Counter
import math

class TextCleaner:
    """Step 4: Text Cleaning Module (ML-lite with TF-IDF)"""
    
    # Architecture-related keywords (expanded)
    ARCHITECTURE_KEYWORDS = [
        'api', 'gateway', 'service', 'server', 'database', 'cache', 'queue',
        'load balancer', 'cdn', 'microservice', 'request', 'response',
        'authentication', 'authorization', 'storage', 'notification',
        'message', 'broker', 'cluster', 'node', 'endpoint', 'architecture',
        'component', 'module', 'layer', 'tier', 'client', 'backend', 'frontend',
        'scaling', 'partition', 'replica', 'shard', 'distributed', 'system',
        'protocol', 'http', 'websocket', 'rest', 'grpc', 'kafka', 'redis',
        'mongodb', 'postgresql', 'mysql', 'nosql', 'sql', 'data flow',
        'pipeline', 'stream', 'batch', 'real-time', 'latency', 'throughput'
    ]
    
    # Noise words to remove
    NOISE_WORDS = [
        'advertisement', 'subscribe', 'newsletter', 'comment below',
        'like and share', 'follow us', 'social media', 'copyright',
        'all rights reserved', 'terms of service', 'privacy policy'
    ]
    
    def clean(self, raw_text):
        """
        Clean and filter raw text using ML-lite techniques:
        - Remove duplicates
        - Remove irrelevant sections
        - Keep architecture keywords
        - Optional TF-IDF scoring
        """
        # Step 1: Remove noise
        text = self._remove_noise(raw_text)
        
        # Step 2: Split into sentences
        sentences = self._split_sentences(text)
        
        # Step 3: Remove duplicates
        unique_sentences = self._remove_duplicates(sentences)
        
        # Step 4: Filter by relevance (keyword-based)
        relevant_sentences = self._filter_by_keywords(unique_sentences)
        
        # Step 5: Score sentences using TF-IDF (optional)
        scored_sentences = self._score_sentences_tfidf(relevant_sentences)
        
        # Step 6: Keep top sentences
        top_sentences = self._select_top_sentences(scored_sentences, top_n=30)
        
        # Step 7: Join and clean up
        clean_text = ". ".join(top_sentences)
        clean_text = re.sub(r'\s+', ' ', clean_text)
        
        # Fallback if nothing found
        if len(clean_text) < 100:
            clean_text = raw_text[:2000]
        
        return clean_text
    
    def _remove_noise(self, text):
        """Remove advertisement and noise content"""
        for noise in self.NOISE_WORDS:
            text = re.sub(re.escape(noise), '', text, flags=re.IGNORECASE)
        return text
    
    def _split_sentences(self, text):
        """Split text into sentences"""
        # Split by sentence boundaries
        sentences = re.split(r'[.!?]+', text)
        # Clean and filter
        return [s.strip() for s in sentences if len(s.strip()) > 20]
    
    def _remove_duplicates(self, sentences):
        """Remove duplicate sentences"""
        seen = set()
        unique = []
        
        for sentence in sentences:
            sentence_normalized = sentence.lower().strip()
            if sentence_normalized not in seen:
                seen.add(sentence_normalized)
                unique.append(sentence)
        
        return unique
    
    def _filter_by_keywords(self, sentences):
        """Filter sentences containing architecture keywords"""
        filtered = []
        
        for sentence in sentences:
            sentence_lower = sentence.lower()
            keyword_count = sum(1 for kw in self.ARCHITECTURE_KEYWORDS if kw in sentence_lower)
            
            # Keep if has at least 1 architecture keyword
            if keyword_count >= 1:
                filtered.append(sentence)
        
        return filtered
    
    def _score_sentences_tfidf(self, sentences):
        """
        Score sentences using simplified TF-IDF
        TF = Term Frequency in sentence
        IDF = Inverse Document Frequency across all sentences
        """
        if not sentences:
            return []
        
        # Calculate document frequency for each word
        doc_freq = Counter()
        total_docs = len(sentences)
        
        for sentence in sentences:
            words = set(re.findall(r'\w+', sentence.lower()))
            for word in words:
                doc_freq[word] += 1
        
        # Score each sentence
        scored = []
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            word_freq = Counter(words)
            
            # Calculate TF-IDF score
            score = 0
            for word in word_freq:
                tf = word_freq[word] / len(words) if words else 0
                idf = math.log(total_docs / (doc_freq[word] + 1))
                
                # Boost score for architecture keywords
                boost = 2.0 if word in self.ARCHITECTURE_KEYWORDS else 1.0
                
                score += tf * idf * boost
            
            scored.append((sentence, score))
        
        # Sort by score (descending)
        scored.sort(key=lambda x: x[1], reverse=True)
        
        return scored
    
    def _select_top_sentences(self, scored_sentences, top_n=30):
        """Select top N sentences by score"""
        return [sentence for sentence, score in scored_sentences[:top_n]]
    
    def _contains_architecture_keywords(self, text):
        """Check if text contains architecture-related keywords"""
        count = sum(1 for keyword in self.ARCHITECTURE_KEYWORDS if keyword in text)
        return count >= 1
