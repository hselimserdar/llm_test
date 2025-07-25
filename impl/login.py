from flask import Flask, render_template

def render_login():
    return render_template('login.html')

def login_auth():
    ...