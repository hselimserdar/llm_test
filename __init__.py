# hello.py
# This file contains the main application code for a simple Flask app.

from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import mysql.connector # Importing the MySQL connector for database operations
from impl.login import *  # Importing the login function from the login module

load_dotenv()
# Load environment variables
HOST = os.getenv('host', '127.0.0.1')
PORT = int(os.getenv('port', 5000))
DEBUG = os.getenv('debug', 'False').lower() == 'true'

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get pure form data
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Print the pure values for you to see
        print(f"Email: {email}")
        print(f"Password: {password}")
        
        # Your validation logic here
        # Example: if validate_user(email, password):
        #     return jsonify({'success': True, 'message': 'Login successful'})
        # else:
        #     return jsonify({'success': False, 'message': 'Invalid credentials'})
        
        # For now, basic validation - replace with your actual validation logic
        if email and password:  # Basic check - replace with your validation
            return jsonify({'success': True, 'message': 'Login successful'})
        else:
            return jsonify({'success': False, 'message': 'Please fill in all fields'})
        
    result = render_login()
    print(result)
    return result

@app.route("/api/login")
def login_api():
    return request.json

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get pure form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')
        
        # Print the pure values for you to see
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Repeat Password: {repeat_password}")
        
        # Your validation logic here
        # Example: if create_user(username, email, password, repeat_password):
        #     return jsonify({'success': True, 'message': 'Registration successful'})
        # else:
        #     return jsonify({'success': False, 'message': 'Registration failed'})
        
        # For now, basic validation - replace with your actual validation logic
        if username and email and password and repeat_password:  # Basic check
            if password == repeat_password:  # Password match check
                return jsonify({'success': True, 'message': 'Registration successful'})
            else:
                return jsonify({'success': False, 'message': 'Passwords do not match'})
        else:
            return jsonify({'success': False, 'message': 'Please fill in all fields'})
        
    return render_template('register.html')

@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

@app.route("/chatbot/<int:SessionId>")
def chatbot_session(SessionId):
    return render_template('chatbot.html', session_id=SessionId)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)
    print("test")