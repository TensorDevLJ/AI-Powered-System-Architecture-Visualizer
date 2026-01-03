class InputHandler:
    """Step 1: User Input Module"""
    
    VALID_TOPICS = ["uber", "amazon", "dns", "netflix", "whatsapp", "instagram", "twitter", "youtube"]
    VALID_DESIGNS = ["hld", "lld"]
    VALID_PROVIDERS = ["huggingface", "cohere", "gemini"]
    
    def validate_and_parse(self, data):
        """
        Validates user input and converts to internal config object
        """
        topic = data.get('topic', '').lower().strip()
        design = data.get('design', '').lower().strip()
        ai_provider = data.get('ai_provider', 'gemini').lower().strip()
        generate_gif = data.get('generate_gif', False)
        
        # Validation
        if not topic:
            raise ValueError("Topic is required")
        
        if design not in self.VALID_DESIGNS:
            raise ValueError(f"Design must be one of: {', '.join(self.VALID_DESIGNS)}")
        
        if ai_provider not in self.VALID_PROVIDERS:
            ai_provider = 'gemini'  # Default fallback
        
        return {
            "topic": topic,
            "design": design.upper(),
            "ai_provider": ai_provider,
            "generate_gif": generate_gif
        }
