# hello.py
# This file contains the main application code for a simple Flask app.

from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
# Load environment variables
HOST = os.getenv('host', '127.0.0.1')
PORT = os.getenv('port', 5000)
DEBUG = os.getenv('debug', False)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT, host=HOST)