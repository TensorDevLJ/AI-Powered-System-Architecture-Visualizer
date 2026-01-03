#!/bin/bash

echo "🚀 Starting System Design Visualizer..."
echo ""

# Start backend in background
echo "Starting Backend Server (Port 5000)..."
python app.py &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting Frontend Server (Port 3000)..."
cd frontend
npm start &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"

echo ""
echo "✅ Both servers are running!"
echo "   Backend:  http://localhost:5000"
echo "   Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop all servers"

# Trap Ctrl+C to kill both processes
trap "echo ''; echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT

# Wait for processes
wait
