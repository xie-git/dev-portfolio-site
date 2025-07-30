#!/usr/bin/env python3
"""
Simple Portfolio Website - Main Application File
"""

import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, send_from_directory, send_file, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, EmailField, validators, FileField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length, Optional
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import secrets

# Initialize database
db = SQLAlchemy()

# Email configuration and functions
def send_email(to_email, subject, html_body, reply_to_email=None):
    """
    Send email using SMTP. This function supports multiple email providers.
    For production, you should use environment variables for credentials.
    """
    try:
        # Email configuration - replace with your actual SMTP settings
        smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.environ.get('SMTP_PORT', '587'))
        smtp_username = os.environ.get('SMTP_USERNAME', 'your-email@gmail.com')
        smtp_password = os.environ.get('SMTP_PASSWORD', 'your-app-password')
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if reply_to_email:
            msg['Reply-To'] = reply_to_email
        
        # Add HTML body
        html_part = MIMEText(html_body, 'html')
        msg.attach(html_part)
        
        # Send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

def create_contact_email_html(name, email, subject, message):
    """Create HTML email template for contact form submissions."""
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>New Contact Form Submission</title>
        <style>
            body {{ font-family: 'PP Neue Montreal', -apple-system, BlinkMacSystemFont, sans-serif; margin: 0; padding: 20px; background: #f8f4f5; }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; border-radius: 8px; padding: 30px; box-shadow: 0 2px 10px rgba(74, 56, 71, 0.1); }}
            .header {{ border-bottom: 2px solid #4a3847; padding-bottom: 20px; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; color: #4a3847; font-size: 24px; font-weight: 400; }}
            .field {{ margin-bottom: 20px; }}
            .field-label {{ font-weight: 500; color: #4a3847; margin-bottom: 5px; display: block; }}
            .field-value {{ background: #f8f4f5; padding: 12px; border-radius: 4px; border-left: 3px solid #4a3847; }}
            .message-field {{ white-space: pre-wrap; line-height: 1.6; }}
            .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; color: #666; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🚀 New Portfolio Contact</h1>
            </div>
            
            <div class="field">
                <span class="field-label">From:</span>
                <div class="field-value">{name} &lt;{email}&gt;</div>
            </div>
            
            <div class="field">
                <span class="field-label">Subject:</span>
                <div class="field-value">{subject}</div>
            </div>
            
            <div class="field">
                <span class="field-label">Message:</span>
                <div class="field-value message-field">{message}</div>
            </div>
            
            <div class="footer">
                <p>This message was sent from your portfolio contact form at <a href="https://micheal-xie.dev">micheal-xie.dev</a></p>
                <p>To reply, respond directly to this email or contact {email}</p>
            </div>
        </div>
    </body>
    </html>
    """

# Database models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String(50), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    overview = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.Text)  # JSON string
    features = db.Column(db.Text)  # JSON string
    challenges = db.Column(db.Text)
    impact = db.Column(db.Text)
    description = db.Column(db.String(200))  # Short description for card
    github_url = db.Column(db.String(500))  # GitHub repository URL
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'title': self.title,
            'type': self.type,
            'image': self.image,
            'overview': self.overview,
            'tech_stack': json.loads(self.tech_stack) if self.tech_stack else [],
            'features': json.loads(self.features) if self.features else [],
            'challenges': self.challenges,
            'impact': self.impact,
            'description': self.description,
            'github_url': self.github_url,
            'order_index': self.order_index,
            'is_active': self.is_active
        }

# Bio model for intro section
class Bio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    statement_highlight = db.Column(db.Text)  # Skills/specialties line
    statement_description = db.Column(db.Text)  # Years of experience description
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'statement_highlight': self.statement_highlight,
            'statement_description': self.statement_description,
            'is_active': self.is_active
        }

# Developer story timeline items
class TimelineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)  # 'work' or 'education'
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100))
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50))  # Can be null for current position
    description = db.Column(db.Text, nullable=False)
    logo_image = db.Column(db.String(200))  # Path to company logo
    order_index = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'logo_image': self.logo_image,
            'order_index': self.order_index,
            'is_active': self.is_active
        }

# Contact message model for form submissions
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    is_replied = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'is_read': self.is_read,
            'is_replied': self.is_replied,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Activity log model for admin actions
class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def to_dict(self):
        return {
            'id': self.id,
            'action': self.action,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# Contact form class for CSRF protection and validation
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])

# Project form for admin
class ProjectForm(FlaskForm):
    project_id = StringField('Project ID', validators=[DataRequired(), Length(min=2, max=50)])
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    type = StringField('Type', validators=[DataRequired(), Length(min=2, max=100)])
    image = FileField('Image', validators=[Optional()])
    overview = TextAreaField('Overview', validators=[DataRequired()])
    tech_stack = TextAreaField('Tech Stack (one per line)', validators=[Optional()])
    features = TextAreaField('Features (one per line)', validators=[Optional()])
    challenges = TextAreaField('Challenges', validators=[Optional()])
    impact = TextAreaField('Impact', validators=[Optional()])
    description = StringField('Card Description', validators=[Optional(), Length(max=200)])
    github_url = StringField('GitHub Repository URL', validators=[Optional(), Length(max=500)])
    order_index = StringField('Order Index', validators=[Optional()])

# Bio form for admin
class BioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Bio Description', validators=[DataRequired()])
    statement_highlight = TextAreaField('Skills/Specialties', validators=[Optional()])
    statement_description = TextAreaField('Experience Description', validators=[Optional()])

# Timeline item form for admin
class TimelineForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired(), Length(min=2, max=20)])
    title = StringField('Title/Position', validators=[DataRequired(), Length(min=2, max=200)])
    company = StringField('Company/Institution', validators=[DataRequired(), Length(min=2, max=200)])
    location = StringField('Location', validators=[Optional(), Length(max=100)])
    start_date = StringField('Start Date', validators=[DataRequired(), Length(min=2, max=50)])
    end_date = StringField('End Date', validators=[Optional(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired()])
    logo_image = FileField('Company Logo', validators=[Optional()])
    order_index = StringField('Order Index', validators=[Optional()])

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    
    # Generate secure secret key for production
    app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    
    # Database configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "portfolio.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'static/images/projects'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # Initialize extensions
    db.init_app(app)
    csrf = CSRFProtect(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Security headers
    @app.after_request
    def security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response

    # Flask routes using templates
    
    @app.route('/')
    def home():
        # Get active bio and timeline items
        bio = Bio.query.filter_by(is_active=True).first()
        timeline_items = TimelineItem.query.filter_by(is_active=True).order_by(TimelineItem.order_index).all()
        projects = Project.query.filter_by(is_active=True).order_by(Project.order_index).limit(4).all()
        
        return render_template('index.html', 
                             bio=bio.to_dict() if bio else None,
                             timeline_items=[item.to_dict() for item in timeline_items],
                             featured_projects={p.project_id: p.to_dict() for p in projects})
    
    @app.route('/Xie_Data_Resume.pdf')
    def resume():
        return send_file('Xie_Data_Resume.pdf', as_attachment=False)
    
    @app.route('/projects')
    def all_projects():
        # Get all active projects from database
        projects = Project.query.filter_by(is_active=True).order_by(Project.order_index).all()
        projects_dict = {p.project_id: p.to_dict() for p in projects}
        return render_template('projects.html', projects=projects_dict)

    @app.route('/resume')
    def resume_page():
        return render_template('resume.html')

    # SEO and metadata routes
    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory('static', 'sitemap.xml', mimetype='application/xml')
    
    @app.route('/robots.txt')
    def robots():
        return send_from_directory('static', 'robots.txt', mimetype='text/plain')
    
    @app.route('/site.webmanifest')
    def webmanifest():
        return send_from_directory('static', 'site.webmanifest', mimetype='application/manifest+json')

    @app.route('/about')
    def about_page():
        return render_template('about.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            try:
                # Extract form data
                name = form.name.data
                email = form.email.data
                subject = form.subject.data
                message = form.message.data
                
                # Save to database
                contact_message = ContactMessage(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                db.session.add(contact_message)
                
                # Log activity
                activity = ActivityLog(
                    action='contact_received',
                    description=f'New contact message from {name} ({email}): {subject}'
                )
                db.session.add(activity)
                db.session.commit()
                
                # Create email content
                email_subject = f"Portfolio Contact: {subject}"
                email_html = create_contact_email_html(name, email, subject, message)
                
                # Send email to yourself
                recipient_email = os.environ.get('CONTACT_EMAIL', 'xie.michael@icloud.com')
                email_sent = send_email(
                    to_email=recipient_email,
                    subject=email_subject,
                    html_body=email_html,
                    reply_to_email=email
                )
                
                if email_sent:
                    flash('Thank you for your message! I\'ll get back to you soon.', 'success')
                else:
                    # Fall back to mailto if email sending fails
                    flash('Message received! If you don\'t hear back soon, please email me directly at xie.michael@icloud.com', 'success')
                
                return redirect(url_for('contact'))
                
            except Exception as e:
                print(f"Contact form error: {e}")
                flash('Thank you for your message! I\'ll get back to you soon.', 'success')
                return redirect(url_for('contact'))
                
        return render_template('contact.html', form=form)
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500
    
    # Admin routes
    @app.route('/admin')
    def admin():
        projects = Project.query.order_by(Project.order_index).all()
        bio = Bio.query.filter_by(is_active=True).first()
        timeline_items = TimelineItem.query.order_by(TimelineItem.order_index).all()
        
        # Get data for new admin features
        messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).limit(10).all()
        activity_logs = ActivityLog.query.order_by(ActivityLog.created_at.desc()).limit(10).all()
        
        # Analytics data (placeholder/basic stats)
        total_messages = ContactMessage.query.count()
        unread_messages = ContactMessage.query.filter_by(is_read=False).count()
        total_projects = Project.query.count()
        active_projects = Project.query.filter_by(is_active=True).count()
        
        analytics = {
            'total_visitors': 1247,  # Placeholder - would come from analytics service
            'page_views': 3451,     # Placeholder
            'total_messages': total_messages,
            'unread_messages': unread_messages,
            'total_projects': total_projects,
            'active_projects': active_projects,
            'bounce_rate': 34.2     # Placeholder
        }
        
        return render_template('admin.html', 
                             projects=projects,
                             bio=bio.to_dict() if bio else None,
                             timeline_items=[item.to_dict() for item in timeline_items],
                             messages=[msg.to_dict() for msg in messages],
                             activity_logs=[log.to_dict() for log in activity_logs],
                             analytics=analytics)
    
    @app.route('/admin/project/new', methods=['GET', 'POST'])
    def admin_project_new():
        form = ProjectForm()
        if form.validate_on_submit():
            # Handle file upload
            image_filename = None
            if form.image.data:
                file = form.image.data
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    # Create upload folder if it doesn't exist
                    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    image_filename = f"/static/images/projects/{filename}"
            
            # Create new project
            project = Project(
                project_id=form.project_id.data,
                title=form.title.data,
                type=form.type.data,
                image=image_filename,
                overview=form.overview.data,
                tech_stack=json.dumps([x.strip() for x in form.tech_stack.data.split('\n') if x.strip()]) if form.tech_stack.data else '[]',
                features=json.dumps([x.strip() for x in form.features.data.split('\n') if x.strip()]) if form.features.data else '[]',
                challenges=form.challenges.data,
                impact=form.impact.data,
                description=form.description.data,
                github_url=form.github_url.data,
                order_index=int(form.order_index.data) if form.order_index.data else 0
            )
            
            try:
                db.session.add(project)
                db.session.commit()
                flash('Project created successfully!', 'success')
                return redirect(url_for('admin'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error creating project: {str(e)}', 'error')
        
        return render_template('admin_project_form.html', form=form, action='new')
    
    @app.route('/admin/project/<int:id>/edit', methods=['GET', 'POST'])
    def admin_project_edit(id):
        project = Project.query.get_or_404(id)
        form = ProjectForm()
        
        if form.validate_on_submit():
            # Handle file upload
            if form.image.data:
                file = form.image.data
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    project.image = f"/static/images/projects/{filename}"
            
            # Update project
            project.project_id = form.project_id.data
            project.title = form.title.data
            project.type = form.type.data
            project.overview = form.overview.data
            project.tech_stack = json.dumps([x.strip() for x in form.tech_stack.data.split('\n') if x.strip()]) if form.tech_stack.data else '[]'
            project.features = json.dumps([x.strip() for x in form.features.data.split('\n') if x.strip()]) if form.features.data else '[]'
            project.challenges = form.challenges.data
            project.impact = form.impact.data
            project.description = form.description.data
            project.github_url = form.github_url.data
            project.order_index = int(form.order_index.data) if form.order_index.data else 0
            
            try:
                db.session.commit()
                flash('Project updated successfully!', 'success')
                return redirect(url_for('admin'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating project: {str(e)}', 'error')
        else:
            # Pre-populate form
            form.project_id.data = project.project_id
            form.title.data = project.title
            form.type.data = project.type
            form.overview.data = project.overview
            form.tech_stack.data = '\n'.join(json.loads(project.tech_stack)) if project.tech_stack else ''
            form.features.data = '\n'.join(json.loads(project.features)) if project.features else ''
            form.challenges.data = project.challenges
            form.impact.data = project.impact
            form.description.data = project.description
            form.github_url.data = project.github_url
            form.order_index.data = str(project.order_index)
        
        return render_template('admin_project_form.html', form=form, action='edit', project=project)
    
    @app.route('/admin/project/<int:id>/delete', methods=['POST'])
    def admin_project_delete(id):
        project = Project.query.get_or_404(id)
        try:
            db.session.delete(project)
            db.session.commit()
            flash('Project deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting project: {str(e)}', 'error')
        return redirect(url_for('admin'))
    
    @app.route('/admin/project/<int:id>/toggle', methods=['POST'])
    def admin_project_toggle(id):
        project = Project.query.get_or_404(id)
        project.is_active = not project.is_active
        db.session.commit()
        return jsonify({'success': True, 'is_active': project.is_active})
    
    # Bio admin routes
    @app.route('/admin/bio/edit', methods=['GET', 'POST'])
    def admin_bio_edit():
        bio = Bio.query.filter_by(is_active=True).first()
        form = BioForm()
        
        if form.validate_on_submit():
            if bio:
                # Update existing bio
                bio.title = form.title.data
                bio.description = form.description.data
                bio.statement_highlight = form.statement_highlight.data
                bio.statement_description = form.statement_description.data
            else:
                # Create new bio
                bio = Bio(
                    title=form.title.data,
                    description=form.description.data,
                    statement_highlight=form.statement_highlight.data,
                    statement_description=form.statement_description.data,
                    is_active=True
                )
                db.session.add(bio)
            
            try:
                db.session.commit()
                flash('Bio updated successfully!', 'success')
                return redirect(url_for('admin'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating bio: {str(e)}', 'error')
        else:
            # Pre-populate form if bio exists
            if bio:
                form.title.data = bio.title
                form.description.data = bio.description
                form.statement_highlight.data = bio.statement_highlight
                form.statement_description.data = bio.statement_description
        
        return render_template('admin_bio_form.html', form=form, bio=bio)
    
    # Timeline admin routes
    @app.route('/admin/timeline/new', methods=['GET', 'POST'])
    def admin_timeline_new():
        form = TimelineForm()
        if form.validate_on_submit():
            # Handle logo upload
            logo_filename = None
            if form.logo_image.data:
                file = form.logo_image.data
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    os.makedirs('static/images/companies', exist_ok=True)
                    file.save(os.path.join('static/images/companies', filename))
                    logo_filename = f"/static/images/companies/{filename}"
            
            timeline_item = TimelineItem(
                type=form.type.data,
                title=form.title.data,
                company=form.company.data,
                location=form.location.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                description=form.description.data,
                logo_image=logo_filename,
                order_index=int(form.order_index.data) if form.order_index.data else 0
            )
            
            try:
                db.session.add(timeline_item)
                db.session.commit()
                flash('Timeline item created successfully!', 'success')
                return redirect(url_for('admin'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error creating timeline item: {str(e)}', 'error')
        
        return render_template('admin_timeline_form.html', form=form, action='new')
    
    @app.route('/admin/timeline/<int:id>/edit', methods=['GET', 'POST'])
    def admin_timeline_edit(id):
        timeline_item = TimelineItem.query.get_or_404(id)
        form = TimelineForm()
        
        if form.validate_on_submit():
            # Handle logo upload
            if form.logo_image.data:
                file = form.logo_image.data
                if file and file.filename:
                    filename = secure_filename(file.filename)
                    os.makedirs('static/images/companies', exist_ok=True)
                    file.save(os.path.join('static/images/companies', filename))
                    timeline_item.logo_image = f"/static/images/companies/{filename}"
            
            timeline_item.type = form.type.data
            timeline_item.title = form.title.data
            timeline_item.company = form.company.data
            timeline_item.location = form.location.data
            timeline_item.start_date = form.start_date.data
            timeline_item.end_date = form.end_date.data
            timeline_item.description = form.description.data
            timeline_item.order_index = int(form.order_index.data) if form.order_index.data else 0
            
            try:
                db.session.commit()
                flash('Timeline item updated successfully!', 'success')
                return redirect(url_for('admin'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating timeline item: {str(e)}', 'error')
        else:
            # Pre-populate form
            form.type.data = timeline_item.type
            form.title.data = timeline_item.title
            form.company.data = timeline_item.company
            form.location.data = timeline_item.location
            form.start_date.data = timeline_item.start_date
            form.end_date.data = timeline_item.end_date
            form.description.data = timeline_item.description
            form.order_index.data = str(timeline_item.order_index)
        
        return render_template('admin_timeline_form.html', form=form, action='edit', timeline_item=timeline_item)
    
    @app.route('/admin/timeline/<int:id>/delete', methods=['POST'])
    def admin_timeline_delete(id):
        timeline_item = TimelineItem.query.get_or_404(id)
        try:
            db.session.delete(timeline_item)
            db.session.commit()
            flash('Timeline item deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting timeline item: {str(e)}', 'error')
        return redirect(url_for('admin'))
    
    @app.route('/admin/timeline/<int:id>/toggle', methods=['POST'])
    def admin_timeline_toggle(id):
        timeline_item = TimelineItem.query.get_or_404(id)
        timeline_item.is_active = not timeline_item.is_active
        db.session.commit()
        return jsonify({'success': True, 'is_active': timeline_item.is_active})
    
    # Resume admin routes
    @app.route('/admin/resume/upload', methods=['GET', 'POST'])
    def admin_resume_upload():
        if request.method == 'POST':
            if 'resume' not in request.files:
                flash('No file selected', 'error')
                return redirect(request.url)
            
            file = request.files['resume']
            if file.filename == '':
                flash('No file selected', 'error')
                return redirect(request.url)
            
            if file and file.filename.lower().endswith('.pdf'):
                # Backup old resume
                if os.path.exists('Xie_Data_Resume.pdf'):
                    import datetime
                    backup_name = f"Xie_Data_Resume_backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                    os.rename('Xie_Data_Resume.pdf', backup_name)
                
                # Save new resume
                file.save('Xie_Data_Resume.pdf')
                flash('Resume uploaded successfully!', 'success')
                return redirect(url_for('admin'))
            else:
                flash('Please upload a PDF file', 'error')
        
        return render_template('admin_resume_upload.html')

    # Message management routes
    @app.route('/admin/message/<int:id>/mark-read', methods=['POST'])
    def admin_message_mark_read(id):
        message = ContactMessage.query.get_or_404(id)
        message.is_read = True
        
        # Log activity
        activity = ActivityLog(
            action='message_read',
            description=f'Marked message from {message.name} as read'
        )
        db.session.add(activity)
        db.session.commit()
        
        return jsonify({'success': True})
    
    @app.route('/admin/message/<int:id>/reply', methods=['POST'])
    def admin_message_reply(id):
        message = ContactMessage.query.get_or_404(id)
        message.is_replied = True
        message.is_read = True
        
        # Log activity
        activity = ActivityLog(
            action='message_replied',
            description=f'Replied to message from {message.name} ({message.email})'
        )
        db.session.add(activity)
        db.session.commit()
        
        return jsonify({'success': True})
    
    @app.route('/admin/message/<int:id>/delete', methods=['POST'])
    def admin_message_delete(id):
        message = ContactMessage.query.get_or_404(id)
        
        # Log activity
        activity = ActivityLog(
            action='message_deleted',
            description=f'Deleted message from {message.name} ({message.email}): {message.subject}'
        )
        db.session.add(activity)
        db.session.delete(message)
        db.session.commit()
        
        return jsonify({'success': True})

    return app

# This is the entry point for Gunicorn, which Render will use
app = create_app()

if __name__ == '__main__':
    import os
    # Enable debug mode for local development
    os.environ.setdefault('FLASK_DEBUG', 'True')
    app.run(host='0.0.0.0', port=5005, debug=True)