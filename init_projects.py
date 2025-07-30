#!/usr/bin/env python3
"""
Initialize the database with existing project data
"""

from app import create_app, db, Project, Bio, TimelineItem
import json

# Create the app and context
app = create_app()

# Default project data
default_projects = [
    {
        'project_id': 'homelab',
        'title': 'HomeLab & Smart-Condo Automation Platform',
        'type': 'Infrastructure & DevOps',
        'image': '/static/images/projects/homelab_image.png',
        'overview': 'Built a fully containerized, self-hosted environment that powers home automation, real-time analytics, media streaming, and on-device AI while serving as a playground for DevOps experimentation.',
        'tech_stack': ['Docker Compose', 'Ubuntu 24.04 LTS', 'Proxmox', 'Tailscale VPN', 'Home Assistant', 'InfluxDB', 'Grafana', 'Prometheus', 'Ollama LLM', 'Nextcloud', 'Plex'],
        'features': [
            'Real-time environmental dashboard with sub-5s refresh',
            'Self-hosted cloud suite replacing iCloud/Google Drive',
            'Housing-market microservice with ML price-anomaly alerts',
            'Media & gaming hub streaming 4K HDR video',
            'Automated resilience with health-checks and failover'
        ],
        'challenges': 'Unified heterogeneous hardware under single monitoring plane, tuned InfluxDB retention for 500ms refresh without data loss, hardened remote access eliminating exposed public ports.',
        'impact': '99.9% service uptime over 12 months, reduced cloud-storage spend by $240/yr, improved HVAC efficiency by 8%, delivered reusable DevOps sandbox cutting work project iteration time by 40%.',
        'description': 'Containerized environment powering home automation, analytics, and AI.',
        'order_index': 1
    },
    {
        'project_id': 'real-estate',
        'title': 'Chicago Rental Analytics & Visualization Pipeline',
        'type': 'Data Engineering & Visualization',
        'image': '/static/images/projects/chicago_analytics_map.png',
        'overview': 'Designed, built, and production-hardened a fully automated data platform that scrapes, cleans, enriches, and visualizes 75k+ Chicago apartment records, delivering investment-grade insights via ML models and Grafana dashboards.',
        'tech_stack': ['Python 3.11', 'Docker Compose', 'PostgreSQL 14', 'Redis', 'scikit-learn', 'FastAPI', 'Folium', 'InfluxDB', 'Grafana', 'BeautifulSoup4'],
        'features': [
            'Automated weekly pipeline processing 4,500 URLs in ~6h',
            'Random-Forest price prediction model (R² = 0.995, RMSE ≈ $50)',
            'Building-level insights with investment scores and risk metrics',
            'Interactive Folium-powered clustering map with live queries',
            'Six Grafana dashboards with sub-5s refresh',
            'One-command DevOps deployment with 100% E2E test coverage'
        ],
        'challenges': 'Implemented Redis task queue for 5 parallel scrapers cutting collection time 40%, built ID-fuzzing logic achieving 85%+ data quality, added model drift detection with automated retraining.',
        'impact': '75k+ property rows processed, 600 building insights generated, >99% weekly pipeline success rate over 6 months, enables neighborhood price comps and yield forecasts for investors.',
        'description': 'Automated platform processing 75k+ records with ML insights.',
        'order_index': 2
    },
    {
        'project_id': 'ai-ml',
        'title': 'AI/ML Playground',
        'type': 'Artificial Intelligence',
        'image': '/static/images/projects/aigeneratedai.png',
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
        'impact': 'Accelerated AI/ML learning and provided a foundation for integrating AI into other projects.',
        'description': 'Self-hosted infrastructure with Stable Diffusion and LLM models.',
        'order_index': 3
    },
    {
        'project_id': 'smart-home',
        'title': 'Smart-Home & IoT Ecosystem',
        'type': 'IoT & Home Automation',
        'image': '/static/images/projects/homeassistant.png',
        'overview': 'Architected and maintain a tightly-integrated suite of DIY smart-home solutions built on open-source software and low-cost microcontrollers to drive comfort, security, and data-driven energy efficiency across 1,250 sq ft condo.',
        'tech_stack': ['10× ESP32-WROOM-32', 'BME688 sensors', 'LD2450 mm-wave radars', 'ESPHome 2023.12', 'Home Assistant', 'Mosquitto MQTT', 'InfluxDB 2', 'Grafana', 'Tailscale VPN', 'Pi-hole DNS'],
        'features': [
            'Sensor mesh coverage across 6 zones with real-time heat-maps',
            'Adaptive HVAC & blinds balancing IAQ and comfort automatically',
            'Presence-aware lighting with <100ms response via LD2450 radar',
            'Energy & network dashboards with Slack anomaly alerting',
            'Voice-first control via Mycroft AI (completely offline)',
            'Whole-home ad-blocking via Pi-hole reducing WAN data 25%'
        ],
        'challenges': 'Achieved low-latency telemetry without Wi-Fi saturation via tuned ESP32 QoS, calibrated sensor accuracy in mixed HVAC airflow, secured remote access migrating from port-forwards to Tailscale mesh.',
        'impact': 'Maintained temp ±1°C and humidity 40-55% year-round, achieved 99.9% service uptime, collected 2M+ time-series points, cut annual energy use 8%, provided DevOps sandbox shortening POC cycles 40%.',
        'description': 'Comprehensive sensor network with BME688, LD2450, and custom IoT devices integrated with Home Assistant automation.',
        'order_index': 4
    }
]

