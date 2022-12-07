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

  elif len(request.form['pr']) >= 250 or len(request.form['pr']) <= 10:
    flash("文字数が" + str(len(request.form['pr'])) + "です")
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
@app.route('/search/')
def search():
  con = sqlite3.connect(DATABASE)
  records = con.execute("SELECT * FROM obogs").fetchall()
  con.close()
  results = get_database_dict(records)
  return render_template(
    'search.html',
    results = results
  )

def get_database_dict(records):
  results = []
  for record in records:
    results.append(
      {
      "id": record[0],
      "name": record[1],
      "email": record[2],
      "prefecture": record[3],
      "juniorhighschoolname": record[4],
      "highschoolname": record[5],
      "teaching_area": record[6],
      "pr": record[7]
      }
      )
  return results

@app.route("/search_result",methods = ["POST"])
def search_detail():

  con = sqlite3.connect(DATABASE)
  search_prefecture  = "%"+request.form["Prefecture"]+"%"
  search_jhschool  = "%"+request.form["JHschool"]+"%"
  search_hschool  = "%"+request.form["Hschool"]+"%"
  search_teach  = "%"+request.form["Teach"]+"%"
  records = con.execute("SELECT * FROM obogs where prefecture like ? and juniorhighschoolname like ? and highschoolname like ? and teaching_area like ?",(search_prefecture,search_jhschool,search_hschool,search_teach,)).fetchall()
  con.close()
  results = get_database_dict(records)
  
  if results ==[]:
    print("該当なし")
    return redirect(url_for("search"))
  else:
    return render_template("search.html",results = results)