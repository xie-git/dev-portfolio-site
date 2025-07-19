from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, current_app
from flask_mail import Message
from app import db, mail
from app.models import Project, Experience, Skill, ContactMessage, SiteSettings
from app.forms import ContactForm
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Get featured projects
    featured_projects = Project.query.filter_by(featured=True).order_by(Project.order_index).limit(6).all()
    
    # Get all projects if no featured ones
    if not featured_projects:
        featured_projects = Project.query.order_by(Project.order_index).limit(6).all()
    
    # Get experience timeline
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    
    # Get skills by category
    skills = Skill.query.order_by(Skill.category, Skill.order_index).all()
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    # Get site settings
    hero_title = SiteSettings.get_setting('hero_title', 'Software Developer')
    hero_subtitle = SiteSettings.get_setting('hero_subtitle', 'Building amazing digital experiences')
    about_text = SiteSettings.get_setting('about_text', 'Passionate developer with experience in modern web technologies.')
    
    return render_template('index.html',
                         projects=featured_projects,
                         experiences=experiences,
                         skills_by_category=skills_by_category,
                         hero_title=hero_title,
                         hero_subtitle=hero_subtitle,
                         about_text=about_text)

@main.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    # Get related projects (same technologies)
    if project.technologies:
        tech_list = project.get_tech_list()
        related_projects = []
        for tech in tech_list[:2]:  # Check first 2 technologies
            related = Project.query.filter(
                Project.id != project.id,
                Project.technologies.contains(tech)
            ).limit(3).all()
            related_projects.extend(related)
        
        # Remove duplicates and limit to 3
        seen = set()
        related_projects = [p for p in related_projects if not (p.id in seen or seen.add(p.id))][:3]
    else:
        related_projects = []
    
    return render_template('project_detail.html', project=project, related_projects=related_projects)

@main.route('/portfolio')
def portfolio():
    # Get all projects grouped by category or technology
    page = request.args.get('page', 1, type=int)
    per_page = 9
    
    # Filter by technology if specified
    tech_filter = request.args.get('tech')
    if tech_filter:
        projects = Project.query.filter(Project.technologies.contains(tech_filter))
    else:
        projects = Project.query
    
    projects = projects.order_by(Project.featured.desc(), Project.order_index).paginate(
        page=page, per_page=per_page, error_out=False)
    
    # Get all unique technologies for filter
    all_projects = Project.query.all()
    all_techs = set()
    for project in all_projects:
        all_techs.update(project.get_tech_list())
    
    return render_template('portfolio.html', projects=projects, all_techs=sorted(all_techs), current_tech=tech_filter)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        # Save message to database
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        
        # Send email notification
        try:
            msg = Message(
                subject=f"Portfolio Contact: {form.subject.data or 'New Message'}",
                sender=current_app.config['MAIL_USERNAME'],
                recipients=[current_app.config['ADMIN_EMAIL']],
                body=f"""
New contact form submission:

Name: {form.name.data}
Email: {form.email.data}
Subject: {form.subject.data}

Message:
{form.message.data}
                """
            )
            mail.send(msg)
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
        except Exception as e:
            flash('Message saved, but email notification failed. I\'ll still see your message!', 'warning')
        
        return redirect(url_for('main.contact'))
    
    return render_template('contact.html', form=form)

@main.route('/api/projects')
def api_projects():
    """API endpoint for projects (for potential AJAX loading)"""
    projects = Project.query.order_by(Project.featured.desc(), Project.order_index).all()
    return jsonify([{
        'id': p.id,
        'title': p.title,
        'short_description': p.short_description,
        'image_url': p.image_url,
        'demo_url': p.demo_url,
        'github_url': p.github_url,
        'technologies': p.get_tech_list(),
        'featured': p.featured
    } for p in projects])

@main.route('/resume')
def resume():
    """Resume page or redirect to PDF"""
    resume_url = SiteSettings.get_setting('resume_url')
    if resume_url:
        return redirect(resume_url)
    
    # Otherwise render a resume page
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    skills = Skill.query.order_by(Skill.category, Skill.proficiency.desc()).all()
    
    return render_template('resume.html', experiences=experiences, skills=skills)

@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500 