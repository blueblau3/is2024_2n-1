from flask import Flask
app = Flask(__name__)
import obog.main
from obog import obog_db

obog_db.create_obogs_table()