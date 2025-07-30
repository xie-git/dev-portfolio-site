#!/usr/bin/env python3
"""
Database migration script to add ContactMessage and ActivityLog tables
"""

from app import create_app, db, ContactMessage, ActivityLog

def migrate_database():
    """Add the new ContactMessage and ActivityLog tables."""
    app = create_app()
    
    with app.app_context():
        try:
            # Create the new tables
            print("Creating ContactMessage and ActivityLog tables...")
            
            # Use SQLAlchemy to create all tables
            db.create_all()
            
            db.session.commit()
            print("Successfully created ContactMessage and ActivityLog tables!")
            
            # Add a welcome activity log entry
            welcome_activity = ActivityLog(
                action='system_initialized',
                description='Contact messages and activity logging system initialized'
            )
            db.session.add(welcome_activity)
            db.session.commit()
            print("Added welcome activity log entry!")
            
        except Exception as e:
            print(f"Migration failed: {e}")
            db.session.rollback()
            raise

if __name__ == '__main__':
    migrate_database()