# Developer Portfolio Website

A modern, minimalist portfolio website built with Flask, inspired by the clean layouts of [thea.juniorise.com](https://thea.juniorise.com/) and the aesthetic typography of [long-nguyen.dev](https://long-nguyen.dev/).

## 🎨 Design Inspiration

### Layout Structure (Thea Choem)
- Clean hero section with personal introduction
- Portfolio/Projects grid with hover animations
- Developer story timeline
- Testimonials section
- Simple header/footer navigation

### Typography & Aesthetics (Long Nguyen)
- Modern, minimalist typography
- Elegant spacing and layout
- Subtle animations and interactions
- Professional color palette

## 🚀 Features

### Core Features
- **Responsive Design**: Mobile-first approach with smooth transitions
- **Portfolio Showcase**: Grid layout with hover animations for project previews
- **Developer Timeline**: Interactive story/experience timeline
- **Contact Integration**: Contact form with email functionality
- **Admin Panel**: Simple CMS for content management
- **SEO Optimized**: Meta tags, structured data, and performance optimization

### Interactive Elements
- Smooth hover animations on portfolio items
- Parallax scrolling effects
- Typing animation for hero text
- Image lazy loading
- Smooth scroll navigation

## 🛠 Tech Stack

### Backend
- **Flask**: Python web framework
- **SQLite**: Database for content management
- **Flask-Mail**: Email functionality
- **Flask-Admin**: Content management interface
- **Gunicorn**: WSGI server for production

### Frontend
- **HTML5/CSS3**: Semantic markup and modern styling
- **JavaScript (Vanilla)**: Smooth animations and interactions
- **SCSS**: Organized styling with variables and mixins
- **Font Awesome**: Icon library
- **Google Fonts**: Typography (Inter, Playfair Display)

### Development Tools
- **Python Virtual Environment**: Isolated dependencies
- **Flask-Debug**: Development debugging
- **Watchdog**: File watching for auto-reload
- **Black**: Code formatting

## 📁 Project Structure

```
dev-portfolio-site/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models
│   ├── routes.py                # Application routes
│   ├── admin.py                 # Admin panel configuration
│   ├── forms.py                 # WTForms for contact/admin
│   ├── email.py                 # Email functionality
│   └── utils.py                 # Helper functions
├── static/
│   ├── css/
│   │   ├── main.scss            # Main stylesheet
│   │   ├── components/          # Component-specific styles
│   │   └── compiled/            # Compiled CSS
│   ├── js/
│   │   ├── main.js              # Main JavaScript
│   │   ├── animations.js        # Animation effects
│   │   └── components/          # JS components
│   ├── images/
│   │   ├── portfolio/           # Project screenshots
│   │   ├── profile/             # Personal photos
│   │   └── icons/               # Favicons and icons
│   └── fonts/                   # Custom fonts
├── templates/
│   ├── base.html                # Base template
│   ├── index.html               # Homepage
│   ├── portfolio.html           # Portfolio detail pages
│   ├── contact.html             # Contact page
│   └── admin/                   # Admin templates
├── migrations/                  # Database migrations
├── tests/                       # Unit and integration tests
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 🎯 Page Sections

### 1. Hero Section
- Animated greeting with typing effect
- Professional headshot with subtle hover animation
- Brief introduction and role description
- Call-to-action buttons (Portfolio, Contact)

### 2. About Section
- Expanded bio with personality
- Skills showcase with animated progress bars
- GitHub stats integration
- Download resume button

### 3. Portfolio Section
- Masonry/grid layout for projects
- Hover animations revealing project details
- Filter by technology/category
- Modal popups for detailed project views
- Live demo and source code links

### 4. Developer Story
- Timeline layout with experience milestones
- Company logos and descriptions
- Interactive hover states
- Smooth scroll reveal animations

### 5. Testimonials (Optional)
- Rotating testimonial cards
- Client/colleague recommendations
- Star ratings and source attribution

### 6. Contact Section
- Working contact form
- Social media links
- Location and availability info
- Email confirmation system

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### 🚀 **SUPER SIMPLE - ONE COMMAND SETUP!**

**Just run this ONE command and everything will work:**

```bash
python run.py
```

**That's it! This command will:**
- ✅ Automatically create virtual environment
- ✅ Install all dependencies  
- ✅ Set up the database
- ✅ Add sample portfolio data
- ✅ Start the development server

**Then open your browser and visit:**
- **Website:** http://localhost:5000
- **Admin Panel:** http://localhost:5000/admin

### Alternative Setup Options
**Windows users:** Double-click `setup.bat`
**Mac/Linux users:** Run `./setup.sh` in terminal

### What You'll See
- 🏠 **Homepage:** Hero section, portfolio, skills, and experience timeline
- 💼 **Portfolio:** Filterable project gallery with filters
- 📧 **Contact:** Working contact form with validation
- ⚙️ **Admin:** Content management at `/admin`
- 📱 **Responsive:** Works perfectly on mobile and desktop
- ✨ **Animations:** Smooth scroll effects and hover animations

## ⚙️ Configuration

### Environment Variables (.env)
```
SECRET_KEY=your-secret-key-here
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
ADMIN_EMAIL=admin@yoursite.com
DATABASE_URL=sqlite:///portfolio.db
```

## 🎨 Customization

### Colors and Typography
- Edit `static/css/main.scss` for global styles
- Customize color palette in `_variables.scss`
- Adjust typography settings for different font combinations

### Content Management
- Use the admin panel at `/admin` to manage:
  - Portfolio projects
  - Experience timeline
  - Skills and technologies
  - Contact information

### Animations
- Modify `static/js/animations.js` for custom effects
- Adjust CSS transitions in component stylesheets
- Configure scroll-reveal timings

## 🚀 Deployment

### Local Testing
```bash
python run.py
```

### Production Deployment
1. **Configure production settings**
2. **Set up database**
3. **Configure web server (Nginx + Gunicorn)**
4. **Set up SSL certificate**
5. **Configure domain and DNS**

### Docker Deployment
```bash
docker build -t portfolio-site .
docker run -p 5000:5000 portfolio-site
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=app tests/

# Run specific test file
python -m pytest tests/test_routes.py
```

## 📱 Features Roadmap

### Phase 1 (MVP) ✅ COMPLETED
- [x] Basic Flask setup
- [x] Hero section with animations
- [x] Portfolio grid layout
- [x] Contact form functionality
- [x] Responsive design

### Phase 2 (Enhanced) ✅ COMPLETED
- [x] Admin panel for content management
- [x] Developer story timeline
- [x] Advanced animations
- [x] SEO optimization
- [x] Performance optimization

### Phase 3 (Advanced) - Future Enhancements
- [ ] Blog integration
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] API endpoints
- [ ] Progressive Web App features

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Thea Choem](https://thea.juniorise.com/) for layout inspiration
- [Long Nguyen](https://long-nguyen.dev/) for typography and aesthetic inspiration
- Flask community for excellent documentation
- Open source contributors

## 📞 Support

For support, email [your-email] or create an issue in the GitHub repository.

---

**Built with ❤️ using Flask and modern web technologies** 