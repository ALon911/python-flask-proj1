import os
import os.path

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    
    # Build DATABASE_URL from parts, fallback to DATABASE_URL env var or SQLite
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_NAME = os.environ.get('DB_NAME', 'flask_mvc_db')
    
    # If DATABASE_URL env var is set, use it; otherwise construct URL or fallback to SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}" if os.environ.get('DB_USER') else \
        f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
