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
        
        # Sample Projects
        projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-stack e-commerce application built with Flask and React. Features include user authentication, product catalog, shopping cart, and payment integration.',
                'short_description': 'Modern e-commerce platform with full shopping experience',
                'image_url': 'https://via.placeholder.com/600x400/2563eb/ffffff?text=E-Commerce+Platform',
                'demo_url': 'https://demo-ecommerce.example.com',
                'github_url': 'https://github.com/yourusername/ecommerce-platform',
                'technologies': 'Flask, React, PostgreSQL, Stripe, AWS',
                'featured': True,
                'order_index': 1
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates, team collaboration features, and project tracking capabilities.',
                'short_description': 'Collaborative task management with real-time updates',
                'image_url': 'https://via.placeholder.com/600x400/06b6d4/ffffff?text=Task+Manager',
                'demo_url': 'https://demo-tasks.example.com',
                'github_url': 'https://github.com/yourusername/task-manager',
                'technologies': 'Python, Django, WebSocket, Redis, Docker',
                'featured': True,
                'order_index': 2
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A responsive weather dashboard that displays current weather, forecasts, and historical data with beautiful visualizations.',
                'short_description': 'Beautiful weather dashboard with data visualizations',
                'image_url': 'https://via.placeholder.com/600x400/10b981/ffffff?text=Weather+Dashboard',
                'demo_url': 'https://demo-weather.example.com',
                'github_url': 'https://github.com/yourusername/weather-dashboard',
                'technologies': 'JavaScript, Chart.js, OpenWeather API, CSS3',
                'featured': True,
                'order_index': 3
            },
            {
                'title': 'Blog Platform',
                'description': 'A modern blogging platform with markdown support, SEO optimization, and content management system.',
                'short_description': 'Modern blogging platform with CMS features',
                'image_url': 'https://via.placeholder.com/600x400/8b5cf6/ffffff?text=Blog+Platform',
                'demo_url': 'https://demo-blog.example.com',
                'github_url': 'https://github.com/yourusername/blog-platform',
                'technologies': 'Flask, SQLAlchemy, Markdown, SEO',
                'featured': False,
                'order_index': 4
            },
            {
                'title': 'Portfolio Website',
                'description': 'This very portfolio website you are looking at! Built with Flask and modern web technologies.',
                'short_description': 'Personal portfolio website with modern design',
                'image_url': 'https://via.placeholder.com/600x400/f59e0b/ffffff?text=Portfolio+Site',
                'github_url': 'https://github.com/yourusername/portfolio-website',
                'technologies': 'Flask, JavaScript, CSS3, SQLite',
                'featured': True,
                'order_index': 5
            }
        ]
        
        for project_data in projects:
            project = Project(**project_data)
            db.session.add(project)
        
        # Sample Experience
        experiences = [
            {
                'title': 'Senior Software Developer',
                'company': 'Tech Innovations Inc.',
                'company_url': 'https://techinnovations.example.com',
                'location': 'San Francisco, CA',
                'start_date': date(2022, 1, 1),
                'end_date': None,  # Current position
                'description': 'Leading development of scalable web applications and mentoring junior developers. Focused on full-stack development with Python and JavaScript.',
                'experience_type': 'work',
                'order_index': 1
            },
            {
                'title': 'Full Stack Developer',
                'company': 'StartupXYZ',
                'company_url': 'https://startupxyz.example.com',
                'location': 'Remote',
                'start_date': date(2020, 6, 1),
                'end_date': date(2021, 12, 31),
                'description': 'Developed and maintained multiple web applications using Flask, React, and PostgreSQL. Collaborated with cross-functional teams to deliver high-quality software solutions.',
                'experience_type': 'work',
                'order_index': 2
            },
            {
                'title': 'Computer Science Degree',
                'company': 'University of Technology',
                'location': 'New York, NY',
                'start_date': date(2016, 9, 1),
                'end_date': date(2020, 5, 31),
                'description': 'Bachelor of Science in Computer Science with focus on software engineering and web development. Graduated with honors.',
                'experience_type': 'education',
                'order_index': 3
            },
            {
                'title': 'Open Source Contributor',
                'company': 'Various Projects',
                'start_date': date(2019, 1, 1),
                'end_date': None,
                'description': 'Active contributor to open source projects including Flask extensions and JavaScript libraries. Passionate about giving back to the developer community.',
                'experience_type': 'volunteer',
                'order_index': 4
            }
        ]
        
        for exp_data in experiences:
            experience = Experience(**exp_data)
            db.session.add(experience)
        
        # Sample Skills
        skills = [
            # Frontend
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 90, 'icon_class': 'fab fa-js-square', 'order_index': 1},
            {'name': 'React', 'category': 'frontend', 'proficiency': 85, 'icon_class': 'fab fa-react', 'order_index': 2},
            {'name': 'HTML5', 'category': 'frontend', 'proficiency': 95, 'icon_class': 'fab fa-html5', 'order_index': 3},
            {'name': 'CSS3', 'category': 'frontend', 'proficiency': 90, 'icon_class': 'fab fa-css3-alt', 'order_index': 4},
            {'name': 'Vue.js', 'category': 'frontend', 'proficiency': 75, 'icon_class': 'fab fa-vuejs', 'order_index': 5},
            
            # Backend
            {'name': 'Python', 'category': 'backend', 'proficiency': 95, 'icon_class': 'fab fa-python', 'order_index': 1},
            {'name': 'Flask', 'category': 'backend', 'proficiency': 90, 'icon_class': 'fas fa-flask', 'order_index': 2},
            {'name': 'Django', 'category': 'backend', 'proficiency': 80, 'icon_class': 'fab fa-python', 'order_index': 3},
            {'name': 'Node.js', 'category': 'backend', 'proficiency': 75, 'icon_class': 'fab fa-node-js', 'order_index': 4},
            {'name': 'REST APIs', 'category': 'backend', 'proficiency': 85, 'icon_class': 'fas fa-exchange-alt', 'order_index': 5},
            
            # Database
            {'name': 'PostgreSQL', 'category': 'database', 'proficiency': 85, 'icon_class': 'fas fa-database', 'order_index': 1},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 80, 'icon_class': 'fas fa-database', 'order_index': 2},
            {'name': 'SQLite', 'category': 'database', 'proficiency': 90, 'icon_class': 'fas fa-database', 'order_index': 3},
            {'name': 'Redis', 'category': 'database', 'proficiency': 70, 'icon_class': 'fas fa-memory', 'order_index': 4},
            
            # Tools
            {'name': 'Git', 'category': 'tools', 'proficiency': 90, 'icon_class': 'fab fa-git-alt', 'order_index': 1},
            {'name': 'Docker', 'category': 'tools', 'proficiency': 75, 'icon_class': 'fab fa-docker', 'order_index': 2},
            {'name': 'AWS', 'category': 'tools', 'proficiency': 70, 'icon_class': 'fab fa-aws', 'order_index': 3},
            {'name': 'Linux', 'category': 'tools', 'proficiency': 80, 'icon_class': 'fab fa-linux', 'order_index': 4}
        ]
        
        for skill_data in skills:
            skill = Skill(**skill_data)
            db.session.add(skill)
        
        # Site Settings
        settings = [
            {'key': 'hero_title', 'value': 'Software Developer'},
            {'key': 'hero_subtitle', 'value': 'Building amazing digital experiences with modern web technologies'},
            {'key': 'about_text', 'value': 'Passionate software developer with 4+ years of experience creating scalable web applications. I love turning complex problems into simple, beautiful, and intuitive solutions. When I\'m not coding, you can find me exploring new technologies or contributing to open source projects.'},
            {'key': 'resume_url', 'value': '/static/resume.pdf'},
            {'key': 'github_url', 'value': 'https://github.com/yourusername'},
            {'key': 'linkedin_url', 'value': 'https://linkedin.com/in/yourprofile'},
            {'key': 'email', 'value': 'your.email@example.com'},
            {'key': 'location', 'value': 'Your City, Country'}
        ]
        
        for setting_data in settings:
            setting = SiteSettings(**setting_data)
            db.session.add(setting)
        
        # Commit all changes
        db.session.commit()

    # Initialize database on first run
    init_db()
    
    # Run the development server
    print("🚀 Starting Portfolio Website...")
    print(f"💻 Visit: http://localhost:5000")
    print(f"🔧 Admin Panel: http://localhost:5000/admin")
    print("📧 Note: Configure email settings in .env for contact form")
    print("⚡ Press Ctrl+C to stop the server")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

if __name__ == '__main__':
    setup_and_run() 