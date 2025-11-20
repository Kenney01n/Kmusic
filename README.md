# Music Authentication System - Complete Final Year Project

A full-stack music player application with user authentication, playlist management, and YouTube integration.

## 🎵 Project Overview

This project combines a modern frontend music player with a secure backend authentication system, providing users with a complete music streaming experience.

### Key Features

**Frontend Features:**
- 🎨 **Modern UI**: Purple-themed music player interface
- 🔐 **Secure Authentication**: Sign up, sign in, and profile management
- 🎶 **YouTube Integration**: Play music directly from YouTube
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🎧 **Playlist Management**: Create and manage custom playlists
- ⚙️ **Settings**: User preferences and theme customization

**Backend Features:**
- 🔒 **JWT Authentication**: Secure token-based authentication
- 💾 **MongoDB Database**: Cloud-based user and playlist storage
- 🔑 **Password Security**: Bcrypt hashing for password protection
- 📋 **RESTful API**: Well-structured API endpoints
- 🛡️ **CORS Protection**: Secure cross-origin resource sharing

## 🏗️ Technology Stack

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **JavaScript (ES6+)**: Vanilla JavaScript with async/await
- **YouTube API**: Music streaming integration
- **Responsive Design**: Mobile-first approach

### Backend
- **Node.js**: Runtime environment
- **Express.js**: Web application framework
- **MongoDB**: NoSQL database with Mongoose ODM
- **JWT**: JSON Web Token authentication
- **bcryptjs**: Password hashing
- **express-validator**: Input validation and sanitization

### Development Tools
- **Nodemon**: Development server with auto-restart
- **CORS**: Cross-origin resource sharing
- **dotenv**: Environment variable management

## 📋 Project Structure

```
final_year_project_user_files/
├── complete-frontend/          # Frontend music player
│   ├── index.html             # Main music player page
│   ├── Style1.css             # Purple theme styles
│   ├── app1.js                # Main application logic
│   ├── auth.js                # Authentication functions
│   ├── settings.html          # User settings page
│   └── auth/                  # Authentication pages
│       ├── signin_form.html   # Sign in page
│       └── signup_form.html   # Sign up page
├── auth-music-backend/         # Backend API server
│   ├── server.js              # Main server file
│   ├── package.json           # Dependencies
│   ├── .env                   # Environment variables
│   ├── models/
│   │   └── User.js            # User database model
│   ├── middleware/
│   │   └── auth.js            # JWT authentication middleware
│   ├── routes/
│   │   └── auth.js            # Authentication API routes
│   └── README.md              # Backend documentation
├── README.md                  # This file
├── QUICK_START_GUIDE.md       # Quick setup instructions
├── start_server.bat           # Windows startup script
└── start_server.py            # Cross-platform startup script
```

## 🚀 Quick Start

### Prerequisites
- **Node.js** (v14 or higher)
- **npm** (comes with Node.js)
- **MongoDB Atlas Account** (for cloud database)

### 1. Extract Project
```bash
# Extract the final_year_project_complete.tar.gz
tar -xzf final_year_project_complete.tar.gz
cd final_year_project_user_files
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd auth-music-backend

# Install dependencies
npm install

# The .env file is already configured with:
# - MongoDB Atlas connection
# - JWT secret key
# - Frontend URL (http://localhost:8000)
```

### 3. Start Backend Server
```bash
# Method 1: Using npm script
npm run dev

# Method 2: Using startup scripts
# Windows:
start_server.bat

# Python (cross-platform):
python start_server.py

# Manual start:
node server.js
```

### 4. Start Frontend Server
In a new terminal:

```bash
# Navigate to project root
cd final_year_project_user_files

# Start frontend server (Python)
python -m http.server 8000

# Or using startup script
python start_server.py
```

### 5. Access Application
- **Frontend**: http://localhost:8000
- **Backend API**: http://localhost:5000
- **Health Check**: http://localhost:5000/api/health

## 📊 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "musiclover123",
  "email": "user@example.com",
  "password": "securepass123"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "token": "jwt_token_here",
  "user": {
    "id": "user_id",
    "username": "musiclover123",
    "email": "user@example.com"
  }
}
```

#### Login User
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepass123"
}
```

