# Quick Start Guide 🚀

Get your System Design Visualizer running in 5 minutes!

## Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
./setup.sh

# Start both servers
./start.sh
```

Open http://localhost:3000 in your browser - Done! 🎉

## Option 2: Manual Setup

### Step 1: Install Backend Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install Frontend Dependencies
```bash
cd frontend
npm install
cd ..
```

### Step 3: Start Backend
```bash
python app.py
```
Leave this terminal running.

### Step 4: Start Frontend (New Terminal)
```bash
cd frontend
npm start
```

### Step 5: Open Browser
Navigate to http://localhost:3000

## First Time Usage

1. Select a system (e.g., "Uber")
2. Choose "High Level Design" (HLD)
3. Pick "Google Gemini" as AI Provider
4. Click "Generate Diagram"
5. Wait 10-30 seconds
6. Download your architecture diagram!

## Troubleshooting

### Backend won't start
- Make sure port 5000 is free
- Check Python version: `python3 --version` (needs 3.8+)
- Reinstall dependencies: `pip install -r requirements.txt`

### Frontend won't start
- Make sure port 3000 is free
- Check Node version: `node --version` (needs 16+)
- Delete node_modules and reinstall: `rm -rf frontend/node_modules && cd frontend && npm install`

### Diagram generation fails
- This is normal without API keys - the system uses fallback extraction
- For better results, get free API keys:
  - Gemini: https://makersuite.google.com/app/apikey
  - Cohere: https://dashboard.cohere.com/api-keys
- Add them to `.env` file (copy from `.env.template`)

## What's Next?

- Try different systems (Amazon, Netflix, etc.)
- Compare HLD vs LLD designs
- Enable GIF generation for animated diagrams
- Experiment with different AI providers
- Check README.md for advanced features

Happy Diagramming! 🎨
