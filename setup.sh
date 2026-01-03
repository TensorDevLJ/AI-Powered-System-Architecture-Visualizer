#!/bin/bash

echo "🚀 System Design Visualizer - Setup Script"
echo "==========================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi
echo "✅ Python found: $(python3 --version)"

# Check Node
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+"
    exit 1
fi
echo "✅ Node.js found: $(node --version)"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm"
    exit 1
fi
echo "✅ npm found: $(npm --version)"

echo ""
echo "📦 Installing Backend Dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Backend installation failed"
    exit 1
fi
echo "✅ Backend dependencies installed"

echo ""
echo "📦 Installing Frontend Dependencies..."
cd frontend
npm install

if [ $? -ne 0 ]; then
    echo "❌ Frontend installation failed"
    exit 1
fi
echo "✅ Frontend dependencies installed"

cd ..

# Create output directory
mkdir -p output

echo ""
echo "✅ Setup Complete!"
echo ""
echo "To run the application:"
echo "  1. Start backend:  python app.py"
echo "  2. Start frontend: cd frontend && npm start"
echo ""
echo "Then open http://localhost:3000 in your browser"
