#!/usr/bin/env python3
"""
Simple Portfolio Website - Main Application File
"""

import os
from flask import Flask, render_template, send_from_directory, send_file, request, flash, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, EmailField, validators
from wtforms.validators import DataRequired, Email, Length
import secrets

# Contact form class for CSRF protection and validation
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    
    # Generate secure secret key for production
    app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    
    # Enable CSRF protection
    csrf = CSRFProtect(app)
    
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
        return render_template('index.html')
    
    @app.route('/Xie_Data_Resume.pdf')
    def resume():
        return send_file('Xie_Data_Resume.pdf', as_attachment=False)
    
    @app.route('/projects')
    def all_projects():
        return render_template('projects.html')

    @app.route('/resume')
    def resume_page():
        return render_template('resume.html')

    @app.route('/about')
    def about_page():
        return render_template('about.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            # In a real app, you'd process the form data here
            # For now, just flash a success message
            flash('Thank you for your message! I\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
        return render_template('contact.html', form=form)
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return app

# This is the entry point for Gunicorn, which Render will use
app = create_app()

if __name__ == '__main__':
    import os
    # Enable debug mode for local development
    os.environ.setdefault('FLASK_DEBUG', 'True')
    app.run(host='0.0.0.0', port=5000, debug=True)