#### Get User Profile
```http
GET /api/auth/profile
Authorization: Bearer jwt_token_here
```

#### Create Playlist
```http
POST /api/auth/create-playlist
Authorization: Bearer jwt_token_here
Content-Type: application/json

{
  "name": "My Favorite Songs"
}
```

## 🔧 Configuration

### Environment Variables (.env)
```env
# Server Configuration
PORT=5000
NODE_ENV=development

# Database
MONGODB_URI=mongodb+srv://musicuser:Kaminagoat1675@music-auth.ruimsvb.mongodb.net/?appName=music-auth

# Authentication
JWT_SECRET=31b4acf9af538820ff368524dfab4835a0191b17a164819afdd810a1ae9925fe28c7d97bd206065053da17f81d8af171a57bcd142c7509f1857d2f69f87d3b30
JWT_EXPIRES_IN=90d

# Frontend URL (CORS Configuration)
FRONTEND_URL=http://localhost:8000
```

### CORS Configuration
- **Backend CORS**: Configured to accept requests from `http://localhost:8000`
- **Frontend Server**: Runs on port 8000
- **Backend API**: Runs on port 5000

## 🎨 Frontend Details

### Main Components

1. **Music Player Interface (index.html)**
   - YouTube video player integration
   - Playlist management
   - User authentication status
   - Purple theme design

2. **Authentication Pages (auth/)**
   - Sign in form with validation
   - Sign up form with user registration
   - Password security features

3. **Settings Page (settings.html)**
   - User profile management
   - Preference customization
   - Account settings

### Key JavaScript Functions

- `showSection(sectionName)` - Navigate between app sections
- `searchMusic()` - Search and play YouTube music
- `createPlaylist()` - Create new playlists
- `loadPlaylists()` - Load user's playlists
- `login()`, `register()` - Authentication functions

## 🔒 Security Features

### Authentication Security
- **Password Hashing**: bcryptjs with salt rounds
- **JWT Tokens**: Secure token-based authentication
- **Token Expiration**: 90-day token validity
- **Input Validation**: Express-validator for all inputs

### Database Security
- **MongoDB Atlas**: Encrypted cloud database
- **Connection Security**: Secure connection strings
- **Data Validation**: Mongoose schema validation

### CORS Protection
- **Origin Validation**: Only localhost:8000 allowed
- **Credentials**: Secure credential handling
- **Headers**: Proper CORS header configuration

## 🐛 Troubleshooting

### Common Issues

**CORS Errors:**
- Ensure backend CORS origin matches frontend URL
- Check `FRONTEND_URL=http://localhost:8000` in .env
- Verify frontend server runs on port 8000

**MongoDB Connection:**
- Verify MongoDB Atlas connection string
- Check network connectivity
- Ensure database user has proper permissions

**JWT Errors:**
- Verify JWT_SECRET is set in .env
- Check token expiration settings
- Ensure proper authorization headers

### Debug Commands
```bash
# Check if ports are in use
lsof -i :8000  # Frontend
lsof -i :5000  # Backend

# View backend logs
npm run dev

# Test API health
curl http://localhost:5000/api/health
```

## 📈 Future Enhancements

- **Social Features**: Share playlists with friends
- **Advanced Search**: Filter by genre, artist, year
- **Offline Mode**: Download songs for offline listening
- **Mobile App**: React Native mobile application
- **Premium Features**: Ad-free experience, high-quality audio
- **Analytics**: User listening statistics and recommendations

## 📝 Development Notes

### Backend Architecture
- **Middleware**: Authentication, CORS, error handling
- **Models**: User schema with playlists and preferences
- **Routes**: RESTful API design with proper HTTP methods
- **Validation**: Input sanitization and validation

### Frontend Architecture
- **Modular JavaScript**: Separate concerns for auth, music, UI
- **API Integration**: Async/await for backend communication
- **State Management**: Client-side user session management
- **Responsive Design**: Mobile-first CSS approach

## 👥 Credits

- **YouTube API**: For music streaming capabilities
- **MongoDB Atlas**: Cloud database hosting
- **Express.js**: Web framework foundation
- **Bootstrap/Tailwind**: UI component inspiration

## 📄 License

This project is for educational purposes as a final year project demonstration.

---

**🎵 Ready to rock? Start your music journey now! 🎵**