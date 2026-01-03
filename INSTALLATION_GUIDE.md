# 📘 Complete Installation & Usage Guide
## System Design Visualizer - React + Flask

---

## 📦 What's Inside the ZIP File

```
system-design-visualizer/
│
├── 🐍 BACKEND (Flask/Python)
│   ├── app.py                      # Main Flask server
│   ├── requirements.txt            # Python dependencies
│   └── modules/                    # 10-step pipeline
│       ├── input_handler.py        # Step 1: Validate input
│       ├── article_finder.py       # Step 2: Find articles
│       ├── web_scraper.py          # Step 3: Scrape content
│       ├── text_cleaner.py         # Step 4: Clean text
│       ├── ai_extractor.py         # Step 5: AI extraction
│       ├── data_normalizer.py      # Step 6: Normalize data
│       ├── visual_mapper.py        # Step 7: Map to shapes
│       ├── layout_engine.py        # Step 8: Calculate positions
│       ├── image_generator.py      # Step 9: Generate PNG
│       └── gif_generator.py        # Step 10: Generate GIF
│
├── ⚛️ FRONTEND (React)
│   └── frontend/
│       ├── package.json            # Node dependencies
│       ├── public/
│       │   └── index.html          # HTML template
│       └── src/
│           ├── index.js            # React entry point
│           ├── App.js              # Main React component
│           ├── App.css             # Custom styling
│           └── index.css           # Base styles
│
├── 📚 DOCUMENTATION
│   ├── README.md                   # Full documentation
│   ├── QUICKSTART.md              # Quick start guide
│   └── .env.template              # Environment config
│
└── 🛠️ SCRIPTS
    ├── setup.sh                    # Automated setup
    └── start.sh                    # Start both servers
```

---

## 🚀 STEP-BY-STEP INSTALLATION

### Prerequisites Check

Before starting, ensure you have:

```bash
# Check Python (need 3.8 or higher)
python3 --version

# Check Node.js (need 16 or higher)
node --version

# Check npm
npm --version
```

If any are missing, install them first:
- **Python**: https://www.python.org/downloads/
- **Node.js**: https://nodejs.org/ (includes npm)

---

### 🎯 OPTION 1: Automated Setup (Easiest)

#### Step 1: Extract the ZIP
```bash
# Extract the downloaded file
unzip system-design-visualizer.zip

# Navigate into the folder
cd system-design-visualizer
```

#### Step 2: Run Setup Script
```bash
# Make scripts executable
chmod +x setup.sh start.sh

# Run automated setup
./setup.sh
```

This will:
- ✅ Check Python & Node versions
- ✅ Install all backend dependencies (Flask, Pillow, etc.)
- ✅ Install all frontend dependencies (React, axios, etc.)
- ✅ Create output directory

#### Step 3: Start Both Servers
```bash
# Start backend AND frontend together
./start.sh
```

This runs:
- Backend on `http://localhost:5000`
- Frontend on `http://localhost:3000`

#### Step 4: Open Browser
Navigate to: **http://localhost:3000**

---

### 🔧 OPTION 2: Manual Setup (Step by Step)

#### Backend Setup

```bash
# Step 1: Navigate to project folder
cd system-design-visualizer

# Step 2: Install Python dependencies
pip install -r requirements.txt

# Expected output: Installing flask, flask-cors, beautifulsoup4...
# This may take 2-3 minutes

# Step 3: Start backend server
python app.py

# You should see:
# * Running on http://127.0.0.1:5000
# * Press CTRL+C to quit
```

**✅ Backend is now running!** Leave this terminal open.

---

#### Frontend Setup

Open a **NEW terminal window**:

```bash
# Step 1: Navigate to frontend folder
cd system-design-visualizer/frontend

# Step 2: Install Node dependencies
npm install

# Expected output: Installing react, react-dom, axios...
# This may take 3-5 minutes

# Step 3: Start frontend server
npm start

# Your browser will automatically open to http://localhost:3000
```

**✅ Frontend is now running!**

