# Makes the website folder a package.  

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy() # database object
DB_NAME  = "database.db" 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Something_secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # This stores the database in the  website folder.'sqlite:///{DB_NAME}'
    # sql database is store at this location.  
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    from .models import User, Note
    # We import it to initialize the class
    create_database(app)

    login_manager  = LoginManager()
    login_manager.login_view = 'auth.login' # where we need to go if we're not logged-in
    login_manager.init_app(app) # telling login_manager which app we're using

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) 
        # telling flask how we load a user, get works similar to filterby except it looks for the primary key by default and checks if it's equal to the parameter we pass.
    return app


def create_database(app):
    if not path.exists('Website/'+ DB_NAME):
        db.create_all(app = app)
        print("Created database!")
    
