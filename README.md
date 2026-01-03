# System Design Visualizer 🎨

An **AI-powered full-stack application** that automatically generates beautiful architecture diagrams from system design descriptions. 

**🌟 Built with:**
- **Frontend**: React 18 with modern CSS animations
- **Backend**: Python Flask with 10-step AI pipeline
- **AI Integration**: Google Gemini, Cohere, HuggingFace support

## ✨ Key Features

### 🎯 Frontend (React)
- **Modern UI**: Cyberpunk-inspired design with smooth animations
- **8 Pre-built Systems**: Uber, Amazon, Netflix, WhatsApp, Instagram, Twitter, YouTube, DNS
- **Interactive Selection**: Click-to-select system, design type, and AI provider
- **Real-time Feedback**: Loading indicators, error messages, success states
- **Download Options**: Direct download of PNG and GIF files
- **Responsive Design**: Works on desktop and mobile devices
- **Component Display**: Shows extracted components and relationships

### 🤖 Backend (Flask + Python)
- **Multiple AI Providers**: Google Gemini, Cohere, HuggingFace (with fallback)
- **10-Step Pipeline**: Complete modular architecture (see below)
- **Web Scraping**: Automatic article fetching and content extraction
- **Smart Extraction**: AI-powered component and relationship detection
- **Visual Mapping**: Automatic shape assignment (rectangles, cylinders, hexagons, etc.)
- **Graph Algorithms**: Intelligent layout using NetworkX
- **Image Generation**: Professional diagrams with Pillow (PIL)
- **GIF Animation**: Optional animated data flow visualization

## Architecture Overview 🏗️

```
┌─────────────┐
│   React     │
│  Frontend   │ (Port 3000)
└──────┬──────┘
       │ HTTP/REST
       ▼
┌─────────────┐
│   Flask     │
│   Backend   │ (Port 5000)
└──────┬──────┘
       │
       ├──► Article Finder
       ├──► Web Scraper
       ├──► Text Cleaner
       ├──► AI Extractor (Gemini/Cohere/HF)
       ├──► Data Normalizer
       ├──► Visual Mapper
       ├──► Layout Engine
       └──► Image/GIF Generator
```

## Prerequisites 📋

- Python 3.8+
- Node.js 16+
- npm or yarn

## Installation 🚀

### 1. Clone the Repository

```bash
cd system-design-visualizer
```

### 2. Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Optional: Set up API keys for AI providers
export GEMINI_API_KEY="your-gemini-api-key"
export COHERE_API_KEY="your-cohere-api-key"
```

**Note**: The system works without API keys using fallback rule-based extraction.

### 3. Frontend Setup

```bash
cd frontend
npm install
```

## Running the Application 🎯

### Start Backend Server

```bash
# From project root
python app.py
```

Backend will run on `http://localhost:5000`

### Start Frontend

```bash
# In a new terminal, from frontend directory
cd frontend
npm start
```

Frontend will run on `http://localhost:3000`

## Usage 💡

1. **Open your browser** to `http://localhost:3000`
2. **Select a system** (e.g., Uber, Amazon, Netflix)
3. **Choose design type** (HLD or LLD)
4. **Pick AI provider** (Gemini recommended if API key available)
5. **Optional**: Enable GIF generation for animated diagrams
6. **Click "Generate Diagram"**
7. **Download** your architecture diagram!

## Project Structure 📁

```
system-design-visualizer/
├── app.py                      # Flask backend entry point
├── requirements.txt            # Python dependencies
├── modules/                    # Backend modules
│   ├── input_handler.py       # Step 1: Input validation
│   ├── article_finder.py      # Step 2: Find relevant articles
│   ├── web_scraper.py         # Step 3: Scrape content
│   ├── text_cleaner.py        # Step 4: Clean text
│   ├── ai_extractor.py        # Step 5: Extract with AI
│   ├── data_normalizer.py     # Step 6: Normalize data
│   ├── visual_mapper.py       # Step 7: Map to visuals
│   ├── layout_engine.py       # Step 8: Calculate layout
│   ├── image_generator.py     # Step 9: Generate PNG
│   └── gif_generator.py       # Step 10: Generate GIF
├── output/                     # Generated diagrams
└── frontend/                   # React frontend
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── App.js             # Main component
        ├── App.css            # Styles
        ├── index.js           # Entry point
        └── index.css
```

