#!/usr/bin/env python3
"""
Simple Portfolio Website - Works immediately without complex setup
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
        
        # Install minimal dependencies
        print("📥 Installing dependencies...")
        subprocess.run([str(pip_exe), "install", "Flask==3.0.0"], check=True)
        
        # Re-run this script with the virtual environment Python
        print("🚀 Starting application with virtual environment...")
        subprocess.run([str(python_exe), __file__], check=True)
        return
    
    # If we're here, we're in the virtual environment
    print("✅ Virtual environment active!")
    run_simple_app()

def run_simple_app():
    """Run a simple Flask application."""
    from flask import Flask, render_template_string, jsonify, send_from_directory
    import os
    
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Project data
    projects = [
        {
            'id': 'homelab',
            'title': 'Personal HomeLab',
            'type': 'Infrastructure & DevOps',
            'placeholder': '🏠',
            'description': 'Self-hosted Linux server infrastructure serving custom applications and services for home automation and productivity.',
            'details': {
                'overview': 'A comprehensive home server setup running on Linux, providing self-hosted alternatives to cloud services while maintaining full control over data and functionality.',
                'tech_stack': ['Linux Server', 'Docker', 'Nginx', 'PostgreSQL', 'Redis', 'Monitoring Stack'],
                'features': [
                    'Media streaming and management',
                    'Network-attached storage (NAS)',
                    'VPN server for secure remote access',
                    'Automated backup systems',
                    'Custom web applications',
                    'Home automation integrations'
                ],
                'challenges': 'Designing a robust, scalable infrastructure that balances performance, security, and maintainability while keeping costs low.',
                'impact': 'Reduced dependency on cloud services, improved privacy, and created a testing environment for new technologies.'
            }
        },
        {
            'id': 'real-estate',
            'title': 'Real Estate Analytics',
            'type': 'Data Engineering & Visualization',
            'placeholder': '📊',
            'description': 'Automated Chicago real estate and rental market data scraping with comprehensive Grafana visualization dashboards.',
            'details': {
                'overview': 'A data pipeline that automatically collects, processes, and visualizes Chicago real estate and rental market trends to provide actionable insights.',
                'tech_stack': ['Python', 'Beautiful Soup', 'Selenium', 'PostgreSQL', 'Grafana', 'Docker', 'Cron Jobs'],
                'features': [
                    'Multi-source data scraping (Zillow, Apartments.com, etc.)',
                    'Real-time market trend analysis',
                    'Price prediction modeling',
                    'Neighborhood comparison tools',
                    'Automated alert systems',
                    'Historical data tracking'
                ],
                'challenges': 'Handling anti-scraping measures, data normalization across different sources, and creating meaningful visualizations.',
                'impact': 'Enabled data-driven real estate decisions and provided insights into Chicago market patterns.'
            }
        },
        {
            'id': 'ai-ml',
            'title': 'AI/ML Playground',
            'type': 'Artificial Intelligence',
            'placeholder': '🤖',
            'description': 'Self-hosted AI infrastructure featuring Stable Diffusion image generation and Ollama language models for experimentation.',
            'details': {
                'overview': 'A local AI development environment for experimenting with cutting-edge machine learning models while maintaining privacy and control.',
                'tech_stack': ['Stable Diffusion', 'Ollama', 'Python', 'PyTorch', 'CUDA', 'FastAPI', 'Docker'],
                'features': [
                    'Local Stable Diffusion image generation',
                    'Multiple LLM model hosting with Ollama',
                    'Custom model fine-tuning pipeline',
                    'API endpoints for integration',
                    'Prompt engineering tools',
                    'Model performance monitoring'
                ],
                'challenges': 'Optimizing model performance on consumer hardware, managing GPU memory efficiently, and creating intuitive interfaces.',
                'impact': 'Accelerated AI/ML learning and provided a foundation for integrating AI into other projects.'
            }
        },
        {
            'id': 'smart-home',
            'title': 'Smart Home IoT',
            'type': 'IoT & Home Automation',
            'placeholder': '🏡',
            'description': 'Comprehensive sensor network with BME688, LD2450, and custom IoT devices integrated with Home Assistant automation.',
            'details': {
                'overview': 'An intelligent home automation system using various sensors and custom IoT devices to create a responsive living environment.',
                'tech_stack': ['Home Assistant', 'ESPHome', 'MQTT', 'BME688 Sensors', 'LD2450 Radar', 'Arduino', 'Zigbee'],
                'features': [
                    'Environmental monitoring (temperature, humidity, air quality)',
                    'Human presence detection with millimeter-wave radar',
                    'Automated lighting and climate control',
                    'Energy consumption tracking',
                    'Security system integration',
                    'Voice control and mobile app access'
                ],
                'challenges': 'Ensuring reliable wireless communication, balancing automation with manual control, and maintaining system stability.',
                'impact': 'Improved energy efficiency, enhanced security, and created a more comfortable living environment.'
            }
        }
    ]
    
    # Homepage template - EXACT Long Nguyen structure
    home_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Michael Xie - Software Engineer</title>
        <meta name="description" content="Michael Xie is a software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems. 5+ years experience in fintech and enterprise software.">
        <meta name="keywords" content="Michael Xie, Software Engineer, Python, AWS, Data Engineering, ETL, Cloud Infrastructure, Chicago">
        <meta name="author" content="Michael Xie">
        
        <!-- Open Graph / Facebook -->
        <meta property="og:type" content="website">
        <meta property="og:title" content="Michael Xie - Software Engineer">
        <meta property="og:description" content="Software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems.">
        <meta property="og:url" content="https://micheal-xie.dev">
        
        <!-- Twitter -->
        <meta property="twitter:card" content="summary">
        <meta property="twitter:title" content="Michael Xie - Software Engineer">
        <meta property="twitter:description" content="Software engineer specializing in big data ETL pipelines, cloud infrastructure, and scalable systems.">
        
        <!-- Favicon -->
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
        
        <style>
            /* EXACT Long Nguyen Font Loading - LOCAL HOSTING */
            @font-face {
                font-family: 'PP Neue Montreal';
                src: url('/static/fonts/PPNeueMontreal-Regular.woff') format("woff");
                font-weight: 400;
                font-style: normal;
                font-display: swap;
            }

            @font-face {
                font-family: 'PP Neue Montreal';
                src: url('/static/fonts/PPNeueMontreal-Italic.woff') format("woff");
                font-weight: 400;
                font-style: italic;
                font-display: swap;
            }

            /* EXACT Long Nguyen CSS Variables */
            :root {
                --color-bg-main: #fffbfc;
                --color-fg-main: #2d1724;
                --spacing-xs: .25rem;
                --spacing-sm: .5rem;
                --spacing-md: 1.5rem;
                --spacing-lg: 2rem;
                --spacing-xl: 3rem;
                --spacing-xxl: 4rem;
            }
            
            /* EXACT Long Nguyen Base Styles */
            * {
                box-sizing: border-box;
            }
            
            body {
                position: relative;
                min-height: calc(100vh - env(safe-area-inset-bottom));
                margin: 0;
                padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);
                display: flex;
                flex-flow: column nowrap;
                font: 1.5rem 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
                color: var(--color-fg-main);
                background: var(--color-bg-main);
            }

            body > * {
                flex: 1 0 auto;
            }
            
            /* EXACT Long Nguyen Typography */
            h1, h2, h3, h4, h5, h6 {
                margin: 0;
                font-size: 1.5rem;
                font-weight: 400;
            }

            h1 {
                font-size: 2.5rem;
                text-transform: uppercase;
            }

            button {
                border: 0;
                background: none;
                padding: 0;
            }

            a {
                color: inherit;
                text-decoration: underline;
            }

            code {
                background: rgba(45, 23, 36, .1);
                padding: .05em .25em .1em;
            }

            a:visited {
                color: inherit;
            }

            /* EXACT Long Nguyen Utility Classes */
            .block {
                margin: auto;
                width: 100%;
                max-width: 66ch;
            }
            
            .flex {
                display: flex;
            }
            
            .flex-grow {
                flex: 1 0 auto;
            }
            
            .flex-columns {
                flex-direction: column;
            }
            
            .flex-nowrap {
                flex-wrap: nowrap;
            }

            /* EXACT Long Nguyen Container System */
            .container {
                position: relative;
                --spacing-vertical: 0;
                --spacing-horizontal: 0;
                --configuration: var(--spacing-vertical) var(--spacing-horizontal);
            }

            .horizontal {
                --spacing-horizontal: var(--spacing-md);
            }

            .padding {
                padding: var(--configuration);
            }

            .margin {
                margin: var(--configuration);
            }
            
            /* EXACT Long Nguyen Header */
            header {
                background: var(--color-bg-main);
                position: sticky;
                bottom: 0;
                order: 2;
                z-index: 10;
            }

            header h2 {
                font-size: 1.5rem;
                font-weight: 400;
                margin: 0 auto 0 0;
            }

            nav {
                position: relative;
            }

            .container-actions {
                padding: var(--spacing-md) 0;
                display: flex;
                flex-flow: row nowrap;
            }

            header ul {
                margin: 0;
                padding: 0;
            }

            header li {
                list-style: none;
                margin: 0 var(--spacing-sm);
            }

            .links-container {
                display: flex;
                flex-flow: row nowrap;
                align-items: flex-end;
            }

            .links-list {
                display: flex;
                align-items: flex-end;
            }

            .container-actions .links-list {
                flex-flow: row nowrap;
            }
            
            /* EXACT Long Nguyen Content Styles */
            .intro-container p {
                margin-bottom: var(--spacing-md);
                max-width: 512px;
            }

            .intro-container ul {
                padding: 0;
                list-style: none;
            }

            .intro-container {
                margin-top: var(--spacing-xxl);
                margin-bottom: 6rem;
            }

            /* EXACT Long Nguyen Works Section */
            .works-section {
                margin: 4.5rem auto;
            }

            .works-section h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) auto;
            }

            /* EXACT Long Nguyen Project Cards */
            .project-card h3 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: 0;
            }

            .project-card p {
                font-size: 1rem;
                opacity: .5;
                margin: 0;
            }

            .project-card img {
                aspect-ratio: 3 / 2;
                object-fit: cover;
                width: 100%;
                border: 1px solid var(--color-fg-main);
            }

            .project-card {
                display: flex;
                flex-flow: column nowrap;
                row-gap: var(--spacing-sm);
                margin: var(--spacing-sm) auto;
                width: 100%;
            }

            .project-card .fade {
                opacity: 50%;
            }

            .project-placeholder {
                aspect-ratio: 3 / 2;
                width: 100%;
                border: 1px solid var(--color-fg-main);
                background: #f5f5f5;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2rem;
                color: var(--color-fg-main);
                opacity: 0.3;
            }

            .project-card {
                cursor: pointer;
                transition: transform 0.2s ease;
            }

            .project-card:hover {
                transform: translateY(-2px);
            }

            /* See All Projects Link */
            .see-all-container {
                text-align: right;
                margin-top: var(--spacing-lg);
            }

            .see-all-link {
                color: var(--color-fg-main);
                text-decoration: none;
                font-size: 0.875rem;
                opacity: 0.6;
                transition: opacity 0.3s ease;
            }

            .see-all-link:hover {
                opacity: 1;
                text-decoration: underline;
            }

            /* Modal Styles - Ultra Minimal & Centered */
            .modal {
                display: none;
                position: fixed;
                z-index: 1000;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background: rgba(45, 23, 36, 0.8);
                align-items: center;
                justify-content: center;
            }

            .modal.show {
                display: flex;
            }

            .modal-content {
                background: var(--color-bg-main);
                border: 1px solid var(--color-fg-main);
                width: 90%;
                max-width: 1200px;
                height: 70vh;
                position: relative;
                display: grid;
                grid-template-columns: 1fr 1fr;
            }

            .modal-left {
                padding: var(--spacing-xxl);
                display: flex;
                flex-direction: column;
            }

            .modal-right {
                padding: var(--spacing-xxl);
                display: flex;
                flex-direction: column;
                gap: var(--spacing-lg);
            }

            .modal-header {
                margin-bottom: var(--spacing-lg);
            }

            .modal-title {
                font-size: 1.1rem;
                margin: 0;
                text-transform: uppercase;
                font-weight: 400;
            }

            .modal-type {
                opacity: 0.5;
                font-size: 0.8rem;
                margin-top: var(--spacing-xs);
                font-weight: 400;
            }

            .close {
                position: absolute;
                right: var(--spacing-lg);
                top: var(--spacing-lg);
                font-size: 1.2rem;
                cursor: pointer;
                line-height: 1;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .close:hover {
                opacity: 0.7;
            }

            .modal-image {
                aspect-ratio: 4 / 3;
                width: 100%;
                border: 1px solid var(--color-fg-main);
                background: #f5f5f5;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 6rem;
                color: var(--color-fg-main);
                opacity: 0.3;
                flex-grow: 1;
            }

            .modal-overview {
                font-size: 0.8rem;
                line-height: 1.4;
                opacity: 0.7;
                margin-top: var(--spacing-md);
                font-weight: 400;
            }

            .modal-section {
                margin-bottom: var(--spacing-md);
            }

            .modal-section h3 {
                font-size: 0.8rem;
                text-transform: uppercase;
                margin-bottom: var(--spacing-sm);
                color: var(--color-fg-main);
                font-weight: 400;
                letter-spacing: 0.1em;
            }

            .modal-section p {
                font-size: 0.8rem;
                line-height: 1.4;
                margin: 0;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .tech-list {
                display: flex;
                flex-wrap: wrap;
                gap: var(--spacing-sm);
            }

            .tech-tag {
                font-size: 0.75rem;
                color: var(--color-fg-main);
                font-weight: 400;
            }

            .tech-tag:not(:last-child)::after {
                content: "•";
                margin-left: var(--spacing-sm);
                opacity: 0.5;
            }

            .feature-list {
                list-style: none;
                padding: 0;
                margin: 0;
                font-size: 0.75rem;
            }

            .feature-list li {
                padding: 0.15rem 0;
                color: var(--color-fg-main);
                line-height: 1.4;
                font-weight: 400;
            }

            /* Mobile responsive for modal */
            @media (max-width: 768px) {
                .modal-content {
                    grid-template-columns: 1fr;
                    width: 95%;
                    height: 85vh;
                }

                .modal-left {
                    padding: var(--spacing-lg);
                }

                .modal-right {
                    padding: var(--spacing-lg);
                    gap: var(--spacing-md);
                }

                .modal-image {
                    aspect-ratio: 3 / 2;
                    font-size: 4rem;
                }
            }
            
            /* Developer Story Timeline - Minimal inspired by Thea */
            .developer-story-section {
                margin: 4.5rem auto;
            }

            .developer-story-section h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin: var(--spacing-md) auto;
            }

            .timeline-wrapper {
                position: relative;
                margin-top: var(--spacing-xxl);
            }

            .timeline-wrapper::before {
                content: '';
                position: absolute;
                left: 1rem;
                top: 0;
                bottom: 0;
                width: 1px;
                background: var(--color-fg-main);
                opacity: 0.2;
            }

            .timeline-item {
                position: relative;
                margin-bottom: var(--spacing-xxl);
                padding-left: var(--spacing-xl);
            }

            .timeline-marker {
                position: absolute;
                left: 0.75rem;
                top: 0.5rem;
                width: 0.5rem;
                height: 0.5rem;
                background: var(--color-fg-main);
                border-radius: 50%;
                z-index: 1;
            }

            .timeline-content {
                max-width: 512px;
            }

            .timeline-header {
                display: flex;
                align-items: center;
                gap: var(--spacing-sm);
                margin-bottom: var(--spacing-sm);
            }

            .timeline-date {
                font-size: 0.875rem;
                opacity: 0.6;
            }

            .timeline-type {
                font-size: 0.75rem;
                text-transform: uppercase;
                padding: 0.15rem 0.5rem;
                border: 1px solid var(--color-fg-main);
                opacity: 0.7;
            }

            .timeline-type.education {
                border-color: #0E4DA4;
                color: #0E4DA4;
            }

            .timeline-type.volunteer {
                border-color: #CE2B30;
                color: #CE2B30;
            }

            .timeline-type.work {
                border-color: #4C4C39;
                color: #4C4C39;
            }

            .timeline-type.app {
                border-color: #204B8D;
                color: #204B8D;
            }

            .timeline-content h3 {
                font-size: 1rem;
                font-weight: 400;
                text-transform: uppercase;
                margin: 0 0 var(--spacing-xs) 0;
            }

            .timeline-company {
                font-size: 0.875rem;
                opacity: 0.8;
                margin-bottom: var(--spacing-sm);
            }

            .timeline-content p {
                font-size: 0.875rem;
                line-height: 1.4;
                opacity: 0.7;
                margin: 0 0 var(--spacing-sm) 0;
            }

            .logo-placeholder {
                position: absolute;
                right: 0;
                top: 0;
                font-size: 1.5rem;
                opacity: 0.3;
            }

            /* EXACT Long Nguyen Statement Section */
            .statement-section {
                margin: 4.5rem auto;
            }
            
            .statement-section .text-lg {
                font-size: 2.5rem;
            }
            
            .statement-section a {
                text-decoration: underline;
            }

            /* EXACT Long Nguyen Footer */
            footer {
                flex-shrink: 0;
            }

            .footer-links h2 {
                font-weight: 400;
                font-size: 1rem;
                text-transform: uppercase;
                margin-bottom: var(--spacing-sm);
            }

            .footer-links ul {
                margin: 0;
                margin-top: var(--spacing-sm);
                margin-bottom: var(--spacing-xl);
                padding: 0;
            }

            .footer-links li {
                list-style: none;
                font-size: 3rem;
                margin: var(--spacing-sm) auto;
            }

            footer small {
                opacity: .5;
                font-size: 1rem;
            }

            /* EXACT Long Nguyen Mobile Responsive */
            @media screen and (max-device-width: 480px) {
                body {
                    -webkit-text-size-adjust: 100%;
                }
            }

            @media screen and (min-width: 768px) {
                .vertical {
                    --spacing-vertical: var(--spacing-lg);
                }

                .horizontal {
                    --spacing-horizontal: 6rem;
                }

                header {
                    order: 0;
                    bottom: unset;
                    top: 0;
                }

                .intro-container ul {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    grid-auto-rows: auto;
                }

                .intro-container .wrapper {
                    margin-top: 8rem;
                    margin-bottom: 10rem;
                }

                .works-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    column-gap: var(--spacing-xl);
                }

                .project-card {
                    max-width: 512px;
                }

                .statement-section {
                    margin-top: 8.5rem;
                }

                .statement-container {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    grid-template-rows: auto;
                    column-gap: var(--spacing-xxl);
                }

                .statement-sub p {
                    margin-top: 0;
                }

                .statement-highlight {
                    grid-area: 1 / 1 / 2 / 2;
                }

                .statement-sub {
                    grid-area: 1 / 2 / 2 / 3;
                    margin-bottom: var(--spacing-xxl);
                }

                .footer-links {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    column-gap: var(--spacing-xxl);
                }

                .footer-links li {
                    font-size: unset;
                }

                /* Timeline responsive */
                .timeline-wrapper::before {
                    left: 1rem;
                }

                .timeline-item {
                    padding-left: var(--spacing-xl);
                }

                .timeline-marker {
                    left: 0.75rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="container margin vertical flex flex-columns flex-nowrap">
            <!-- Header - EXACT Long Nguyen structure -->
            <header>
                <div class="container padding horizontal">
                    <div class="block">
                        <nav>
                            <div class="container-actions">
                                <h2><a href="/">Michael Xie</a></h2>
                                <div class="links-container">
                                    <ul class="links-list">
                                        <li><a href="#projects">Projects</a></li>
                                        <li><a href="#story">Story</a></li>
                                        <li><a href="#contact">Contact</a></li>
                                    </ul>
                                </div>
                            </div>
                        </nav>
                    </div>
                </div>
            </header>

            <!-- Main Content Container -->
            <div class="container margin horizontal flex flex-columns flex-grow">
                <main class="flex-grow">
                    <div class="block">
                        <!-- Intro Section - EXACT structure -->
                        <div class="block">
                            <div class="intro-container">
                                <p>Hello!<br>I'm Michael, a software engineer. I build scalable data systems and cloud infrastructure with modern technologies.</p>
                                <ul>
                                    <li><a href="/Xie_Data_Resume.pdf">Resume</a></li>
                                    <li><a href="mailto:xie.michael@icloud.com">xie.michael@icloud.com</a></li>
                                </ul>
                            </div>
                        </div>

                        <!-- Selected Works Section - EXACT structure -->
                        <section id="projects" class="block works-section">
                            <div class="wrapper">
                                <h2>Selected <br> Works ↘</h2>
                                <div class="works-grid">
                                    <div class="project-card" onclick="openModal('homelab')">
                                        <h3>Personal HomeLab • <br><span class="fade">Infrastructure & DevOps</span></h3>
                                        <div class="project-placeholder">🏠</div>
                                        <p>Self-hosted Linux server infrastructure serving custom applications and services for home automation and productivity.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('real-estate')">
                                        <h3>Real Estate Analytics • <br><span class="fade">Data Engineering & Visualization</span></h3>
                                        <div class="project-placeholder">📊</div>
                                        <p>Automated Chicago real estate and rental market data scraping with comprehensive Grafana visualization dashboards.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('ai-ml')">
                                        <h3>AI/ML Playground • <br><span class="fade">Artificial Intelligence</span></h3>
                                        <div class="project-placeholder">🤖</div>
                                        <p>Self-hosted AI infrastructure featuring Stable Diffusion image generation and Ollama language models for experimentation.</p>
                                    </div>

                                    <div class="project-card" onclick="openModal('smart-home')">
                                        <h3>Smart Home IoT • <br><span class="fade">IoT & Home Automation</span></h3>
                                        <div class="project-placeholder">🏡</div>
                                        <p>Comprehensive sensor network with BME688, LD2450, and custom IoT devices integrated with Home Assistant automation.</p>
                                    </div>
                                </div>
                                
                                <!-- See All Projects Link -->
                                <div class="see-all-container">
                                    <a href="/projects" class="see-all-link">see all projects ↘</a>
                                </div>
                            </div>
                        </section>

                        <!-- Developer Story Section - Inspired by Thea -->
                        <section id="story" class="block developer-story-section">
                            <div class="wrapper">
                                <h2>Developer <br> Story ↘</h2>
                                <div class="timeline-wrapper">
                                    <div class="timeline-item">
                                        <div class="timeline-marker"></div>
                                        <div class="timeline-content">
                                            <div class="timeline-header">
                                                <div class="timeline-date">Nov 2019 - Sep 2023</div>
                                                <div class="timeline-type education">education</div>
                                            </div>
                                            <h3>Computer Science</h3>
                                            <div class="timeline-company">Cambodia Academy of Digital Technology - CADT</div>
                                            <p>My journey began here as a Computer Science student. Foundation in algorithms, data structures, and software engineering principles.</p>
                                            <!-- Logo placeholder: Add CADT logo here -->
                                            <div class="logo-placeholder">📚</div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-marker"></div>
                                        <div class="timeline-content">
                                            <div class="timeline-header">
                                                <div class="timeline-date">Jan 2020 - Jun 2023</div>
                                                <div class="timeline-type volunteer">volunteer</div>
                                            </div>
                                            <h3>Mobile Team Leader</h3>
                                            <div class="timeline-company">E-Robot</div>
                                            <p>Led mobile development team building educational robotics applications. Transitioned from visual programming to Flutter development.</p>
                                            <!-- Logo placeholder: Add E-Robot logo here -->
                                            <div class="logo-placeholder">🤖</div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-marker"></div>
                                        <div class="timeline-content">
                                            <div class="timeline-header">
                                                <div class="timeline-date">Nov 2020 - Jan 2023</div>
                                                <div class="timeline-type work">work</div>
                                            </div>
                                            <h3>Software Developer</h3>
                                            <div class="timeline-company">VTENH - Part Time</div>
                                            <p>Developed full-stack ecommerce solutions with Flutter and Ruby on Rails. Gained hands-on experience in scalable web applications.</p>
                                            <!-- Logo placeholder: Add VTENH logo here -->
                                            <div class="logo-placeholder">🛒</div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-marker"></div>
                                        <div class="timeline-content">
                                            <div class="timeline-header">
                                                <div class="timeline-date">Mar 2021 - Present</div>
                                                <div class="timeline-type app">side project</div>
                                            </div>
                                            <h3>Creator & Developer</h3>
                                            <div class="timeline-company">StoryPad Mobile App</div>
                                            <p>Designed and built a story writing app from scratch. Achieved 80,000+ downloads and learned product development end-to-end.</p>
                                            <!-- Logo placeholder: Add StoryPad logo here -->
                                            <div class="logo-placeholder">📱</div>
                                        </div>
                                    </div>

                                    <div class="timeline-item">
                                        <div class="timeline-marker"></div>
                                        <div class="timeline-content">
                                            <div class="timeline-header">
                                                <div class="timeline-date">Jan 2023 - Present</div>
                                                <div class="timeline-type work">work</div>
                                            </div>
                                            <h3>Tech Lead</h3>
                                            <div class="timeline-company">BookMeBus</div>
                                            <p>Leading development of scalable booking platform (BookMe+). Managing technical architecture and mentoring development team.</p>
                                            <!-- Logo placeholder: Add BookMeBus logo here -->
                                            <div class="logo-placeholder">🚌</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Statement Section - Long Nguyen approach -->
                        <section class="block statement-section">
                            <div class="statement-container">
                                <p class="statement-highlight text-lg">
                                    Software engineering with purpose. I build scalable systems that solve real problems
                                    and create value through thoughtful architecture and clean code.
                                </p>
                                <div class="statement-sub">
                                    <p>
                                        With 5+ years of experience in fintech and enterprise systems, I specialize in
                                        big data ETL pipelines, cloud infrastructure, and modern software development practices.
                                    </p>
                                    <div>
                                        <a href="#about">More About Me ↘</a>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </div>
                </main>

                <!-- Footer - EXACT Long Nguyen structure -->
                <footer class="block">
                    <div class="container">
                        <section class="footer-links">
                            <div>
                                <h2>Links ↘</h2>
                                <ul>
                                    <li><a href="#about">About Me</a></li>
                                    <li><a href="/resume.pdf">Resume</a></li>
                                </ul>
                            </div>
                            <div>
                                <h2>Socials ↘</h2>
                                <ul>
                                    <li><a href="https://github.com/yourusername">Github</a></li>
                                    <li><a href="https://linkedin.com/in/yourusername">LinkedIn</a></li>
                                </ul>
                            </div>
                        </section>
                                                     <small>© 2024 Michael Xie. All rights reserved.</small>
                    </div>
                </footer>
            </div>
        </div>

        <!-- Project Modal -->
        <div id="projectModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal()">&times;</span>
                
                <!-- Left side: Image and title -->
                <div class="modal-left">
                    <div class="modal-header">
                        <h2 id="modalTitle" class="modal-title"></h2>
                        <div id="modalType" class="modal-type"></div>
                    </div>
                    <div id="modalImage" class="modal-image"></div>
                    <p id="modalOverview" class="modal-overview"></p>
                </div>
                
                <!-- Right side: Details -->
                <div class="modal-right">
                    <div class="modal-section">
                        <h3>Tech Stack</h3>
                        <div id="modalTechStack" class="tech-list"></div>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Features</h3>
                        <ul id="modalFeatures" class="feature-list"></ul>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Challenge</h3>
                        <p id="modalChallenges"></p>
                    </div>
                    
                    <div class="modal-section">
                        <h3>Impact</h3>
                        <p id="modalImpact"></p>
                    </div>
                </div>
            </div>
        </div>

        <script>
            // Project data for modal
            const projects = {
                'homelab': {
                    title: 'Personal HomeLab',
                    type: 'Infrastructure & DevOps',
                    placeholder: '🏠',
                    overview: 'A comprehensive home server setup running on Linux, providing self-hosted alternatives to cloud services while maintaining full control over data and functionality.',
                    tech_stack: ['Linux Server', 'Docker', 'Nginx', 'PostgreSQL', 'Redis', 'Monitoring Stack'],
                    features: [
                        'Media streaming and management',
                        'Network-attached storage (NAS)',
                        'VPN server for secure remote access',
                        'Automated backup systems',
                        'Custom web applications',
                        'Home automation integrations'
                    ],
                    challenges: 'Designing a robust, scalable infrastructure that balances performance, security, and maintainability while keeping costs low.',
                    impact: 'Reduced dependency on cloud services, improved privacy, and created a testing environment for new technologies.'
                },
                'real-estate': {
                    title: 'Real Estate Analytics',
                    type: 'Data Engineering & Visualization',
                    placeholder: '📊',
                    overview: 'A data pipeline that automatically collects, processes, and visualizes Chicago real estate and rental market trends to provide actionable insights.',
                    tech_stack: ['Python', 'Beautiful Soup', 'Selenium', 'PostgreSQL', 'Grafana', 'Docker', 'Cron Jobs'],
                    features: [
                        'Multi-source data scraping (Zillow, Apartments.com, etc.)',
                        'Real-time market trend analysis',
                        'Price prediction modeling',
                        'Neighborhood comparison tools',
                        'Automated alert systems',
                        'Historical data tracking'
                    ],
                    challenges: 'Handling anti-scraping measures, data normalization across different sources, and creating meaningful visualizations.',
                    impact: 'Enabled data-driven real estate decisions and provided insights into Chicago market patterns.'
                },
                'ai-ml': {
                    title: 'AI/ML Playground',
                    type: 'Artificial Intelligence',
                    placeholder: '🤖',
                    overview: 'A local AI development environment for experimenting with cutting-edge machine learning models while maintaining privacy and control.',
                    tech_stack: ['Stable Diffusion', 'Ollama', 'Python', 'PyTorch', 'CUDA', 'FastAPI', 'Docker'],
                    features: [
                        'Local Stable Diffusion image generation',
                        'Multiple LLM model hosting with Ollama',
                        'Custom model fine-tuning pipeline',
                        'API endpoints for integration',
                        'Prompt engineering tools',
                        'Model performance monitoring'
                    ],
                    challenges: 'Optimizing model performance on consumer hardware, managing GPU memory efficiently, and creating intuitive interfaces.',
                    impact: 'Accelerated AI/ML learning and provided a foundation for integrating AI into other projects.'
                },
                'smart-home': {
                    title: 'Smart Home IoT',
                    type: 'IoT & Home Automation',
                    placeholder: '🏡',
                    overview: 'An intelligent home automation system using various sensors and custom IoT devices to create a responsive living environment.',
                    tech_stack: ['Home Assistant', 'ESPHome', 'MQTT', 'BME688 Sensors', 'LD2450 Radar', 'Arduino', 'Zigbee'],
                    features: [
                        'Environmental monitoring (temperature, humidity, air quality)',
                        'Human presence detection with millimeter-wave radar',
                        'Automated lighting and climate control',
                        'Energy consumption tracking',
                        'Security system integration',
                        'Voice control and mobile app access'
                    ],
                    challenges: 'Ensuring reliable wireless communication, balancing automation with manual control, and maintaining system stability.',
                    impact: 'Improved energy efficiency, enhanced security, and created a more comfortable living environment.'
                }
            };

            function openModal(projectId) {
                const project = projects[projectId];
                if (!project) return;

                // Populate modal content
                document.getElementById('modalTitle').textContent = project.title;
                document.getElementById('modalType').textContent = project.type;
                document.getElementById('modalImage').textContent = project.placeholder;
                document.getElementById('modalOverview').textContent = project.overview;
                document.getElementById('modalChallenges').textContent = project.challenges;
                document.getElementById('modalImpact').textContent = project.impact;

                // Tech stack
                const techStackContainer = document.getElementById('modalTechStack');
                techStackContainer.innerHTML = '';
                project.tech_stack.forEach(tech => {
                    const tag = document.createElement('span');
                    tag.className = 'tech-tag';
                    tag.textContent = tech;
                    techStackContainer.appendChild(tag);
                });

                // Features
                const featuresContainer = document.getElementById('modalFeatures');
                featuresContainer.innerHTML = '';
                project.features.forEach(feature => {
                    const li = document.createElement('li');
                    li.textContent = feature;
                    featuresContainer.appendChild(li);
                });

                // Show modal
                const modal = document.getElementById('projectModal');
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
            }

            function closeModal() {
                const modal = document.getElementById('projectModal');
                modal.classList.remove('show');
                document.body.style.overflow = 'auto';
            }

            // Close modal when clicking outside
            window.onclick = function(event) {
                const modal = document.getElementById('projectModal');
                if (event.target === modal) {
                    closeModal();
                }
            }

            // Make sure modal closes properly
            document.addEventListener('DOMContentLoaded', function() {
                const modal = document.getElementById('projectModal');
                if (modal) {
                    modal.classList.remove('show');
                }
            });

            // Close modal with Escape key
            document.addEventListener('keydown', function(event) {
                if (event.key === 'Escape') {
                    closeModal();
                }
            });
        </script>
    </body>
    </html>
    """
    
    @app.route('/')
    def home():
        return render_template_string(home_template)
    
    @app.route('/Xie_Data_Resume.pdf')
    def resume():
        from flask import send_file
        return send_file('Xie_Data_Resume.pdf', as_attachment=False)
    
    @app.route('/projects')
    def all_projects():
        # Projects page template with extended grid
        projects_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                         <title>All Projects - Michael Xie</title>
            <style>
                /* Include all the same styles as main page */
                """ + home_template.split('<style>')[1].split('</style>')[0] + """
                
                /* Projects page specific styles */
                .projects-page {
                    min-height: 100vh;
                }
                
                .projects-header {
                    margin: var(--spacing-xxl) 0;
                }
                
                .projects-header h1 {
                    font-size: 1.5rem;
                    margin-bottom: var(--spacing-md);
                    text-transform: uppercase;
                }
                
                .back-link {
                    display: inline-block;
                    margin-bottom: var(--spacing-lg);
                    color: var(--color-fg-main);
                    text-decoration: none;
                    font-size: 0.875rem;
                    opacity: 0.6;
                    transition: opacity 0.3s ease;
                }
                
                .back-link:hover {
                    opacity: 1;
                    text-decoration: underline;
                }
                
                .extended-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    column-gap: var(--spacing-xl);
                    row-gap: var(--spacing-xxl);
                }
                
                @media (max-width: 767px) {
                    .extended-grid {
                        grid-template-columns: 1fr;
                        gap: var(--spacing-xl);
                    }
                }
            </style>
        </head>
        <body>
            <div class="container margin vertical flex flex-columns flex-nowrap projects-page">
                <!-- Header - Same as main page -->
                <header>
                    <div class="container padding horizontal">
                        <div class="block">
                            <nav>
                                <div class="container-actions">
                                    <h2><a href="/">Michael Xie</a></h2>
                                    <div class="links-container">
                                        <ul class="links-list">
                                            <li><a href="#about">About</a></li>
                                            <li><a href="#contact">Contact</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </nav>
                        </div>
                    </div>
                </header>

                <!-- Main Content -->
                <div class="container margin horizontal flex flex-columns flex-grow">
                    <main class="flex-grow">
                                                 <div class="block">
                             <div class="projects-header">
                                 <a href="/" class="back-link">← back to home</a>
                                 <h1>All Projects</h1>
                                 <p style="opacity: 0.7; font-size: 0.875rem;">Technical projects and experiments.</p>
                             </div>
                            
                            <div class="extended-grid">
                                <div class="project-card" onclick="openModal('homelab')">
                                    <h3>Personal HomeLab • <br><span class="fade">Infrastructure & DevOps</span></h3>
                                    <div class="project-placeholder">🏠</div>
                                    <p>Self-hosted Linux server infrastructure serving custom applications and services for home automation and productivity.</p>
                                </div>

                                <div class="project-card" onclick="openModal('real-estate')">
                                    <h3>Real Estate Analytics • <br><span class="fade">Data Engineering & Visualization</span></h3>
                                    <div class="project-placeholder">📊</div>
                                    <p>Automated Chicago real estate and rental market data scraping with comprehensive Grafana visualization dashboards.</p>
                                </div>

                                <div class="project-card" onclick="openModal('ai-ml')">
                                    <h3>AI/ML Playground • <br><span class="fade">Artificial Intelligence</span></h3>
                                    <div class="project-placeholder">🤖</div>
                                    <p>Self-hosted AI infrastructure featuring Stable Diffusion image generation and Ollama language models for experimentation.</p>
                                </div>

                                <div class="project-card" onclick="openModal('smart-home')">
                                    <h3>Smart Home IoT • <br><span class="fade">IoT & Home Automation</span></h3>
                                    <div class="project-placeholder">🏡</div>
                                    <p>Comprehensive sensor network with BME688, LD2450, and custom IoT devices integrated with Home Assistant automation.</p>
                                </div>
                                
                                <!-- Placeholder for future projects -->
                                <div class="project-card" style="opacity: 0.5; cursor: default;">
                                    <h3>Coming Soon • <br><span class="fade">Future Project</span></h3>
                                    <div class="project-placeholder">🔮</div>
                                    <p>More exciting projects are in development. Stay tuned for updates!</p>
                                </div>
                                
                                <div class="project-card" style="opacity: 0.5; cursor: default;">
                                    <h3>Coming Soon • <br><span class="fade">Future Project</span></h3>
                                    <div class="project-placeholder">⚡</div>
                                    <p>Additional technical experiments and innovations coming soon.</p>
                                </div>
                            </div>
                        </div>
                    </main>

                    <!-- Footer - Same as main page -->
                    <footer class="block">
                        <div class="container">
                            <section class="footer-links">
                                <div>
                                    <h2>Links ↘</h2>
                                    <ul>
                                        <li><a href="#about">About Me</a></li>
                                        <li><a href="/resume.pdf">Resume</a></li>
                                    </ul>
                                </div>
                                <div>
                                    <h2>Socials ↘</h2>
                                    <ul>
                                        <li><a href="https://github.com/xie-git">Github</a></li>
                                        <li><a href="https://linkedin.com/in/xie-michael">LinkedIn</a></li>
                                    </ul>
                                </div>
                            </section>
                            <small>© 2024 Michael Xie. All rights reserved.</small>
                        </div>
                    </footer>
                </div>
            </div>

            <!-- Same modal as main page -->
            """ + home_template.split('<!-- Project Modal -->')[1].split('</script>')[0] + """</script>
        </body>
        </html>
        """
        return render_template_string(projects_template)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        error_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>404 - Page Not Found | Michael Xie</title>
            <style>
                """ + home_template.split('<style>')[1].split('</style>')[0] + """
                .error-container {
                    min-height: 80vh;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                }
                .error-code {
                    font-size: 8rem;
                    font-weight: 400;
                    opacity: 0.3;
                    margin-bottom: var(--spacing-lg);
                }
                .error-message {
                    font-size: 1.5rem;
                    margin-bottom: var(--spacing-lg);
                }
                .error-description {
                    opacity: 0.7;
                    margin-bottom: var(--spacing-xl);
                }
                .home-link {
                    color: var(--color-fg-main);
                    text-decoration: none;
                    border-bottom: 1px solid var(--color-fg-main);
                    padding-bottom: 2px;
                }
                .home-link:hover {
                    opacity: 0.7;
                }
            </style>
        </head>
        <body>
            <div class="container margin vertical flex flex-columns flex-nowrap">
                <header>
                    <div class="container padding horizontal">
                        <div class="block">
                            <nav>
                                <div class="container-actions">
                                    <h2><a href="/">Michael Xie</a></h2>
                                    <div class="links-container">
                                        <ul class="links-list">
                                            <li><a href="/">Home</a></li>
                                            <li><a href="/projects">Projects</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </nav>
                        </div>
                    </div>
                </header>
                
                <div class="container margin horizontal flex flex-columns flex-grow">
                    <main class="flex-grow">
                        <div class="error-container">
                            <div class="error-code">404</div>
                            <h1 class="error-message">Page Not Found</h1>
                            <p class="error-description">The page you're looking for doesn't exist.</p>
                            <a href="/" class="home-link">← Back to Home</a>
                        </div>
                    </main>
                </div>
            </div>
        </body>
        </html>
        """
        return render_template_string(error_template), 404
    
    @app.errorhandler(500)
    def server_error(error):
        error_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>500 - Server Error | Michael Xie</title>
            <style>
                """ + home_template.split('<style>')[1].split('</style>')[0] + """
                .error-container {
                    min-height: 80vh;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    text-align: center;
                }
                .error-code {
                    font-size: 8rem;
                    font-weight: 400;
                    opacity: 0.3;
                    margin-bottom: var(--spacing-lg);
                }
                .error-message {
                    font-size: 1.5rem;
                    margin-bottom: var(--spacing-lg);
                }
                .error-description {
                    opacity: 0.7;
                    margin-bottom: var(--spacing-xl);
                }
                .home-link {
                    color: var(--color-fg-main);
                    text-decoration: none;
                    border-bottom: 1px solid var(--color-fg-main);
                    padding-bottom: 2px;
                }
                .home-link:hover {
                    opacity: 0.7;
                }
            </style>
        </head>
        <body>
            <div class="container margin vertical flex flex-columns flex-nowrap">
                <header>
                    <div class="container padding horizontal">
                        <div class="block">
                            <nav>
                                <div class="container-actions">
                                    <h2><a href="/">Michael Xie</a></h2>
                                    <div class="links-container">
                                        <ul class="links-list">
                                            <li><a href="/">Home</a></li>
                                            <li><a href="/projects">Projects</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </nav>
                        </div>
                    </div>
                </header>
                
                <div class="container margin horizontal flex flex-columns flex-grow">
                    <main class="flex-grow">
                        <div class="error-container">
                            <div class="error-code">500</div>
                            <h1 class="error-message">Server Error</h1>
                            <p class="error-description">Something went wrong on our end. Please try again later.</p>
                            <a href="/" class="home-link">← Back to Home</a>
                        </div>
                    </main>
                </div>
            </div>
        </body>
        </html>
        """
        return render_template_string(error_template), 500
    
    # Favicon route
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(app.static_folder or 'static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
    # Use environment variables for configuration
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5005))
    
    # Run the development server
    print("🚀 Starting Portfolio Website...")
    print(f"💻 Visit: http://localhost:{port}")
    print("⚡ Press Ctrl+C to stop the server")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
    
    return app  # Return app for WSGI servers

# WSGI application for production servers (Gunicorn, etc.)
app = None

def create_app():
    """Application factory for WSGI servers."""
    from flask import Flask, render_template_string, jsonify, send_from_directory
    import os
    
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Import all the routes and config from run_simple_app
    # This is a bit hacky but works for our single-file approach
    return run_simple_app()

# For WSGI servers (gunicorn, etc.)
try:
    app = create_app()
except:
    app = None

if __name__ == '__main__':
    setup_and_run() 