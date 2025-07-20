# 🚀 Michael Xie Portfolio - Production Deployment Guide

## Quick Start (Git Workflow)

### 1. Push from Development Machine
```bash
git add .
git commit -m "Portfolio updates"
git push origin main
```

### 2. Deploy on Linux Server
```bash
# Clone or pull latest changes
git clone https://github.com/yourusername/portfolio.git  # First time
# OR
git pull origin main  # Updates

# Deploy automatically
./deploy.sh production 5000
```

## ✅ **What's Production Ready Now:**

- ✅ **Error Handling**: 404/500 pages with consistent design
- ✅ **SEO Optimized**: Meta tags, Open Graph, Twitter cards
- ✅ **Performance**: Static file caching, optimized delivery
- ✅ **WSGI Compatible**: Works with Gunicorn for production
- ✅ **Environment Variables**: Secure configuration
- ✅ **Auto Deployment**: One-command setup on any Linux server

## 📋 **Deployment Options**

### Option 1: Internal Network (Easiest)
```bash
./deploy.sh development 5000  # Development mode
./deploy.sh production 5000   # Production mode
```
Access via: `http://your-server-ip:5000`

### Option 2: Public with Nginx (Recommended)
1. **Setup Nginx reverse proxy**:
   ```bash
   sudo cp nginx.conf.template /etc/nginx/sites-available/portfolio
   sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/
   sudo nginx -t && sudo systemctl reload nginx
   ```

2. **Run application**:
   ```bash
   ./deploy.sh production 5000
   ```

### Option 3: Systemd Service (Auto-restart)
```bash
# Create service file
sudo nano /etc/systemd/system/portfolio.service

# Add content:
[Unit]
Description=Michael Xie Portfolio
After=network.target

[Service]
User=yourusername
WorkingDirectory=/path/to/portfolio
Environment=PATH=/path/to/portfolio/venv/bin
ExecStart=/path/to/portfolio/venv/bin/gunicorn --bind 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target

# Enable and start
sudo systemctl enable portfolio
sudo systemctl start portfolio
```

## 🌐 **Going Public (When Ready)**

### 1. Domain Setup
- Point your domain to your server IP
- Update `nginx.conf.template` with your domain
- Get SSL certificate (Let's Encrypt recommended)

### 2. SSL Certificate (Free with Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 3. Security (Future Phase)
```bash
# Firewall
sudo ufw allow 22  # SSH
sudo ufw allow 80  # HTTP
sudo ufw allow 443 # HTTPS
sudo ufw enable

# Auto-renewal for SSL
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 🔧 **Development Workflow**

### Local Development
```bash
python app.py  # Windows/Mac
./deploy.sh development  # Linux
```

### Production Testing
```bash
./deploy.sh production 8000  # Test on different port
```

### Updates
```bash
git pull origin main
./deploy.sh production  # Auto-restarts with new code
```

## 📊 **Performance & Monitoring**

### Current Optimizations
- ✅ Gzip compression
- ✅ Static file caching
- ✅ Optimized fonts (local hosting)
- ✅ Minimal CSS/JS
- ✅ Error handling

### Future Additions
- [ ] Analytics integration
- [ ] Performance monitoring
- [ ] Backup automation
- [ ] CDN integration

## 🐳 **Docker Alternative (If Preferred)**

```bash
# Create Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Build and run
docker build -t portfolio .
docker run -p 5000:5000 portfolio
```

## 🎯 **What You Need to Complete:**

1. **📸 Project Images** - Replace emoji placeholders
2. **🎨 Favicon** - Add `favicon.ico` to `/static/`
3. **🌐 Domain** - When ready to go public
4. **📧 Contact Form** - If you want email functionality

## 📞 **Support Commands**

```bash
# Check if site is running
curl http://localhost:5000

# View logs
tail -f /var/log/nginx/access.log
journalctl -u portfolio -f

# Restart services
sudo systemctl restart portfolio
sudo systemctl restart nginx
```

**Your portfolio is now production-ready for internal hosting and easily scalable to public deployment!** 🚀 