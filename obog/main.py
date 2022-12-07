from tkinter import FIRST
from cmath import nan
from obog import app
from flask import render_template, request, redirect, url_for, flash, session
import sqlite3
import re
from datetime import datetime

DATABASE = 'obog/obogs.db'

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/register_form')
def form():
  return render_template(
    'register_form.html'
  )

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/new', methods=['POST'])
def new():
  # validation
  if request.form['name'] is None or request.form['email'] is None or request.form['prefecture'] is None or request.form['juniorhighschoolname'] is None or request.form['highschoolname'] is None or request.form['teaching_area'] is None or request.form['pr'] is None:
    flash("未入力の箇所があります")
    if len(request.form['pr']) => 250 and len(request.form['pr']) <= 50:
      flash("文字数が" + str(len(request.form['pr'])) + "です")
    else:
      return render_template(
        'register_form.html',
        name=request.form['name'],
        email=request.form['email'],
        prefecture=request.form['prefecture'],
        juniorhighschoolname=request.form['juniorhighschoolname'],
        highschoolname=request.form['highschoolname'],
        teaching_area=request.form['teaching_area'],
        pr=request.form['pr'],
      )
  else:
    # registration to db
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('insert into obogs (name, email, prefecture, juniorhighschoolname, highschoolname, teaching_area, pr) values (?, ?, ?, ?, ?, ?, ?)',
                [request.form['name'], request.form['email'], request.form['prefecture'],request.form['juniorhighschoolname'], request.form['highschoolname'], request.form['teaching_area'],request.form['pr']])
    con.commit()
    cur.close()
    con.close()
    flash("追加しました")

  return redirect('/')

#投稿一覧ページ(OB・OG一覧)
@app.route('/search')
def search():
  return render_template(
    'search.html'
  )