# Default bio data
default_bio = {
    'title': 'Senior Software Engineer',
    'description': 'Senior Software Engineer based in Chicago, IL with extensive experience delivering scalable, enterprise-grade systems for leading financial institutions.',
    'statement_highlight': 'Software Engineering. Data Engineering. API Development. Embedded Systems. Cloud & Infrastructure. Security & DevOps.',
    'statement_description': '6+ years specializing in Python, Java, ETL pipelines, AWS cloud infrastructure, on-premises systems, and enterprise-scale data platforms at Fortune 500 companies.',
    'is_active': True
}

# Default timeline data
default_timeline = [
    {
        'type': 'education',
        'title': 'Bachelor\'s Degree',
        'company': 'University of Wisconsin-Madison',
        'location': 'Madison, WI',
        'start_date': 'Aug 2014',
        'end_date': 'May 2018',
        'description': 'Bachelor\'s degree focused on financial statistics, econometrics, and computational methods for large-scale data analysis.',
        'logo_image': '/static/images/companies/uw_small.png',
        'order_index': 1,
        'is_active': True
    },
    {
        'type': 'work',
        'title': 'Operations Lead',
        'company': 'Northwestern Mutual',
        'location': 'Milwaukee, WI',
        'start_date': 'Jun 2018',
        'end_date': 'Aug 2019',
        'description': 'Managed enterprise iOS/Android app deployment using Microsoft Intune and Azure AD.',
        'logo_image': '/static/images/companies/northwestern_mutual_small.png',
        'order_index': 2,
        'is_active': True
    },
    {
        'type': 'work',
        'title': 'Software Engineer',
        'company': 'Capital One',
        'location': 'Chicago, IL',
        'start_date': 'Aug 2019',
        'end_date': 'Nov 2023',
        'description': 'Built scalable AWS ETL pipelines with Python/PySpark and fraud analytics systems using Java Spring Boot.',
        'logo_image': '/static/images/companies/capital_one_small.png',
        'order_index': 3,
        'is_active': True
    },
    {
        'type': 'work',
        'title': 'Software Engineer (IAM)',
        'company': 'Northern Trust',
        'location': 'Chicago, IL',
        'start_date': 'Mar 2025',
        'end_date': None,
        'description': 'Developing Python ETL pipelines for enterprise identity systems and automating legacy IAM data migration.',
        'logo_image': '/static/images/companies/northern_trust_small.png',
        'order_index': 4,
        'is_active': True
    }
]

def init_projects():
    with app.app_context():
        # Check if data already exists
        existing_projects = Project.query.count()
        existing_bio = Bio.query.count()
        existing_timeline = TimelineItem.query.count()
        
        if existing_projects > 0 and existing_bio > 0 and existing_timeline > 0:
            print(f"Database already initialized with {existing_projects} projects, {existing_bio} bio, {existing_timeline} timeline items.")
            return
        
        # Add default projects if not exist
        if existing_projects == 0:
            for proj_data in default_projects:
                project = Project(
                    project_id=proj_data['project_id'],
                    title=proj_data['title'],
                    type=proj_data['type'],
                    image=proj_data['image'],
                    overview=proj_data['overview'],
                    tech_stack=json.dumps(proj_data['tech_stack']),
                    features=json.dumps(proj_data['features']),
                    challenges=proj_data['challenges'],
                    impact=proj_data['impact'],
                    description=proj_data['description'],
                    order_index=proj_data['order_index'],
                    is_active=True
                )
                db.session.add(project)
            print(f"Added {len(default_projects)} projects.")
        
        # Add default bio if not exist
        if existing_bio == 0:
            bio = Bio(
                title=default_bio['title'],
                description=default_bio['description'],
                statement_highlight=default_bio['statement_highlight'],
                statement_description=default_bio['statement_description'],
                is_active=default_bio['is_active']
            )
            db.session.add(bio)
            print("Added bio content.")
        
        # Add default timeline items if not exist
        if existing_timeline == 0:
            for timeline_data in default_timeline:
                timeline_item = TimelineItem(
                    type=timeline_data['type'],
                    title=timeline_data['title'],
                    company=timeline_data['company'],
                    location=timeline_data['location'],
                    start_date=timeline_data['start_date'],
                    end_date=timeline_data['end_date'],
                    description=timeline_data['description'],
                    logo_image=timeline_data['logo_image'],
                    order_index=timeline_data['order_index'],
                    is_active=timeline_data['is_active']
                )
                db.session.add(timeline_item)
            print(f"Added {len(default_timeline)} timeline items.")
        
        db.session.commit()
        print("Successfully initialized all data.")

if __name__ == '__main__':
    init_projects()