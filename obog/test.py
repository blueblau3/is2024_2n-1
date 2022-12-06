from flask import Flask
from obog import app

@app.route('/')
def index():
    return "Hello world!!"