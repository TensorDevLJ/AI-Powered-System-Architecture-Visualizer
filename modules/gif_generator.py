from PIL import Image, ImageDraw, ImageFont
import os
import math

class GIFGenerator:
    """Step 10: GIF Generation Module (Optional)"""
    
    def __init__(self):
        self.node_width = 120
        self.node_height = 60
        self.font_size = 14
        self.num_frames = 30
        
    def generate(self, positioned_data, output_dir):
        """
        Generate animated GIF showing data flow
        """
        width = positioned_data['canvas_width']
        height = positioned_data['canvas_height']
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", self.font_size)
        except:
            font = ImageFont.load_default()
        
        positions = positioned_data['positions']
        components = positioned_data['components']
        relationships = positioned_data['relationships']
        
        frames = []
        
        # Create frames with animated arrows
        for frame_idx in range(self.num_frames):
            img = Image.new('RGB', (width, height), color='#F8F9FA')
            draw = ImageDraw.Draw(img)
            
            # Draw components
            for comp in components:
                if comp['name'] in positions:
                    self._draw_component(
                        draw,
                        positions[comp['name']],
                        comp['name'],
                        comp['shape'],
                        comp['color'],
                        font
                    )
            
            # Draw animated relationships
            for rel_idx, rel in enumerate(relationships):
                if rel['from'] in positions and rel['to'] in positions:
                    # Stagger animations
                    rel_progress = (frame_idx - rel_idx * 3) / self.num_frames
                    if rel_progress > 0:
                        self._draw_animated_arrow(
                            draw,
                            positions[rel['from']],
                            positions[rel['to']],
                            min(rel_progress, 1.0)
                        )
            
            frames.append(img)
        
        # Save GIF
        filename = 'architecture.gif'
        filepath = os.path.join(output_dir, filename)
        
        frames[0].save(
            filepath,
            save_all=True,
            append_images=frames[1:],
            duration=100,
            loop=0
        )
        
        return filepath
    
    def _draw_component(self, draw, position, name, shape, color, font):
        """Draw component (same as ImageGenerator)"""
        x, y = position
        w = self.node_width
        h = self.node_height
        
        # Simple rectangle for all shapes in GIF (for performance)
        x1, y1 = x - w//2, y - h//2
        x2, y2 = x + w//2, y + h//2
        draw.rectangle([x1, y1, x2, y2], fill=color, outline='#2C3E50', width=2)
        
        # Draw text
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = x - text_width // 2
        text_y = y - text_height // 2
        draw.text((text_x, text_y), name, fill='white', font=font)
    
    def _draw_animated_arrow(self, draw, from_pos, to_pos, progress):
        """Draw arrow with animation progress"""
        x1, y1 = from_pos
        x2, y2 = to_pos
        
        # Calculate current endpoint
        dx = x2 - x1
        dy = y2 - y1
        
        current_x = x1 + dx * progress
        current_y = y1 + dy * progress
        
        # Draw line
        draw.line([x1, y1, current_x, current_y], fill='#E74C3C', width=3)
        
        # Draw moving dot
        if progress > 0.1:
            r = 5
            draw.ellipse([current_x - r, current_y - r, current_x + r, current_y + r], 
                        fill='#E74C3C')
