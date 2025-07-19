// ===== ANIMATIONS JAVASCRIPT FILE =====

// Animation configuration
const ANIMATION_CONFIG = {
    duration: {
        fast: 200,
        normal: 300,
        slow: 500
    },
    easing: {
        ease: 'ease',
        easeIn: 'ease-in',
        easeOut: 'ease-out',
        easeInOut: 'ease-in-out',
        bounce: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)'
    },
    delays: {
        stagger: 100,
        reveal: 200
    }
};

// Initialize animations when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initScrollReveal();
    initHoverEffects();
    initTypingAnimation();
    initParticleBackground();
    initImageHoverEffects();
    initButtonAnimations();
});

// ===== SCROLL REVEAL ANIMATIONS =====
function initScrollReveal() {
    // Create intersection observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add staggered delay for multiple elements
                const delay = index * ANIMATION_CONFIG.delays.stagger;
                
                setTimeout(() => {
                    entry.target.classList.add('revealed');
                    
                    // Trigger specific animations based on element type
                    triggerSpecificAnimation(entry.target);
                }, delay);
                
                // Stop observing once revealed
                revealObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Elements to reveal on scroll
    const revealElements = document.querySelectorAll(`
        .portfolio-item,
        .timeline-item,
        .skill-category,
        .contact-method,
        .hero-text,
        .hero-image,
        .section-header
    `);

    revealElements.forEach(el => {
        el.classList.add('reveal-element');
        revealObserver.observe(el);
    });
}

// ===== SPECIFIC ANIMATIONS =====
function triggerSpecificAnimation(element) {
    // Portfolio items animation
    if (element.classList.contains('portfolio-item')) {
        animatePortfolioItem(element);
    }
    
    // Timeline items animation
    if (element.classList.contains('timeline-item')) {
        animateTimelineItem(element);
    }
    
    // Skill bars animation
    if (element.classList.contains('skill-category')) {
        animateSkillBars(element);
    }
    
    // Contact methods animation
    if (element.classList.contains('contact-method')) {
        animateContactMethod(element);
    }
}

function animatePortfolioItem(element) {
    element.style.animation = `slideInUp ${ANIMATION_CONFIG.duration.normal}ms ${ANIMATION_CONFIG.easing.easeOut}`;
    
    // Animate child elements
    const image = element.querySelector('.portfolio-image img');
    const content = element.querySelector('.portfolio-content');
    
    if (image) {
        setTimeout(() => {
            image.style.animation = `zoomIn ${ANIMATION_CONFIG.duration.slow}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        }, 100);
    }
    
    if (content) {
        setTimeout(() => {
            content.style.animation = `fadeInUp ${ANIMATION_CONFIG.duration.normal}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        }, 200);
    }
}

function animateTimelineItem(element) {
    const marker = element.querySelector('.timeline-marker');
    const content = element.querySelector('.timeline-content');
    
    element.style.animation = `slideInLeft ${ANIMATION_CONFIG.duration.normal}ms ${ANIMATION_CONFIG.easing.easeOut}`;
    
    if (marker) {
        setTimeout(() => {
            marker.style.animation = `bounceIn ${ANIMATION_CONFIG.duration.slow}ms ${ANIMATION_CONFIG.easing.bounce}`;
        }, 200);
    }
    
    if (content) {
        setTimeout(() => {
            content.style.animation = `fadeInRight ${ANIMATION_CONFIG.duration.normal}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        }, 300);
    }
}

function animateSkillBars(element) {
    const progressBars = element.querySelectorAll('.skill-progress');
    
    progressBars.forEach((bar, index) => {
        const targetWidth = bar.style.width;
        bar.style.width = '0%';
        bar.style.transition = `width ${ANIMATION_CONFIG.duration.slow * 2}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, index * 100 + 300);
    });
}

function animateContactMethod(element) {
    const icon = element.querySelector('.contact-method-icon');
    const content = element.querySelector('.contact-method-content');
    
    if (icon) {
        icon.style.animation = `bounceIn ${ANIMATION_CONFIG.duration.slow}ms ${ANIMATION_CONFIG.easing.bounce}`;
    }
    
    if (content) {
        setTimeout(() => {
            content.style.animation = `fadeInRight ${ANIMATION_CONFIG.duration.normal}ms ${ANIMATION_CONFIG.easing.easeOut}`;
        }, 200);
    }
}

// ===== HOVER EFFECTS =====
function initHoverEffects() {
    // Portfolio card hover effects
    const portfolioCards = document.querySelectorAll('.portfolio-card');
    portfolioCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
            this.style.boxShadow = '0 20px 40px rgba(0, 0, 0, 0.15)';
            
            // Animate image
            const image = this.querySelector('.portfolio-image img');
            if (image) {
                image.style.transform = 'scale(1.1)';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            this.style.boxShadow = '';
            
            // Reset image
            const image = this.querySelector('.portfolio-image img');
            if (image) {
                image.style.transform = 'scale(1)';
            }
        });
    });
    
    // Skill category hover effects
    const skillCategories = document.querySelectorAll('.skill-category');
    skillCategories.forEach(category => {
        category.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.1)';
        });
        
        category.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
    
    // Timeline content hover effects
    const timelineContents = document.querySelectorAll('.timeline-content');
    timelineContents.forEach(content => {
        content.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px)';
            this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.1)';
        });
        
        content.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
}

