# hello.py
# This file contains the main application code for a simple Flask app.

from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()
# Load environment variables
HOST = os.getenv('host', '127.0.0.1')
PORT = int(os.getenv('port', 5000))
DEBUG = os.getenv('debug', 'False').lower() == 'true'

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

@app.route("/chatbot/<int:SessionId>")
def chatbot_session(SessionId):
    return render_template('chatbot.html', session_id=SessionId)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)