---

## 🎨 HOW TO USE THE APPLICATION

### First Time Usage

1. **Open Browser**
   - Go to `http://localhost:3000`
   - You'll see the System Design Visualizer interface

2. **Select a System**
   - Click on any system tile (Uber 🚗, Amazon 📦, Netflix 🎬, etc.)
   - The selected tile will highlight

3. **Choose Design Type**
   - **HLD** (High Level Design): Overview of system architecture
   - **LLD** (Low Level Design): Detailed component design

4. **Pick AI Provider**
   - **Google Gemini** ✨ (Recommended - requires API key)
   - **Cohere** 🧠 (Requires API key)
   - **HuggingFace** 🤗 (Uses rule-based fallback)

5. **Optional: Enable GIF**
   - Check "Generate animated GIF" for animated data flow

6. **Generate!**
   - Click "Generate Diagram" button
   - Wait 10-30 seconds (depends on system complexity)

7. **Download Results**
   - View the generated architecture diagram
   - Click "Download PNG" or "Download GIF"
   - See extracted components and relationships

---

## 🔑 Setting Up AI Providers (Optional but Recommended)

The system works without API keys using fallback extraction, but AI providers give better results.

### Get Free API Keys

1. **Google Gemini** (Recommended)
   - Visit: https://makersuite.google.com/app/apikey
   - Create free account
   - Generate API key

2. **Cohere**
   - Visit: https://dashboard.cohere.com/api-keys
   - Sign up for free
   - Create API key

### Add API Keys

```bash
# Copy the template
cp .env.template .env

# Edit .env file
nano .env   # or use any text editor

# Add your keys:
GEMINI_API_KEY=your_actual_gemini_key_here
COHERE_API_KEY=your_actual_cohere_key_here

# Save and restart backend server
```

---

## 🎯 TESTING THE APPLICATION

### Quick Test

1. Select: **Uber** 🚗
2. Design: **HLD**
3. Provider: **Google Gemini**
4. Click: **Generate Diagram**

Expected Result:
- Loading spinner for 10-20 seconds
- Architecture diagram with components like:
  - Client
  - API Gateway
  - Load Balancer
  - Ride Service
  - Database
  - Cache
- Downloadable PNG file

### Test Other Systems

Try these combinations:

| System | Design | Expected Components |
|--------|--------|-------------------|
| Amazon | HLD | Shopping Cart, Payment Service, Inventory DB |
| Netflix | HLD | Video Streaming, CDN, Recommendation Engine |
| WhatsApp | HLD | Message Queue, WebSocket Server, User DB |
| Instagram | HLD | Media Storage, Feed Service, Notification |

---

## 🛠️ TROUBLESHOOTING

### Problem: Backend won't start

**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install -r requirements.txt
```

**Error**: `Address already in use (Port 5000)`

**Solution**:
```bash
# Find what's using port 5000
lsof -i :5000

# Kill that process or change port in app.py
# Edit app.py, last line: app.run(port=5001)
```

---

### Problem: Frontend won't start

**Error**: `npm install` fails

**Solution**:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Error**: `Port 3000 already in use`

**Solution**:
```bash
# The prompt will ask to use another port
# Type 'Y' to use port 3001 instead
```

---

### Problem: CORS errors

**Error**: `Access-Control-Allow-Origin` in console

**Solution**:
- Make sure backend is running on port 5000
- Check `flask-cors` is installed
- Backend already has CORS enabled in `app.py`

---

### Problem: Image generation fails

**Error**: "Generation failed"

**Solution**:
- This is normal without API keys
- The system uses fallback rule-based extraction
- Result may be simpler but still works
- For better results, add API keys (see above)

---

### Problem: No images appear

**Solution**:
```bash
# Check output directory exists
mkdir -p output

# Check backend logs in terminal
# Look for errors when generating

# Verify backend URL in frontend
# Check frontend/src/App.js line 5:
# const API_URL = 'http://localhost:5000';
```

---

## 📊 ARCHITECTURE FLOW

```
User Input (React Frontend)
       ↓
    HTTP POST
       ↓
