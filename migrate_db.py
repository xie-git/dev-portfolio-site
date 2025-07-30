#!/usr/bin/env python3
"""
Migrate database to add github_url column to existing projects
"""

from app import create_app, db

def migrate_database():
    app = create_app()
    with app.app_context():
        # Check if github_url column exists
        inspector = db.inspect(db.engine)
        columns = [column['name'] for column in inspector.get_columns('project')]
        
        if 'github_url' not in columns:
            print("Adding github_url column to project table...")
            with db.engine.connect() as conn:
                conn.execute(db.text('ALTER TABLE project ADD COLUMN github_url VARCHAR(500)'))
                conn.commit()
            print("Migration completed successfully!")
        else:
            print("github_url column already exists.")

if __name__ == '__main__':
    migrate_database()