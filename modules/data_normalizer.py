import re
from difflib import SequenceMatcher

class DataNormalizer:
    """Step 6: Data Normalization Module"""
    
    def normalize(self, raw_data):
        """
        Normalize extracted data:
        - Remove duplicates
        - Normalize names
        - Validate relationships
        """
        components = self._normalize_components(raw_data.get('components', []))
        relationships = self._normalize_relationships(
            raw_data.get('relationships', []),
            components
        )
        
        return {
            "components": components,
            "relationships": relationships
        }
    
    def _normalize_components(self, components):
        """
        Remove duplicates and normalize component names
        """
        normalized = []
        seen_lower = {}
        
        for comp in components:
            # Clean up component name
            comp = str(comp).strip()
            if not comp:
                continue
            
            # Normalize
            comp = self._normalize_name(comp)
            comp_lower = comp.lower()
            
            # Check for similar existing components
            similar_found = False
            for existing_lower, existing_name in seen_lower.items():
                if self._is_similar(comp_lower, existing_lower):
                    similar_found = True
                    break
            
            if not similar_found:
                normalized.append(comp)
                seen_lower[comp_lower] = comp
        
        return normalized
    
    def _normalize_relationships(self, relationships, valid_components):
        """
        Validate and normalize relationships
        """
        normalized = []
        seen = set()
        
        valid_comp_set = {c.lower(): c for c in valid_components}
        
        for rel in relationships:
            if not isinstance(rel, dict):
                continue
            
            from_comp = str(rel.get('from', '')).strip()
            to_comp = str(rel.get('to', '')).strip()
            rel_type = str(rel.get('type', 'connects')).strip()
            
            if not from_comp or not to_comp:
                continue
            
            # Normalize names
            from_comp = self._normalize_name(from_comp)
            to_comp = self._normalize_name(to_comp)
            
            # Find matching valid components
            from_match = self._find_matching_component(from_comp, valid_comp_set)
            to_match = self._find_matching_component(to_comp, valid_comp_set)
            
            if not from_match or not to_match:
                continue
            
            # Check for duplicates
            rel_key = (from_match, to_match, rel_type)
            if rel_key in seen:
                continue
            
            seen.add(rel_key)
            normalized.append({
                "from": from_match,
                "to": to_match,
                "type": rel_type
            })
        
        return normalized
    
    def _normalize_name(self, name):
        """
        Normalize component name
        """
        # Title case
        name = name.title()
        
        # Fix common abbreviations
        name = re.sub(r'\bApi\b', 'API', name)
        name = re.sub(r'\bDb\b', 'Database', name)
        name = re.sub(r'\bCdn\b', 'CDN', name)
        name = re.sub(r'\bHttp\b', 'HTTP', name)
        name = re.sub(r'\bRest\b', 'REST', name)
        
        return name
    
    def _is_similar(self, str1, str2, threshold=0.8):
        """
        Check if two strings are similar using sequence matching
        """
        return SequenceMatcher(None, str1, str2).ratio() > threshold
    
    def _find_matching_component(self, name, valid_components_dict):
        """
        Find matching component from valid list
        """
        name_lower = name.lower()
        
        # Exact match
        if name_lower in valid_components_dict:
            return valid_components_dict[name_lower]
        
        # Similarity match
        for valid_lower, valid_name in valid_components_dict.items():
            if self._is_similar(name_lower, valid_lower, threshold=0.75):
                return valid_name
        
        return None
