from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import traceback
from modules.input_handler import InputHandler
from modules.article_finder import ArticleFinder
from modules.web_scraper import WebScraper
from modules.text_cleaner import TextCleaner
from modules.ai_extractor import AIExtractor
from modules.data_normalizer import DataNormalizer
from modules.visual_mapper import VisualMapper
from modules.layout_engine import LayoutEngine
from modules.image_generator import ImageGenerator
from modules.gif_generator import GIFGenerator

app = Flask(__name__)
CORS(app)

# Create output directory
OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "System Design Visualizer API is running"})

@app.route('/api/generate', methods=['POST'])
def generate_visualization():
    try:
        data = request.json
        
        # Step 1: Input Handler
        input_handler = InputHandler()
        config = input_handler.validate_and_parse(data)
        
        # Step 2: Article Finder
        article_finder = ArticleFinder()
        urls = article_finder.find_articles(config['topic'], config['design'])
        
        # Step 3: Web Scraper
        scraper = WebScraper()
        raw_text = scraper.scrape_urls(urls)
        
        # Step 4: Text Cleaner
        cleaner = TextCleaner()
        clean_text = cleaner.clean(raw_text)
        
        # Step 5: AI Extractor
        extractor = AIExtractor()
        architecture_data = extractor.extract(clean_text, config['ai_provider'])
        
        # Step 6: Data Normalizer
        normalizer = DataNormalizer()
        normalized_data = normalizer.normalize(architecture_data)
        
        # Step 7: Visual Mapper
        mapper = VisualMapper()
        visual_data = mapper.map_visuals(normalized_data)
        
        # Step 8: Layout Engine
        layout = LayoutEngine()
        positioned_data = layout.calculate_layout(visual_data)
        
        # Step 9: Image Generator
        image_gen = ImageGenerator()
        metadata = {'topic': config['topic'], 'design': config['design']}
        image_path = image_gen.generate(positioned_data, OUTPUT_DIR, metadata)
        
        # Step 10: GIF Generator (optional)
        gif_path = None
        if config.get('generate_gif', False):
            gif_gen = GIFGenerator()
            gif_path = gif_gen.generate(positioned_data, OUTPUT_DIR)
        
        return jsonify({
            "success": True,
            "image_path": f"/api/download/{os.path.basename(image_path)}",
            "gif_path": f"/api/download/{os.path.basename(gif_path)}" if gif_path else None,
            "components": normalized_data['components'],
            "relationships": normalized_data['relationships']
        })
        
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_path = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=False)
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
