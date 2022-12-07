from flask import Flask
app = Flask(__name__)
app.secret_key='scsk2n-1'
import obog.main
from obog import obog_db

obog_db.create_obogs_table()