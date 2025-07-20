# 🔄 Development & Deployment Workflows

This guide covers both local development and server deployment workflows for the portfolio website.

## 🖥️ **Local Development Workflow**

### **Windows/Mac Quick Start**
```bash
# Clone the repository
git clone https://github.com/yourusername/dev-portfolio-site.git
cd dev-portfolio-site

# Start local development server
python run_local.py
```

### **What This Does:**
- ✅ Imports the Flask app from `app.py`
- ✅ Sets `FLASK_DEBUG=True` for auto-reload
- ✅ Runs on `http://localhost:5000` 
- ✅ Enables debug mode for development
- ✅ Works on Windows, Mac, and Linux

### **Local Development Features:**
- **Auto-reload**: Changes to code automatically restart server
- **Debug mode**: Detailed error messages in browser
- **No setup required**: Just run one command
- **Port 5000**: Standard Flask development port

---

## 🚀 **Server Deployment Workflow**

### **Initial Server Setup**
```bash
# On your server (Linux)
git clone https://github.com/yourusername/dev-portfolio-site.git
cd dev-portfolio-site

# Deploy in production mode
chmod +x deploy.sh
./deploy.sh production 5000
```

### **Update Workflow (After Making Changes)**
```bash
# 1. On your development machine - push changes
git add .
git commit -m "Updated portfolio"
git push origin main

# 2. On your server - pull and redeploy
git pull origin main
./deploy.sh production 5000
```

### **What Server Deploy Does:**
- ✅ Creates virtual environment (`venv/`)
- ✅ Installs dependencies from `requirements.txt`
- ✅ Generates secure production secret key
- ✅ Runs with Gunicorn WSGI server
- ✅ Optimized for production traffic
- ✅ Accessible on network: `http://SERVER-IP:5000`

---

## 📋 **Workflow Comparison**

| Feature | Local Development | Server Production |
|---------|------------------|------------------|
| **Command** | `python run_local.py` | `./deploy.sh production 5000` |
| **Server** | Flask dev server | Gunicorn WSGI |
| **Debug** | Enabled | Disabled |
| **Auto-reload** | Yes | No |
| **Performance** | Development | Production-optimized |
| **Access** | localhost:5000 | SERVER-IP:5000 |
| **Setup** | Zero setup | Virtual env + deps |

---

## 🔧 **Troubleshooting**

### **Local Development Issues**

#### Port Already in Use
```bash
# Check what's using port 5000
netstat -ano | findstr :5000  # Windows
lsof -i :5000                 # Mac/Linux

# Kill the process or use different port
# Edit run_local.py and change port=5000 to port=8000
```

#### Import Errors
```bash
# Make sure you're in the project directory
cd dev-portfolio-site

# Check if app.py exists
ls -la app.py  # Mac/Linux
dir app.py     # Windows
```

### **Server Deployment Issues**

#### Permission Denied
```bash
# Make deploy script executable
chmod +x deploy.sh

# Check file permissions
ls -la deploy.sh
```

#### Python Not Found
```bash
# Install Python on Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-venv python3-pip

# Install Python on CentOS/RHEL
sudo yum install python3 python3-venv python3-pip
```

#### Port in Use on Server
```bash
# Check what's using the port
sudo netstat -tlnp | grep :5000

# Use different port
./deploy.sh production 8000
```

---

## ⚡ **Quick Commands Reference**

### **Local Development**
```bash
# Start development server
python run_local.py

# Start with custom port (edit run_local.py first)
python run_local.py
```

### **Server Deployment**
```bash
# Production deployment
./deploy.sh production 5000

# Development mode on server (for testing)
./deploy.sh development 5000

# Custom port
./deploy.sh production 8080
```

### **Git Workflow**
```bash
# Push changes from local
git add .
git commit -m "Description of changes"
git push origin main

# Pull changes on server
git pull origin main
./deploy.sh production 5000
```

---

## 🎯 **Best Practices**

### **Local Development**
1. ✅ Always test changes locally first
2. ✅ Use `run_local.py` for development
3. ✅ Commit frequently with descriptive messages
4. ✅ Test on both desktop and mobile browsers

### **Server Deployment**
1. ✅ Pull latest changes before deploying
2. ✅ Use production mode for live sites
3. ✅ Monitor logs for errors
4. ✅ Keep backups of working deployments

### **Git Workflow**
1. ✅ Test locally → Commit → Push → Pull on server → Deploy
2. ✅ Use descriptive commit messages
3. ✅ Don't commit local testing files
4. ✅ Pull before making new changes

---

## 🌐 **Going Public (Optional)**

When ready to make your portfolio public:

1. **Get a domain name**
2. **Set up Nginx reverse proxy** (see `DEPLOYMENT.md`)
3. **Configure SSL certificate** (Let's Encrypt)
4. **Update DNS records**

See `DEPLOYMENT.md` for complete public deployment guide.

---

**Both workflows are now fully tested and production-ready!** 🚀 