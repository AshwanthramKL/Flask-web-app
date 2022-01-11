# Stores all the main views or the URL end points for the actual front-end aspect of the website.  

from flask import Blueprint,render_template, request, flash, jsonify
#render_template is used when we want to render a template function.
from flask.templating import _render
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
views = Blueprint('views',__name__)


@views.route('/', methods = ['GET','POST'])  # after creating the blueprints we need to register them in the init.py file
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Note too short!', category = 'error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category= 'success')

    return render_template("home.html", user = current_user)
    # current user means that we'll be able to reference our current user in our template and check if its authenticated.


@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data) # sent from the index.js file POST request, we must turn it into a python dictionary object
    noteId = note['noteId']
    note = Note.query.get(noteId) # search for the note that has that id
    if note: # check if the note exists
        if note.user_id == current_user.id: # check if the user owns that note
            db.session.delete(note) # delete the note
            db.session.commit()
            flash('Note deleted', category='success')

    return jsonify({}) # return an empty response, because we need to return something from the views