## Module Pipeline 🔄

### Step 1: Input Handler
Validates user input (topic, design type, AI provider)

### Step 2: Article Finder
Finds relevant system design articles (hardcoded + web search)

### Step 3: Web Scraper
Extracts content from articles using BeautifulSoup

### Step 4: Text Cleaner
Filters architecture-relevant content using keywords

### Step 5: AI Extractor
Uses selected AI provider to extract components and relationships

### Step 6: Data Normalizer
Removes duplicates and normalizes component names

### Step 7: Visual Mapper
Maps components to shapes (rectangle, cylinder, hexagon, etc.)

### Step 8: Layout Engine
Calculates positions using topological sort and layered layout

### Step 9: Image Generator
Draws components and arrows using PIL

### Step 10: GIF Generator
Creates animated version with data flow animation

## API Endpoints 🌐

### GET `/api/health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "message": "System Design Visualizer API is running"
}
```

### POST `/api/generate`
Generate architecture diagram

**Request Body:**
```json
{
  "topic": "uber",
  "design": "hld",
  "ai_provider": "gemini",
  "generate_gif": false
}
```

**Response:**
```json
{
  "success": true,
  "image_path": "/api/download/architecture.png",
  "gif_path": "/api/download/architecture.gif",
  "components": ["API Gateway", "Load Balancer", "Database"],
  "relationships": [
    {"from": "API Gateway", "to": "Load Balancer", "type": "request"}
  ]
}
```

### GET `/api/download/<filename>`
Download generated file

## Configuration ⚙️

### Adding New Systems

Edit `modules/article_finder.py`:

```python
KNOWN_RESOURCES = {
    "your_system": [
        "https://article1.com",
        "https://article2.com"
    ]
}
```

### Customizing Shapes

Edit `modules/visual_mapper.py`:

```python
SHAPE_MAP = {
    'your_component': 'hexagon',  # or 'rectangle', 'cylinder', etc.
}
```

### Adjusting Layout

Edit `modules/layout_engine.py`:

```python
self.layer_spacing = 250  # Horizontal spacing
self.node_spacing = 150   # Vertical spacing
```

## Troubleshooting 🔧

### Backend Issues

**Problem**: `ModuleNotFoundError`
**Solution**: Run `pip install -r requirements.txt`

**Problem**: AI extraction fails
**Solution**: Set API keys or system will use fallback extraction

**Problem**: Port 5000 already in use
**Solution**: Change port in `app.py`: `app.run(port=5001)`

### Frontend Issues

**Problem**: `npm install` fails
**Solution**: Delete `node_modules` and `package-lock.json`, then reinstall

**Problem**: CORS errors
**Solution**: Ensure backend is running and CORS is enabled

**Problem**: Images not loading
**Solution**: Check backend logs and ensure output directory exists

## Technologies Used 🛠️

### Backend
- **Flask**: Web framework
- **BeautifulSoup4**: Web scraping
- **Pillow**: Image generation
- **NetworkX**: Graph algorithms
- **Google Gemini**: AI extraction (optional)
- **Cohere**: AI extraction (optional)
- **HuggingFace**: AI extraction (optional)

### Frontend
- **React**: UI framework
- **Axios**: HTTP client
- **CSS3**: Animations and styling
- **Google Fonts**: Custom typography

## Future Enhancements 🚀

- [ ] Support for more system templates
- [ ] Custom component editor
- [ ] Export to SVG format
- [ ] Real-time collaboration
- [ ] Template gallery
- [ ] Dark/light theme toggle
- [ ] Mobile app version
- [ ] Docker containerization
- [ ] Cloud deployment guides

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License.

## Support 💬

For issues and questions, please open an issue on GitHub.

---

Built with ❤️ using React, Flask, and AI
