# Michael Xie's Portfolio Setup Guide

## Quick Start on Server (10.0.0.221)

### 1. Pull Latest Changes
```bash
cd ~/dev-portfolio-site
git pull origin main
```

### 2. Start with Screen (Recommended)
```bash
# Make scripts executable (one time)
chmod +x start_portfolio.sh stop_portfolio.sh

# Start the portfolio
./start_portfolio.sh
```

### 3. Access Your Portfolio
- **Website:** http://10.0.0.221:5005
- **Admin Panel:** http://10.0.0.221:5005/admin (to edit content)

## Portfolio Projects Initialized

✅ **Homelab Linux Server** - Self-hosted infrastructure at 10.0.0.221  
✅ **Chicago Real Estate Scraper** - Scalable market tracking service  
✅ **Personal Real Estate Tracker** - Best deals and trends analysis  
✅ **AI/ML Self-Hosted Lab** - Stable Diffusion & Ollama experimentation  
✅ **HomeData IoT Sensor Network** - BME688, LD2450, ESP32, Raspberry Pi automation  

## Screen Management

### Start Portfolio
```bash
./start_portfolio.sh
```

### View Running Portfolio
```bash
screen -r portfolio
# Press Ctrl+A, then D to detach
```

### Stop Portfolio
```bash
./stop_portfolio.sh
```

### Check Status
```bash
screen -list
```

## Alternative: Systemd Service (Production)

For permanent background service:

```bash
# Copy service file
sudo cp portfolio.service /etc/systemd/system/

# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable portfolio.service
sudo systemctl start portfolio.service

# Check status
sudo systemctl status portfolio.service
```

## Skills Categories Added

- **Languages:** Python, Java, R, SQL
- **AWS:** Lambda, Step Functions, S3, DynamoDB, RDS, EC2
- **Frameworks:** PySpark, Pandas, Spring Boot, Docker, Kafka
- **Databases:** PostgreSQL, OracleDB, Snowflake
- **Platforms:** Linux, Azure, Databricks
- **IoT & Homelab:** Home Assistant, ESP32, Raspberry Pi, Self-hosting
- **AI/ML:** Stable Diffusion, Ollama, Model Tuning

## Contact Information

- **Email:** xie.michael@icloud.com
- **Phone:** 262 527 6438
- **Location:** Chicago, IL
- **GitHub:** https://github.com/xie-git
- **LinkedIn:** https://linkedin.com/in/xie-michael

## Troubleshooting

### Check if Running
```bash
ps aux | grep python | grep run.py
```

### View Logs
```bash
# If using screen
screen -r portfolio

# If using systemd
sudo journalctl -u portfolio.service -f
```

### Kill Process
```bash
pkill -f run.py
```

---

**🚀 Your portfolio is now ready with your real homelab projects!** 