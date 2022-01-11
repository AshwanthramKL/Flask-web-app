# Responsible for the authentication part of the website

from flask import Blueprint, render_template, request, flash,redirect,url_for
# flash - used for message flashing
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash 
# Importing to hash a password 
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__) 

@auth.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first() # filtering the database.

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category="success")
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password.', category="error")

        else:
            flash("Email does not exist.", category='error')

    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required # specifies that we cannot access this page unless the user is logged-in.
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/sign-up", methods = ["GET", "POST"])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()

        if user:
            flash("User already exits!", category='error')
        elif len(email) < 4:
            flash("Email too short", category="error")
        elif len(first_name) < 2:
            flash("First Name too short", category="error")
        elif len(password1) < 7:
            flash("Password must be atleast 7 characters", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        
        else:
            # add user to the data base.
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # loggin the the user in
            login_user(user, remember=True)
            flash("Account created successfully.", category='success')
            #Now we redirect the user to the home page using redirect() and url_for()
            return redirect(url_for('views.home')) # views - name of the blueprint, home - name of the function.

            
    return render_template("sign_up.html", user = current_user)