Flask Backend receives:
  {
    topic: "uber",
    design: "hld",
    ai_provider: "gemini"
  }
       ↓
Step 1: Input Handler validates data
       ↓
Step 2: Article Finder searches for articles
       ↓
Step 3: Web Scraper extracts content
       ↓
Step 4: Text Cleaner filters relevant text
       ↓
Step 5: AI Extractor extracts components & relationships
       ↓
Step 6: Data Normalizer removes duplicates
       ↓
Step 7: Visual Mapper assigns shapes & colors
       ↓
Step 8: Layout Engine calculates positions
       ↓
Step 9: Image Generator creates PNG
       ↓
Step 10: GIF Generator creates animation (optional)
       ↓
Backend responds with:
  {
    success: true,
    image_path: "/api/download/architecture.png",
    components: [...],
    relationships: [...]
  }
       ↓
React displays image + download button
```

---

## 🎨 CUSTOMIZATION

### Add Your Own System

Edit `modules/article_finder.py`:

```python
KNOWN_RESOURCES = {
    "your_system": [
        "https://article1.com/system-design",
        "https://article2.com/architecture"
    ]
}
```

Edit `frontend/src/App.js`:

```javascript
const topics = [
    { value: 'your_system', label: 'Your System', icon: '🚀' },
    // ... existing topics
];
```

### Change Colors/Shapes

Edit `modules/visual_mapper.py`:

```python
SHAPE_MAP = {
    'your_component': 'hexagon',  # or rectangle, cylinder, diamond
}
```

### Adjust Layout

Edit `modules/layout_engine.py`:

```python
self.canvas_width = 1200    # Change canvas size
self.layer_spacing = 250    # Horizontal spacing
self.node_spacing = 150     # Vertical spacing
```

---

## 🎓 LEARNING THE CODE

### Backend Structure
- **app.py**: Main Flask application with API endpoints
- **modules/**: Modular pipeline (10 steps)
- Each module is independent and testable

### Frontend Structure
- **App.js**: Main React component with state management
- **App.css**: Custom styling with animations
- Uses `axios` for HTTP requests
- Responsive design with CSS Grid

### Key Technologies
- **Backend**: Flask, BeautifulSoup, Pillow, NetworkX
- **Frontend**: React, Axios, CSS3 animations
- **AI**: Google Gemini, Cohere (optional)

---

## 📈 WHAT'S NEXT?

### Immediate Next Steps
1. ✅ Generate your first diagram
2. ✅ Try different systems
3. ✅ Compare HLD vs LLD
4. ✅ Add API keys for better results

### Advanced Features
- Export to SVG format
- Custom component editor
- Real-time collaboration
- Template gallery
- Docker deployment

---

## 🤝 SUPPORT

### Getting Help

1. **Check logs**
   - Backend: Look at terminal running `python app.py`
   - Frontend: Check browser console (F12)

2. **Common issues**
   - Port conflicts: Change ports
   - Missing dependencies: Reinstall
   - API limits: Use fallback mode

3. **Documentation**
   - README.md: Full documentation
   - QUICKSTART.md: Quick reference
   - This guide: Complete walkthrough

---

## ✅ VERIFICATION CHECKLIST

Before reporting issues, verify:

- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Frontend dependencies installed (`npm install`)
- [ ] Backend running on port 5000
- [ ] Frontend running on port 3000
- [ ] Browser opened to http://localhost:3000
- [ ] No CORS errors in browser console
- [ ] Output directory exists

---

## 🎉 SUCCESS!

If you see the architecture diagram, congratulations! You've successfully:
- ✅ Set up a full-stack application
- ✅ Integrated React with Flask
- ✅ Implemented AI-powered extraction
- ✅ Generated beautiful architecture diagrams

**Enjoy creating system design diagrams!** 🎨

---

**Questions or Issues?**
Check the README.md or QUICKSTART.md for more details.

Happy Diagramming! 🚀
