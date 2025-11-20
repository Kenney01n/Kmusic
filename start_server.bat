@echo off
echo 🎵 Music Authentication System Startup
echo =====================================

echo.
echo 📡 Starting Backend Server...
cd auth-music-backend
echo 🔄 Installing dependencies...
npm install
echo 🚀 Starting backend server...
start "Backend Server" cmd /k "npm run dev"

echo.
echo ⏳ Waiting 3 seconds for backend to start...
timeout /t 3 /nobreak > nul

echo.
echo 🌐 Starting Frontend Server...
cd ..
echo 🎨 Starting frontend server on port 8000...
start "Frontend Server" cmd /k "python -m http.server 8000"

echo.
echo 🌐 Server will open at: http://localhost:8000
echo 🔗 Backend API: http://localhost:5000
echo ✅ Both servers are starting...
echo.
echo 📱 Open your browser and go to: http://localhost:8000
echo 🛑 Close this window to stop the startup process
echo.
pause