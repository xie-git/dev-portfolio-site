from datetime import datetime
from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    technologies = db.Column(db.String(300))  # Comma-separated list
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order_index = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Project {self.title}>'
    
    def get_tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()] if self.technologies else []

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    company_url = db.Column(db.String(200))
    company_logo = db.Column(db.String(200))
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)  # NULL for current position
    description = db.Column(db.Text)
    experience_type = db.Column(db.String(20), default='work')  # work, education, volunteer
    order_index = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Experience {self.title} at {self.company}>'
    
    @property
    def is_current(self):
        return self.end_date is None
    
    @property
    def duration(self):
        end = self.end_date or datetime.now().date()
        return f"{self.start_date.strftime('%b %Y')} - {'Present' if self.is_current else end.strftime('%b %Y')}"

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # frontend, backend, tools, etc.
    proficiency = db.Column(db.Integer, default=50)  # 0-100
    icon_class = db.Column(db.String(50))  # Font Awesome icon class
    order_index = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Skill {self.name}>'

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<ContactMessage from {self.name}>'

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.Text)
    
    def __repr__(self):
        return f'<SiteSettings {self.key}>'
    
    @staticmethod
    def get_setting(key, default=None):
        setting = SiteSettings.query.filter_by(key=key).first()
        return setting.value if setting else default
    
    @staticmethod
    def set_setting(key, value):
        setting = SiteSettings.query.filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            setting = SiteSettings(key=key, value=value)
            db.session.add(setting)
        db.session.commit() 