// ===== TYPING ANIMATION =====
function initTypingAnimation() {
    const typingElements = document.querySelectorAll('.typing-text');
    
    typingElements.forEach(element => {
        const text = element.textContent;
        element.textContent = '';
        element.style.borderRight = '2px solid var(--primary-color)';
        
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                // Blinking cursor effect
                setInterval(() => {
                    element.style.borderRight = element.style.borderRight === 'none' 
                        ? '2px solid var(--primary-color)' 
                        : 'none';
                }, 500);
            }
        }
        
        // Start typing after a delay
        setTimeout(typeWriter, 1000);
    });
}

// ===== PARTICLE BACKGROUND =====
function initParticleBackground() {
    const hero = document.querySelector('.hero');
    if (!hero) return;
    
    // Create canvas for particles
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.opacity = '0.3';
    canvas.style.zIndex = '0';
    
    hero.appendChild(canvas);
    
    // Resize canvas
    function resizeCanvas() {
        canvas.width = hero.offsetWidth;
        canvas.height = hero.offsetHeight;
    }
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    // Particle system
    const particles = [];
    const particleCount = 50;
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.radius = Math.random() * 2 + 1;
            this.opacity = Math.random() * 0.5 + 0.2;
        }
        
        update() {
            this.x += this.vx;
            this.y += this.vy;
            
            if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
            if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(37, 99, 235, ${this.opacity})`;
            ctx.fill();
        }
    }
    
    // Initialize particles
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    // Animation loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles.forEach(particle => {
            particle.update();
            particle.draw();
        });
        
        // Draw connections
        particles.forEach((particle, i) => {
            particles.slice(i + 1).forEach(otherParticle => {
                const dx = particle.x - otherParticle.x;
                const dy = particle.y - otherParticle.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.beginPath();
                    ctx.moveTo(particle.x, particle.y);
                    ctx.lineTo(otherParticle.x, otherParticle.y);
                    ctx.strokeStyle = `rgba(37, 99, 235, ${0.2 * (1 - distance / 100)})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            });
        });
        
        requestAnimationFrame(animate);
    }
    
    animate();
}

// ===== IMAGE HOVER EFFECTS =====
function initImageHoverEffects() {
    const profileImage = document.querySelector('.profile-image');
    if (profileImage) {
        profileImage.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05) rotate(2deg)';
            this.style.filter = 'brightness(1.1)';
        });
        
        profileImage.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
            this.style.filter = 'brightness(1)';
        });
    }
    
    // Portfolio image parallax effect
    const portfolioImages = document.querySelectorAll('.portfolio-image');
    portfolioImages.forEach(container => {
        container.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / centerY * 10;
            const rotateY = (centerX - x) / centerX * 10;
            
            const image = this.querySelector('img');
            if (image) {
                image.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.1)`;
            }
        });
        
        container.addEventListener('mouseleave', function() {
            const image = this.querySelector('img');
            if (image) {
                image.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
            }
        });
    });
}

// ===== BUTTON ANIMATIONS =====
function initButtonAnimations() {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        // Ripple effect
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
        
        // Hover animation
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
}

// ===== SCROLL-TRIGGERED ANIMATIONS =====
function initScrollAnimations() {
    let ticking = false;
    
    function updateAnimations() {
        const scrollY = window.scrollY;
        const windowHeight = window.innerHeight;
        
        // Parallax effects
        const hero = document.querySelector('.hero');
        if (hero) {
            const rate = scrollY * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        }
        
        // Navigation bar transparency
        const navbar = document.querySelector('.navbar');
        if (navbar) {
            const opacity = Math.min(scrollY / 100, 1);
            navbar.style.backgroundColor = `rgba(255, 255, 255, ${0.95 + opacity * 0.05})`;
        }
        
        ticking = false;
    }
    
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateAnimations);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestTick);
}

// ===== CSS KEYFRAMES (Injected dynamically) =====
function injectAnimationStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .reveal-element {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease-out;
        }
        
        .reveal-element.revealed {
            opacity: 1;
            transform: translateY(0);
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInRight {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes bounceIn {
            0% {
                opacity: 0;
                transform: scale(0.3);
            }
            50% {
                opacity: 1;
                transform: scale(1.05);
            }
            70% {
                transform: scale(0.9);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        @keyframes zoomIn {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.3);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
        
        .btn {
            position: relative;
            overflow: hidden;
        }
        
        @media (prefers-reduced-motion: reduce) {
            .reveal-element,
            .portfolio-card,
            .skill-category,
            .timeline-content {
                transition: none !important;
                animation: none !important;
            }
        }
    `;
    
    document.head.appendChild(style);
}

// Initialize animation styles
injectAnimationStyles();

// Initialize scroll animations
initScrollAnimations();

// Export functions for external use
window.AnimationLib = {
    initScrollReveal,
    initHoverEffects,
    initTypingAnimation,
    initParticleBackground,
    triggerSpecificAnimation
}; 