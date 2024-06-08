#!/bin/env python3
from flask import Flask,Blueprint, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from routes.extensions import db
from routes.task_routes import task_bp

app = Flask(__name__)
auth_bp = Blueprint('auth', __name__)
 
app.config.from_object(Config)
db.init_app(app)
from models.user import User

cors = CORS(app)
jwt = JWTManager(app)

 ###############################################

@app.route('/register', methods=['GET', 'POST'])
def register():
   if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Create a new user instance
        new_user = User(username=username, email=email, password=password)

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
        # Redirect the user to the login page or any other desired page
        return redirect(url_for('login'))
    
    # Render the registration form
        return render_template('register.html') 
 
 ###############################################

# from routes.task_routes import task_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
# app.register_blueprint(task_bp, url_prefix='/api/tasks')

# Landing page loading 
@app.route('/')
def landing_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)