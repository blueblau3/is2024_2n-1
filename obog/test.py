from flask import Flask
from obog import app

@app.route('/')
def index():
    return "Hello world!!"

#if __name__ == "__main__":
#    app.run(debug=True)