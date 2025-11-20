#!/usr/bin/env python3
"""
Music Authentication System - Cross-Platform Startup Script
Starts both backend and frontend servers automatically
"""

import os
import sys
import subprocess
import time
import platform

def print_banner():
    """Print startup banner"""
    print("🎵 Music Authentication System Startup")
    print("=" * 40)
    print()

def start_backend():
    """Start the backend server"""
    print("📡 Starting Backend Server...")
    print("-" * 30)
    
    # Change to backend directory
    backend_dir = os.path.join(os.getcwd(), 'auth-music-backend')
    if not os.path.exists(backend_dir):
        print(f"❌ Backend directory not found: {backend_dir}")
        return False
    
    os.chdir(backend_dir)
    
    # Install dependencies if needed
    print("🔄 Installing dependencies...")
    try:
        subprocess.run(['npm', 'install'], check=True, capture_output=True)
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Dependency installation had issues: {e}")
        print("Continuing anyway...")
    
    # Start backend server
    print("🚀 Starting backend server...")
    try:
        # Start backend in a new process
        backend_process = subprocess.Popen(
            ['npm', 'run', 'dev'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"✅ Backend server started (PID: {backend_process.pid})")
        return backend_process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_frontend():
    """Start the frontend server"""
    print("\n🌐 Starting Frontend Server...")
    print("-" * 30)
    
    # Go back to project root
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Start frontend server
    PORT = 8000
    print(f"🎨 Starting frontend server on port {PORT}...")
    
    try:
        # Start frontend server
        frontend_process = subprocess.Popen(
            [sys.executable, '-m', 'http.server', str(PORT)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"✅ Frontend server started (PID: {frontend_process.pid})")
        print(f"🌍 Server URL: http://localhost:{PORT}")
        return frontend_process
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}")
        return None

def wait_for_servers():
    """Wait a moment for servers to start"""
    print("\n⏳ Waiting for servers to initialize...")
    time.sleep(3)
    print("✅ Servers should be ready now")

def print_access_info():
    """Print access information"""
    print("\n" + "=" * 50)
    print("🎉 SERVERS STARTED SUCCESSFULLY!")
    print("=" * 50)
    print()
    print("📱 Frontend: http://localhost:8000")
    print("🔗 Backend API: http://localhost:5000")
    print("💚 Health Check: http://localhost:5000/api/health")
    print()
    print("🎵 Ready to use your music player!")
    print("🛑 Press Ctrl+C to stop all servers")
    print()

def check_requirements():
    """Check if required tools are available"""
    print("🔍 Checking system requirements...")
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], 
                              capture_output=True, text=True)
        print(f"✅ Node.js: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.js first.")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], 
                              capture_output=True, text=True)
        print(f"✅ npm: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ npm not found. Please install npm first.")
        return False
    
    # Check Python
    python_version = platform.python_version()
    print(f"✅ Python: {python_version}")
    
    print("✅ All requirements satisfied\n")
    return True

def main():
    """Main startup function"""
    try:
        print_banner()
        
        # Check requirements
        if not check_requirements():
            print("❌ Please install the required tools and try again.")
            sys.exit(1)
        
        # Start backend
        backend_process = start_backend()
        if not backend_process:
            print("❌ Failed to start backend server")
            sys.exit(1)
        
        # Wait a moment
        time.sleep(2)
        
        # Start frontend
        frontend_process = start_frontend()
        if not frontend_process:
            print("❌ Failed to start frontend server")
            backend_process.terminate()
            sys.exit(1)
        
        # Wait for servers
        wait_for_servers()
        
        # Print access info
        print_access_info()
        
        # Keep script running and monitor processes
        try:
            while True:
                # Check if processes are still running
                if backend_process.poll() is not None:
                    print("⚠️  Backend process stopped unexpectedly")
                    break
                if frontend_process.poll() is not None:
                    print("⚠️  Frontend process stopped unexpectedly")
                    break
                
                time.sleep(5)
                
        except KeyboardInterrupt:
            print("\n🛑 Shutting down servers...")
        
        finally:
            # Clean up processes
            print("🔄 Stopping all servers...")
            backend_process.terminate()
            frontend_process.terminate()
            
            # Wait for graceful shutdown
            try:
                backend_process.wait(timeout=5)
                frontend_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                # Force kill if needed
                backend_process.kill()
                frontend_process.kill()
            
            print("✅ All servers stopped")
            print("👋 Goodbye!")
    
    except Exception as e:
        print(f"❌ Startup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()