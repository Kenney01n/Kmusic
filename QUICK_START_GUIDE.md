# Quick Start Guide - Music Authentication System

Get your music player up and running in 5 minutes!

## 🚀 30-Second Setup

### 1. Extract Project
```bash
tar -xzf final_year_project_complete.tar.gz
cd final_year_project_user_files
```

### 2. Backend (Terminal 1)
```bash
cd auth-music-backend
npm install
npm run dev
```

### 3. Frontend (Terminal 2)
```bash
# From project root
python -m http.server 8000
```

### 4. Open Browser
✅ **Success:** Browser opens to http://localhost:8000 automatically

---

## 📋 Detailed Setup Instructions

### Prerequisites Checklist
- [ ] Node.js (v14+) installed
- [ ] npm installed  
- [ ] Python installed (for frontend server)
- [ ] Internet connection (for MongoDB Atlas)

### Step-by-Step Instructions

#### Step 1: Project Extraction
1. Download `final_year_project_complete.tar.gz`
2. Extract to your desired location:
   ```bash
   tar -xzf final_year_project_complete.tar.gz
   cd final_year_project_user_files
   ```

#### Step 2: Backend Setup
1. **Navigate to backend:**
   ```bash
   cd auth-music-backend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```
   *This installs: express, mongoose, jsonwebtoken, bcryptjs, cors, express-validator*

3. **Environment is pre-configured:**
   - MongoDB Atlas connection ready
   - JWT secret configured
   - CORS set for localhost:8000

#### Step 3: Start Backend Server
**Method A - npm script:**
```bash
npm run dev
```

**Method B - Node.js directly:**
```bash
node server.js
```

**Expected Output:**
```
✅ MongoDB connected successfully
🚀 Server is running on port 5000
📱 Health check: http://localhost:5000/api/health
```

#### Step 4: Start Frontend Server
**Open a new terminal window and run:**

**Method A - Python (recommended):**
```bash
# From project root directory
python -m http.server 8000
```

**Method B - Using startup script:**
```bash
python start_server.py
```

**Expected Output:**
```
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

#### Step 5: Access Application
1. **Open your browser**
2. **Navigate to:** http://localhost:8000
3. **You should see:** Purple music player interface

---

## 🎵 Testing Your Setup

### ✅ Verification Checklist

**Backend Health Check:**
- [ ] Visit: http://localhost:5000/api/health
- [ ] Expected: `{"status": "Server is running!", "timestamp": "..."}`

**Frontend Interface:**
- [ ] Visit: http://localhost:8000
- [ ] Expected: Purple-themed music player
- [ ] Navigation buttons should be visible

**Authentication Test:**
- [ ] Click "Sign Up" to create account
- [ ] Use test credentials:
  - Username: `testuser123`
  - Email: `test@example.com`
  - Password: `password123`
- [ ] Should redirect to music player

**Music Player Test:**
- [ ] Search for any song (e.g., "Bohemian Rhapsody")
- [ ] Click play button
- [ ] Video should start playing

---

## 🔧 Configuration Details

### Pre-Configured Settings

**Backend (.env file):**
```env
PORT=5000
MONGODB_URI=mongodb+srv://musicuser:Kaminagoat1675@music-auth.ruimsvb.mongodb.net/?appName=music-auth
JWT_SECRET=31b4acf9af538820ff368524dfab4835a0191b17a164819afdd810a1ae9925fe28c7d97bd206065053da17f81d8af171a57bcd142c7509f1857d2f69f87d3b30
JWT_EXPIRES_IN=90d
FRONTEND_URL=http://localhost:8000
```

**Frontend Server:**
- Port: 8000
- Method: Python HTTP server
- Directory: `/complete-frontend`

**Backend Server:**
- Port: 5000
- Method: Node.js Express
- Directory: `/auth-music-backend`

---

## 🎮 Usage Instructions

### Getting Started

1. **Sign Up:**
   - Click "Sign Up" button
   - Enter username, email, password
   - Click "Create Account"

2. **Sign In:**
   - Use your registered credentials
   - Click "Sign In"

3. **Play Music:**
   - Use search bar to find songs
   - Click play button on results
   - Enjoy your music!

4. **Create Playlists:**
   - Click "Create Playlist" button
   - Add songs to your playlist
   - Manage multiple playlists

### Navigation
- **Home**: Main music player
- **Playlists**: View your playlists
- **Settings**: User preferences
- **Sign Out**: Logout of your account

---

## 🛠️ Startup Scripts

### Windows Users
```batch
# Run from project root
start_server.bat
```
*Opens both backend and frontend servers automatically*

### Cross-Platform Users
```bash
# Run from project root
python start_server.py
```
*Works on Windows, Mac, and Linux*

### Manual Startup
**Terminal 1 (Backend):**
```bash
cd auth-music-backend && npm run dev
```

**Terminal 2 (Frontend):**
```bash
python -m http.server 8000
```

---

## 🐛 Troubleshooting

### Common Issues

**Problem:** "Cannot connect to server"
- **Solution:** Ensure backend is running on port 5000

**Problem:** "CORS error in browser"
- **Solution:** Check `FRONTEND_URL=http://localhost:8000` in `.env`

**Problem:** "MongoDB connection failed"
- **Solution:** Check internet connection for MongoDB Atlas

**Problem:** "Port 8000 already in use"
- **Solution:** Kill process using port 8000 or use different port

### Port Conflicts
```bash
# Check what's using port 8000
lsof -i :8000  # Mac/Linux
netstat -ano | findstr :8000  # Windows

# Kill process if needed
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows
```

### Log Locations
- **Backend logs:** Terminal where you ran `npm run dev`
- **Frontend logs:** Terminal where you ran `python -m http.server 8000`
- **Browser console:** F12 → Console tab

---

## 📱 Mobile Testing

1. **Find your IP address:**
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   ```

2. **Access from mobile device:**
   - Use: `http://YOUR_IP_ADDRESS:8000`
   - Example: `http://192.168.1.100:8000`

3. **Test responsive design:**
   - Rotate phone/tablet
   - Test touch interactions
   - Verify all features work

---

## 🎯 Next Steps

### For Development
1. **Customize styling** in `complete-frontend/Style1.css`
2. **Add features** in `complete-frontend/app1.js`
3. **Extend API** in `auth-music-backend/routes/auth.js`

### For Deployment
1. **Backend:** Deploy to Heroku, Vercel, or DigitalOcean
2. **Frontend:** Deploy to Netlify, Vercel, or GitHub Pages
3. **Database:** MongoDB Atlas (already configured)

### For Enhancement
- Add music recommendations
- Implement social features
- Create mobile app
- Add offline functionality

---

## ✅ Success Indicators

When everything is working correctly, you should see:

- [x] **Backend terminal:** "Server is running on port 5000"
- [x] **Frontend terminal:** "Serving HTTP on port 8000"
- [x] **Browser:** Purple music player interface loads
- [x] **Sign up:** New user account created successfully
- [x] **Music search:** YouTube results appear and play
- [x] **Playlists:** Create and manage playlists

---

**🎵 You're all set! Enjoy your music player! 🎵**

*Need help? Check the main README.md for detailed documentation.*