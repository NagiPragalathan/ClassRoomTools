from flask import Flask
from .routes import notes

def create_app():
    
    app = Flask(__name__)
    
    #blueprints
    app.register_blueprint(notes)
    
    return app