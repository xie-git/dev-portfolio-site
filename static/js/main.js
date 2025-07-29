// ===== SIMPLIFIED MAIN JAVASCRIPT FILE =====
// Only includes functionality actually used by the Long Nguyen-inspired design

document.addEventListener('DOMContentLoaded', function() {
    initContactForm();
    initSmoothScrolling();
});

// ===== CONTACT FORM FUNCTIONALITY =====
function initContactForm() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        // Handle form submission for index.html contact form (mailto)
        contactForm.addEventListener('submit', function(e) {
            // Only prevent default for index.html contact form (mailto)
            if (contactForm.getAttribute('action') && contactForm.getAttribute('action').includes('mailto:')) {
                e.preventDefault();
                
                const name = document.getElementById('name').value;
                const email = document.getElementById('email').value;
                const message = document.getElementById('message').value;
                
                const subject = `Portfolio Contact from ${name}`;
                const mailtoLink = `mailto:xie.michael@icloud.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;
                
                window.location.href = mailtoLink;
            }
            // For contact.html, let the form submit normally to Flask backend
        });
        
        // Basic form validation
        const inputs = contactForm.querySelectorAll('input, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });

            input.addEventListener('input', function() {
                this.classList.remove('error');
            });
        });
    }
}

// ===== SMOOTH SCROLLING =====
function initSmoothScrolling() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===== BASIC FORM VALIDATION =====
function validateField(field) {
    const value = field.value.trim();
    const required = field.hasAttribute('required');
    let isValid = true;

    // Clear previous errors
    field.classList.remove('error');

    // Required field validation
    if (required && !value) {
        isValid = false;
        field.classList.add('error');
    }
    // Email validation
    else if (field.type === 'email' && value && !isValidEmail(value)) {
        isValid = false;
        field.classList.add('error');
    }

    return isValid;
}

// ===== UTILITY FUNCTIONS =====
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// ===== CONTACT FORM TOGGLE (for index.html) =====
function toggleContactForm() {
    const header = document.querySelector('.contact-header');
    const form = document.querySelector('.contact-form');
    const info = document.querySelector('.contact-info');
    
    if (header && form && info) {
        header.classList.toggle('expanded');
        form.classList.toggle('expanded');
        info.classList.toggle('expanded');
    }
}

function expandContactForm() {
    const header = document.querySelector('.contact-header');
    const form = document.querySelector('.contact-form');
    const info = document.querySelector('.contact-info');
    
    if (header && form && info) {
        // Add expanded class if not already expanded
        if (!form.classList.contains('expanded')) {
            header.classList.add('expanded');
            form.classList.add('expanded');
            info.classList.add('expanded');
        }
    }
}

// ===== PROJECT MODAL FUNCTIONALITY =====
// Project data for modal (used by index.html and projects.html)
const projects = {
    'homelab': {
        title: 'HomeLab & Smart-Condo Automation Platform',
        type: 'Infrastructure & DevOps',
        image: '/static/images/projects/homelab_image.png',
        overview: 'Built a fully containerized, self-hosted environment that powers home automation, real-time analytics, media streaming, and on-device AI while serving as a playground for DevOps experimentation.',
        tech_stack: ['Docker Compose', 'Ubuntu 24.04 LTS', 'Proxmox', 'Tailscale VPN', 'Home Assistant', 'InfluxDB', 'Grafana', 'Prometheus', 'Ollama LLM', 'Nextcloud', 'Plex'],
        features: [
            'Real-time environmental dashboard with sub-5s refresh',
            'Self-hosted cloud suite replacing iCloud/Google Drive',
            'Housing-market microservice with ML price-anomaly alerts',
            'Media & gaming hub streaming 4K HDR video',
            'Automated resilience with health-checks and failover'
        ],
        challenges: 'Unified heterogeneous hardware under single monitoring plane, tuned InfluxDB retention for 500ms refresh without data loss, hardened remote access eliminating exposed public ports.',
        impact: '99.9% service uptime over 12 months, reduced cloud-storage spend by $240/yr, improved HVAC efficiency by 8%, delivered reusable DevOps sandbox cutting work project iteration time by 40%.'
    },
    'real-estate': {
        title: 'Chicago Rental Analytics & Visualization Pipeline',
        type: 'Data Engineering & Visualization',
        image: '/static/images/projects/chicago_analytics_map.png',
        overview: 'Designed, built, and production-hardened a fully automated data platform that scrapes, cleans, enriches, and visualizes 75k+ Chicago apartment records, delivering investment-grade insights via ML models and Grafana dashboards.',
        tech_stack: ['Python 3.11', 'Docker Compose', 'PostgreSQL 14', 'Redis', 'scikit-learn', 'FastAPI', 'Folium', 'InfluxDB', 'Grafana', 'BeautifulSoup4'],
        features: [
            'Automated weekly pipeline processing 4,500 URLs in ~6h',
            'Random-Forest price prediction model (R² = 0.995, RMSE ≈ $50)',
            'Building-level insights with investment scores and risk metrics',
            'Interactive Folium-powered clustering map with live queries',
            'Six Grafana dashboards with sub-5s refresh',
            'One-command DevOps deployment with 100% E2E test coverage'
        ],
        challenges: 'Implemented Redis task queue for 5 parallel scrapers cutting collection time 40%, built ID-fuzzing logic achieving 85%+ data quality, added model drift detection with automated retraining.',
        impact: '75k+ property rows processed, 600 building insights generated, >99% weekly pipeline success rate over 6 months, enables neighborhood price comps and yield forecasts for investors.'
    },
    'ai-ml': {
        title: 'AI/ML Playground',
        type: 'Artificial Intelligence',
        image: '/static/images/projects/aigeneratedai.png',
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
        title: 'Smart-Home & IoT Ecosystem',
        type: 'IoT & Home Automation',
        image: '/static/images/projects/homeassistant.png',
        overview: 'Architected and maintain a tightly-integrated suite of DIY smart-home solutions built on open-source software and low-cost microcontrollers to drive comfort, security, and data-driven energy efficiency across 1,250 sq ft condo.',
        tech_stack: ['10× ESP32-WROOM-32', 'BME688 sensors', 'LD2450 mm-wave radars', 'ESPHome 2023.12', 'Home Assistant', 'Mosquitto MQTT', 'InfluxDB 2', 'Grafana', 'Tailscale VPN', 'Pi-hole DNS'],
        features: [
            'Sensor mesh coverage across 6 zones with real-time heat-maps',
            'Adaptive HVAC & blinds balancing IAQ and comfort automatically',
            'Presence-aware lighting with <100ms response via LD2450 radar',
            'Energy & network dashboards with Slack anomaly alerting',
            'Voice-first control via Mycroft AI (completely offline)',
            'Whole-home ad-blocking via Pi-hole reducing WAN data 25%'
        ],
        challenges: 'Achieved low-latency telemetry without Wi-Fi saturation via tuned ESP32 QoS, calibrated sensor accuracy in mixed HVAC airflow, secured remote access migrating from port-forwards to Tailscale mesh.',
        impact: 'Maintained temp ±1°C and humidity 40-55% year-round, achieved 99.9% service uptime, collected 2M+ time-series points, cut annual energy use 8%, provided DevOps sandbox shortening POC cycles 40%.'
    }
};

function openModal(projectId) {
    const project = projects[projectId];
    if (!project) return;

    // Populate modal content
    document.getElementById('modalTitle').textContent = project.title;
    document.getElementById('modalType').textContent = project.type;
    
    // Set modal image
    const modalImage = document.getElementById('modalImage');
    modalImage.innerHTML = `<img src="${project.image}" alt="${project.title}" style="width: 100%; height: 100%; object-fit: cover; opacity: 1;">`;
    
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

// ===== FOOTER LINK BEHAVIORS =====
function handleProjectsLink(event) {
    if (window.location.pathname === '/projects') {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

function handleResumeLink(event) {
    if (window.location.pathname === '/resume') {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

function expandContactOnMainPage() {
    if (window.location.pathname === '/') {
        // On main page, expand contact form
        expandContactForm();
    } else {
        // On other pages, navigate to main page with contact expanded
        window.location.href = '/#contact';
        setTimeout(() => {
            if (typeof expandContactForm === 'function') {
                expandContactForm();
            }
        }, 100);
    }
}

// ===== EVENT LISTENERS =====
// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('projectModal');
    if (event.target === modal) {
        closeModal();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

// Make sure modal closes properly on page load
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('projectModal');
    if (modal) {
        modal.classList.remove('show');
    }
});

// ===== GLOBAL FUNCTIONS =====
// Make functions available globally for inline onclick handlers
window.scrollToTop = scrollToTop;
window.toggleContactForm = toggleContactForm;
window.expandContactForm = expandContactForm;
window.openModal = openModal;
window.closeModal = closeModal;
window.handleProjectsLink = handleProjectsLink;
window.handleResumeLink = handleResumeLink;
window.expandContactOnMainPage = expandContactOnMainPage;