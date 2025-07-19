from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[Length(max=200)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Send Message')

class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired(), Length(max=100)])
    short_description = StringField('Short Description', validators=[Length(max=200)])
    description = TextAreaField('Description', validators=[DataRequired()])
    image_url = StringField('Image URL', validators=[Length(max=200)])
    demo_url = StringField('Demo URL', validators=[Length(max=200)])
    github_url = StringField('GitHub URL', validators=[Length(max=200)])
    technologies = StringField('Technologies (comma-separated)', validators=[Length(max=300)])
    featured = BooleanField('Featured Project')
    order_index = IntegerField('Order Index', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Save Project')

class ExperienceForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired(), Length(max=100)])
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    company_url = StringField('Company URL', validators=[Length(max=200)])
    company_logo = StringField('Company Logo URL', validators=[Length(max=200)])
    location = StringField('Location', validators=[Length(max=100)])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[Optional()])
    description = TextAreaField('Description')
    experience_type = SelectField('Type', choices=[('work', 'Work'), ('education', 'Education'), ('volunteer', 'Volunteer')])
    order_index = IntegerField('Order Index', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Save Experience')

class SkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired(), Length(max=50)])
    category = SelectField('Category', choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('languages', 'Languages'),
        ('other', 'Other')
    ])
    proficiency = IntegerField('Proficiency (0-100)', validators=[NumberRange(min=0, max=100)])
    icon_class = StringField('Icon Class (Font Awesome)', validators=[Length(max=50)])
    order_index = IntegerField('Order Index', validators=[Optional(), NumberRange(min=0)])
    submit = SubmitField('Save Skill') 