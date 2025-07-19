from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from app.models import Project, Experience, Skill, ContactMessage, SiteSettings

class ProjectAdmin(ModelView):
    column_list = ['title', 'short_description', 'featured', 'technologies', 'created_at']
    column_searchable_list = ['title', 'description', 'technologies']
    column_filters = ['featured', 'created_at']
    form_excluded_columns = ['created_at']
    column_editable_list = ['featured', 'order_index']
    column_default_sort = ('order_index', False)

class ExperienceAdmin(ModelView):
    column_list = ['title', 'company', 'start_date', 'end_date', 'experience_type']
    column_searchable_list = ['title', 'company', 'description']
    column_filters = ['experience_type', 'start_date']
    column_default_sort = ('start_date', True)
    
    def scaffold_form(self):
        form_class = super().scaffold_form()
        # Custom form modifications if needed
        return form_class

class SkillAdmin(ModelView):
    column_list = ['name', 'category', 'proficiency', 'order_index']
    column_searchable_list = ['name', 'category']
    column_filters = ['category']
    column_editable_list = ['proficiency', 'order_index']
    column_default_sort = [('category', False), ('order_index', False)]

class ContactMessageAdmin(ModelView):
    column_list = ['name', 'email', 'subject', 'created_at', 'read']
    column_searchable_list = ['name', 'email', 'subject', 'message']
    column_filters = ['read', 'created_at']
    column_editable_list = ['read']
    column_default_sort = ('created_at', True)
    can_create = False  # Only allow reading and updating
    can_delete = True

class SiteSettingsAdmin(ModelView):
    column_list = ['key', 'value']
    column_searchable_list = ['key', 'value']
    form_columns = ['key', 'value']
    
    def scaffold_form(self):
        form_class = super().scaffold_form()
        # Make value field a text area
        form_class.value.kwargs['widget'] = lambda field, **kwargs: f'<textarea name="{field.name}" class="form-control">{field.data or ""}</textarea>'
        return form_class

class DashboardView(BaseView):
    @expose('/')
    def index(self):
        # Get some stats
        project_count = Project.query.count()
        experience_count = Experience.query.count()
        skill_count = Skill.query.count()
        unread_messages = ContactMessage.query.filter_by(read=False).count()
        
        return self.render('admin/dashboard.html',
                         project_count=project_count,
                         experience_count=experience_count,
                         skill_count=skill_count,
                         unread_messages=unread_messages)

def setup_admin(admin_instance, db):
    """Setup admin interface"""
    # Add dashboard
    admin_instance.add_view(DashboardView(name='Dashboard', endpoint='dashboard'))
    
    # Add model views
    admin_instance.add_view(ProjectAdmin(Project, db.session, name='Projects'))
    admin_instance.add_view(ExperienceAdmin(Experience, db.session, name='Experience'))
    admin_instance.add_view(SkillAdmin(Skill, db.session, name='Skills'))
    admin_instance.add_view(ContactMessageAdmin(ContactMessage, db.session, name='Messages'))
    admin_instance.add_view(SiteSettingsAdmin(SiteSettings, db.session, name='Site Settings')) 