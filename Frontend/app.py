from flask import Flask, render_template, request, flash, redirect, url_for,session
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = 'itsme'  # Replace with a secure secret key

client = MongoClient('mongodb://localhost:27017/')
db = client['Resumer-parser']  # Replace with your MongoDB database name
users = db['users']

@app.route('/')
def registration():
    return render_template('registration.html')

@app.route('/index2')  # Define the endpoint for index2.html
def index2():
    return render_template('index2.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(email)

        try:
            # Check if the email is already registered
            if users.find_one({'email': email}):
                flash('Email is already registered. Please Login.', 'danger')
                return redirect(url_for("login"))
            else:
                # Hash the password before storing it
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                user_data = {'username': username, 'email': email, 'password': hashed_password}
                users.insert_one(user_data)
                flash('Account created successfully.', 'success')
                return redirect(url_for('login'))
        except Exception as e:
            flash(f'Registration error: {str(e)}', 'danger')
            return redirect(url_for('registration'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users.find_one({'email': email})

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            flash('Login successful!', 'success')
            return redirect(url_for('index2'))
            # Successful login - Implement your session management here
            
        else:
            flash('Login failed. Please check your email and password.', 'danger')
        return redirect(url_for('registration'))

if __name__ == '__main__':
    app.run(debug=True)
