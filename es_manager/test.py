from flask import Flask
from es_manager import app

@app.route('/')
def index():
    return "Hello world!!"

#if __name__ == "__main__":
#    app.run(debug=True)