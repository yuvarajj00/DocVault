from flask import Flask, request, render_template, url_for,flash,redirect,session
import requests
from  werkzeug.security import generate_password_hash
import pyrebase

app = Flask(__name__)

# Firebase configuration
Config = {
    "apiKey": "AIzaSyB6Ey-wlu-9xgOqn2CPEP6myZMKcUjOXFM",
    "authDomain": "pbl-project-3ef8d.firebaseapp.com",
    "projectId": "pbl-project-3ef8d",
    "storageBucket": "pbl-project-3ef8d.appspot.com",
    "messagingSenderId": "873183429790",
    "appId": "1:873183429790:web:4eb49025fb7e43b876278f",
    "measurementId": "G-FVXBQJGMZS",
    "databaseURL": "https://pbl-project-3ef8d-default-rtdb.firebaseio.com/"
}

# Initialize the app with the configuration
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app.secret_key = '999'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            return redirect(url_for('signup'))

        try:
            try:

                users = db.child("users").get()
                email_exists = any(user.val()['email'] == email for user in users.each())

                if email_exists:
                    print('Email is already registered!')
                    return redirect(url_for('signup'))
            except Exception as e:
                print("error")
                
            
            user_data = {
                "name": name,
                "email": email,
                "password": password,
                "private_key" : 0
            }
            db.child("users").push(user_data)
            return redirect(url_for('login'))

        except Exception as e:
            return redirect(url_for('signup'))

    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            # Check if the email and password match
            users = db.child("users").get()
            user_found = False
            for user in users.each():
                user_data = user.val()
                if user_data['email'] == email and user_data['password'] == password:
                    user_found = True
                    # Optionally, store user data in session
                    session['user'] = user_data['name']
                    break
                
            if user_found:
                return render_template('user.html' , name = session['user'])
            else:
                flash('Invalid email or password. Please try again.')
                return redirect(url_for('login'))

        except Exception as e:
            flash('An error occurred while processing your request. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/userpage')
def user():
    return render_template('user.html')

@app.route('/addFile')
def add_file():
    return render_template('addFile.html')

if __name__ == '__main__':
    app.run(debug=True)
