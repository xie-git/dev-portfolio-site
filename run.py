#!/usr/bin/env python3
"""
Portfolio Website - Flask Application Entry Point
Run this file to start the development server.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_and_run():
    """Setup virtual environment, install dependencies, and run the app."""
    project_root = Path(__file__).parent
    venv_path = project_root / "venv"
    
    # Check if we're in a virtual environment
    in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    
    if not in_venv:
        print("🔧 Setting up virtual environment...")
        
        # Create virtual environment if it doesn't exist
        if not venv_path.exists():
            print("📦 Creating virtual environment...")
            subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
        
        # Determine the correct activation script and python executable
        if os.name == 'nt':  # Windows
            python_exe = venv_path / "Scripts" / "python.exe"
            pip_exe = venv_path / "Scripts" / "pip.exe"
        else:  # Unix/Linux/macOS
            python_exe = venv_path / "bin" / "python"
            pip_exe = venv_path / "bin" / "pip"
        
        # Install dependencies
        print("📥 Installing dependencies...")
        subprocess.run([str(pip_exe), "install", "-r", "requirements.txt"], check=True)
        
        # Re-run this script with the virtual environment Python
        print("🚀 Starting application with virtual environment...")
        subprocess.run([str(python_exe), __file__], check=True)
        return
    
    # If we're here, we're in the virtual environment
    print("✅ Virtual environment active!")
    run_flask_app()

def run_flask_app():
    """Run the Flask application."""
    from datetime import date, datetime
    
    # Import Flask components
    try:
        from app.simple_init import create_app, db
        from app.models import Project, Experience, Skill, SiteSettings
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all dependencies are installed.")
        sys.exit(1)
    
    # Create Flask application
    app = create_app()
    
    def init_db():
        """Initialize database and create sample data if tables are empty."""
        with app.app_context():
            # Create all database tables
            db.create_all()
            
            # Check if we need to add sample data
            try:
                if Project.query.count() == 0:
                    print("Creating sample data...")
                    create_sample_data()
                    print("Sample data created successfully!")
            except Exception as e:
                print(f"Creating sample data (first run): {e}")
                create_sample_data()
                print("Sample data created successfully!")

    def create_sample_data():
        """Create sample data for the portfolio."""
        
        # Real Projects based on resume
        projects = [
            {
                'title': 'Homelab Linux Server',
                'description': 'Self-hosted infrastructure running on Linux server at 10.0.0.221. Provides all home serving purposes and needs with multiple self-hosted services including Docker containers, monitoring, and automation. Complete home infrastructure management with network services, file storage, media streaming, and development environments.',
                'short_description': 'Complete self-hosted home infrastructure with multiple services',
                'image_url': 'https://via.placeholder.com/600x400/2563eb/ffffff?text=Homelab+Server',
                'demo_url': 'http://10.0.0.221:5005',
                'github_url': 'https://github.com/xie-git/homelab-infrastructure',
                'technologies': 'Linux, Docker, Self-hosting, Network Management, Infrastructure',
                'featured': True,
                'order_index': 1
            },
            {
                'title': 'Chicago Real Estate Scraper',
                'description': 'Scalable real estate scraping service that continuously monitors and tracks Chicago\'s apartment and rental market. Automated data collection system that aggregates listings, pricing trends, and market analytics from multiple sources. Built for scalability to handle large volumes of real estate data with efficient processing and storage.',
                'short_description': 'Scalable service tracking Chicago\'s apartment and real estate market',
                'image_url': 'https://via.placeholder.com/600x400/06b6d4/ffffff?text=Real+Estate+Scraper',
                'github_url': 'https://github.com/xie-git/RealEstateScraper',
                'technologies': 'Python, Web Scraping, Data Pipeline, Market Analysis, Automation',
                'featured': True,
                'order_index': 2
            },
            {
                'title': 'Personal Real Estate Tracker',
                'description': 'Personal analytics dashboard for tracking the best apartment deals and real estate trends in Chicago. Combines data from the scraping service with custom algorithms to identify undervalued properties, market opportunities, and investment insights. Features trend analysis, price predictions, and automated alerts for optimal deals.',
                'short_description': 'Personal tracker for best apartment deals and market trends',
                'image_url': 'https://via.placeholder.com/600x400/10b981/ffffff?text=Real+Estate+Tracker',
                'github_url': 'https://github.com/xie-git/real-estate-tracker',
                'technologies': 'Python, Data Analysis, Market Trends, Investment Analytics, Dashboards',
                'featured': True,
                'order_index': 3
            },
            {
                'title': 'AI/ML Self-Hosted Lab',
                'description': 'Self-hosted AI/ML environment featuring Stable Diffusion and Ollama for model tuning and testing. Focus on developing scalable, cost-efficient AI solutions with custom model fine-tuning, prompt engineering, and deployment strategies. Experimenting with local LLMs, image generation, and efficient inference for practical use cases.',
                'short_description': 'Self-hosted AI/ML lab with Stable Diffusion and Ollama',
                'image_url': 'https://via.placeholder.com/600x400/8b5cf6/ffffff?text=AI%2FML+Lab',
                'github_url': 'https://github.com/xie-git/ai-ml-lab',
                'technologies': 'Stable Diffusion, Ollama, LLMs, Model Tuning, Self-hosting, AI/ML',
                'featured': True,
                'order_index': 4
            },
            {
                'title': 'HomeData IoT Sensor Network',
                'description': 'Comprehensive IoT sensor network gathering environmental and occupancy data throughout the home using BME688 environmental sensors and LD2450 presence detection. Built on ESP32 and Raspberry Pi platforms with AI/ML analytics to generate insights and optimize Home Assistant automation. Real-time monitoring, predictive analytics, and intelligent home automation.',
                'short_description': 'IoT sensor network with AI insights for home automation',
                'image_url': 'https://via.placeholder.com/600x400/f59e0b/ffffff?text=HomeData+IoT',
                'github_url': 'https://github.com/xie-git/HomeData',
                'technologies': 'IoT, BME688, LD2450, ESP32, Raspberry Pi, Home Assistant, AI/ML Analytics',
                'featured': True,
                'order_index': 5
            }
        ]
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        # Real Experience based on resume
        experiences = [
            {
                'title': 'Software Engineer (IAM)',
                'company': 'Northern Trust',
                'company_url': 'https://www.northerntrust.com',
                'location': 'Chicago, IL',
                'start_date': date(2025, 3, 1),
                'end_date': None,  # Current position
                'description': 'Developed and maintained Python-based ETL pipelines for enterprise identity systems using Linux and Control-M. Automated and migrated legacy IAM data into modern platforms using secure OracleDB and PostgreSQL connections. Provisioned on-prem infrastructure to support scheduled ETL workflows.',
                'experience_type': 'work',
                'order_index': 1
            },
            {
                'title': 'Software Engineer',
                'company': 'Capital One',
                'company_url': 'https://www.capitalone.com',
                'location': 'Chicago, IL',
                'start_date': date(2019, 8, 1),
                'end_date': date(2023, 11, 30),
                'description': 'Built scalable AWS Big Data ETL pipelines (Step Functions, EMR, DynamoDB, Lambda) using Python and PySpark to process sensitive customer credit and behavioral data. Created automated UI testing suite using Selenium and OpenCV. Engineered fraud analytics reporting system with SQL, Snowflake, R, and Python. Developed customer communication microservices using Java Spring Boot, containerized in Docker and deployed on ECS with CI/CD pipelines.',
                'experience_type': 'work',
                'order_index': 2
            },
            {
                'title': 'Operations Lead',
                'company': 'Northwestern Mutual',
                'company_url': 'https://www.northwesternmutual.com',
                'location': 'Milwaukee, WI',
                'start_date': date(2018, 6, 1),
                'end_date': date(2019, 8, 31),
                'description': 'Managed deployment of internal enterprise apps on iOS/Android using Microsoft Intune and Azure AD policies. Resolved authentication and MDM compliance issues across employee devices and collaborated with internal support and security teams. Coordinated between offshore development teams and on-site stakeholders; delivered weekly operations reports.',
                'experience_type': 'work',
                'order_index': 3
            },
            {
                'title': 'Statistics & Computer Science',
                'company': 'University of Wisconsin Madison',
                'company_url': 'https://www.wisc.edu',
                'location': 'Madison, WI',
                'start_date': date(2014, 8, 1),
                'end_date': date(2018, 5, 31),
                'description': 'Bachelor of Science in Statistics and Computer Science. Focused on data analysis, statistical modeling, and software development fundamentals.',
                'experience_type': 'education',
                'order_index': 4
            }
        ]
        
        for exp_data in experiences:
            experience = Experience(**exp_data)
            db.session.add(experience)
        
        # Real Skills based on resume
        skills = [
            # Languages
            {'name': 'Python', 'category': 'languages', 'proficiency': 95, 'icon_class': 'fab fa-python', 'order_index': 1},
            {'name': 'Java', 'category': 'languages', 'proficiency': 85, 'icon_class': 'fab fa-java', 'order_index': 2},
            {'name': 'R', 'category': 'languages', 'proficiency': 80, 'icon_class': 'fab fa-r-project', 'order_index': 3},
            {'name': 'SQL', 'category': 'languages', 'proficiency': 90, 'icon_class': 'fas fa-database', 'order_index': 4},
            
            # AWS Services
            {'name': 'AWS Lambda', 'category': 'aws', 'proficiency': 90, 'icon_class': 'fab fa-aws', 'order_index': 1},
            {'name': 'Step Functions', 'category': 'aws', 'proficiency': 85, 'icon_class': 'fab fa-aws', 'order_index': 2},
            {'name': 'EC2', 'category': 'aws', 'proficiency': 80, 'icon_class': 'fab fa-aws', 'order_index': 3},
            {'name': 'S3', 'category': 'aws', 'proficiency': 90, 'icon_class': 'fab fa-aws', 'order_index': 4},
            {'name': 'DynamoDB', 'category': 'aws', 'proficiency': 85, 'icon_class': 'fab fa-aws', 'order_index': 5},
            {'name': 'RDS', 'category': 'aws', 'proficiency': 80, 'icon_class': 'fab fa-aws', 'order_index': 6},
            
            # Frameworks & Tools
            {'name': 'PySpark', 'category': 'frameworks', 'proficiency': 90, 'icon_class': 'fas fa-fire', 'order_index': 1},
            {'name': 'Pandas', 'category': 'frameworks', 'proficiency': 95, 'icon_class': 'fas fa-chart-line', 'order_index': 2},
            {'name': 'Spring Boot', 'category': 'frameworks', 'proficiency': 85, 'icon_class': 'fas fa-leaf', 'order_index': 3},
            {'name': 'Docker', 'category': 'frameworks', 'proficiency': 80, 'icon_class': 'fab fa-docker', 'order_index': 4},
            {'name': 'Kafka', 'category': 'frameworks', 'proficiency': 75, 'icon_class': 'fas fa-stream', 'order_index': 5},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'databases', 'proficiency': 85, 'icon_class': 'fas fa-database', 'order_index': 1},
            {'name': 'OracleDB', 'category': 'databases', 'proficiency': 80, 'icon_class': 'fas fa-database', 'order_index': 2},
            {'name': 'Snowflake', 'category': 'databases', 'proficiency': 85, 'icon_class': 'fas fa-snowflake', 'order_index': 3},
            
            # Platforms
            {'name': 'Linux', 'category': 'platforms', 'proficiency': 85, 'icon_class': 'fab fa-linux', 'order_index': 1},
            {'name': 'Azure', 'category': 'platforms', 'proficiency': 75, 'icon_class': 'fab fa-microsoft', 'order_index': 2},
            {'name': 'Databricks', 'category': 'platforms', 'proficiency': 80, 'icon_class': 'fas fa-database', 'order_index': 3},
            
            # IoT & Homelab
            {'name': 'Home Assistant', 'category': 'iot', 'proficiency': 85, 'icon_class': 'fas fa-home', 'order_index': 1},
            {'name': 'ESP32', 'category': 'iot', 'proficiency': 80, 'icon_class': 'fas fa-microchip', 'order_index': 2},
            {'name': 'Raspberry Pi', 'category': 'iot', 'proficiency': 85, 'icon_class': 'fab fa-raspberry-pi', 'order_index': 3},
            {'name': 'Self-hosting', 'category': 'iot', 'proficiency': 90, 'icon_class': 'fas fa-server', 'order_index': 4},
            
            # AI/ML
            {'name': 'Stable Diffusion', 'category': 'ai', 'proficiency': 75, 'icon_class': 'fas fa-brain', 'order_index': 1},
            {'name': 'Ollama', 'category': 'ai', 'proficiency': 80, 'icon_class': 'fas fa-robot', 'order_index': 2},
            {'name': 'Model Tuning', 'category': 'ai', 'proficiency': 70, 'icon_class': 'fas fa-cogs', 'order_index': 3}
        ]
        
        for skill_data in skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
        
        # Site Settings with Michael's real information
        settings = [
            {'key': 'hero_title', 'value': 'Software Engineer'},
            {'key': 'hero_subtitle', 'value': 'Building scalable data pipelines and enterprise solutions with modern cloud technologies'},
            {'key': 'about_text', 'value': 'Experienced software engineer with 6+ years developing scalable ETL pipelines, big data solutions, and enterprise applications. Currently building a comprehensive homelab infrastructure with self-hosted services, IoT sensor networks, and AI/ML experimentation. Passionate about automation, data engineering, and creating efficient systems that solve real-world problems at home and in enterprise environments.'},
            {'key': 'resume_url', 'value': '/static/resume.pdf'},
            {'key': 'github_url', 'value': 'https://github.com/xie-git'},
            {'key': 'linkedin_url', 'value': 'https://linkedin.com/in/xie-michael'},
            {'key': 'email', 'value': 'xie.michael@icloud.com'},
            {'key': 'location', 'value': 'Chicago, IL'},
            {'key': 'phone', 'value': '262 527 6438'}
        ]
        
        for setting_data in settings:
            setting = SiteSettings(**setting_data)
            db.session.add(setting)
        
        # Commit all changes
        db.session.commit()

    # Initialize database on first run
    init_db()
    
    # Run the development server
    print("🚀 Starting Michael Xie's Portfolio Website...")
    print(f"💻 Visit: http://10.0.0.221:5005")
    print(f"🔧 Admin Panel: http://10.0.0.221:5005/admin")
    print("📧 Note: Configure email settings in .env for contact form")
    print("⚡ Press Ctrl+C to stop the server")
    
    app.run(
        host='10.0.0.221',
        port=5005,
        debug=False  # Set to False for production/background running
    )

if __name__ == '__main__':
    setup_and_run() 