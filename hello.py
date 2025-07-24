# hello.py
# This file contains the main application code for a simple Flask app.

from flask import Flask
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
    return "<p>Welcome to the Gemini chatbot!</p>"
@app.route("/login")
def login():
    return "<p>Please log in to continue.</p>"
@app.route("/register")
def register():
    return "<p>Please register to continue.</p>"
@app.route("/chatbot")
def chatbot():
    return "<p>You can start chat by typing your message!</p>"

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)