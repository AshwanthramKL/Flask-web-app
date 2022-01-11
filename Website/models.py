# Used to create the database models.  

from datetime import timezone
from . import db # import db from current package
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now()) # func.now() stores the current date automatically when called
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Associating/Linking notes with our users. user is in lowercase because SQL follows a different convention.
    # foreign-key is a Column in your database that always references a Column on another database. 


class User(db.Model, UserMixin): #inheritance
# A database model is like a layout or a blueprint for the databse.
    
    id = db.Column(db.Integer, primary_key = True) # primary key is a unique identifier that represents our object
    email = db.Column(db.String(1500), unique = True) # every email is unique
    password = db.Column(db.String(1500))
    first_name = db.Column(db.String(1500))
    notes = db.relationship('Note') # Store all of the users notes
  
