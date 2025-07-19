from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_admin import Admin
from config import config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
admin_instance = Admin()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    admin_instance.init_app(app)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    # Set up admin views after models are imported
    with app.app_context():
        from app.models import Project, Experience, Skill, ContactMessage, SiteSettings
        from app.admin import ProjectAdmin, ExperienceAdmin, SkillAdmin, ContactMessageAdmin, SiteSettingsAdmin, DashboardView
        
        # Add dashboard
        admin_instance.add_view(DashboardView(name='Dashboard', endpoint='dashboard'))
        
        # Add model views
        admin_instance.add_view(ProjectAdmin(Project, db.session, name='Projects'))
        admin_instance.add_view(ExperienceAdmin(Experience, db.session, name='Experience'))
        admin_instance.add_view(SkillAdmin(Skill, db.session, name='Skills'))
        admin_instance.add_view(ContactMessageAdmin(ContactMessage, db.session, name='Messages'))
        admin_instance.add_view(SiteSettingsAdmin(SiteSettings, db.session, name='Site Settings'))
    
    return app 