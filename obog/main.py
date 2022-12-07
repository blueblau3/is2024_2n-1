from tkinter import FIRST
from cmath import nan
from obog import app
from flask import render_template, request, redirect, url_for, flash, session
import sqlite3
import re
from datetime import datetime

DATABASE = 'obog.db'


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

def is_str(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@app.route('/new', methods=['POST'])
def new():
  # validation
  if is_int(request.form['word_count'])==False:
    flash("文字数には半角で自然数を入力してください")
    return render_template(
      'register_form.html',
      company_name=request.form['company_name'],
      selection_kind=request.form['selection_kind'],
      question_genre_1=request.form['question_genre_1'],
      submitted_at=request.form['submitted_at'],
      word_count=request.form['word_count'],
      acceptance_status=request.form['acceptance_status'],
      abstract=request.form['abstract'],
      content=request.form['contents']
    )
  else:

      if int(request.form['word_count'])<=0:
        flash("文字数には半角で自然数を入力してください")
        return render_template(
          'register_form.html',
          company_name=request.form['company_name'],
          selection_kind=request.form['selection_kind'],
          question_genre_1=request.form['question_genre_1'],
          submitted_at=request.form['submitted_at'],
          word_count=request.form['word_count'],
          acceptance_status=request.form['acceptance_status'],
          abstract=request.form['abstract'],
          content=request.form['contents']
        )

      # registration to db
      con = sqlite3.connect(DATABASE)
      con.execute('insert into entry_sheets (company_name, selection_kind, question_genre_1, word_count, updated_at, submitted_at,acceptance_status, abstract, content) values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  [request.form['company_name'], request.form['selection_kind'], request.form['question_genre_1'],request.form['word_count'], str(datetime.now())[:19], request.form['submitted_at'], request.form['acceptance_status'],request.form['abstract'], request.form['contents']])
      con.commit()
      con.close()
      flash("追加しました")

  return redirect(url_for('index'))


@app.route('/edit/<int:id>')
def edit(id):
  
  con = sqlite3.connect(DATABASE)
  record = con.execute('select * from entry_sheets where id=?', [id]).fetchall()[0]
  con.close()

  entry_sheet = {
      "id":record[0],
      "company_name":record[1],
      "selection_kind":record[2],
      "question_genre_1":record[3],
      "question_genre_2":record[4],
      "question_genre_3":record[5],
      "word_count":record[6],
      "updated_at":record[7],
      "submitted_at":record[8],
      "abstract":record[9],
      "content":record[10],
      "acceptance_status":record[11],
  }

  return render_template(
    'edit.html',
    entry_sheet = entry_sheet,
  )


@app.route('/update/<int:id>', methods=['POST'])
def update(id):

  if is_int(request.form['word_count'])==False:
    flash("文字数には半角で自然数を入力してください")

    entry_sheet = {
      "id":id,
      "company_name":request.form['company_name'],
      "selection_kind":request.form['selection_kind'],
      "question_genre_1":request.form['question_genre_1'],
      "word_count":request.form['word_count'],
      "updated_at":str(datetime.now())[:19],
      "submitted_at":request.form['submitted_at'],
      "abstract":request.form['abstract'],
      "content":request.form['content'],
      "acceptance_status":request.form['acceptance_status'],
    }
    return render_template(
      'edit.html',
      entry_sheet = entry_sheet,
    )
  else:

      if int(request.form['word_count'])<=0:
        flash("文字数には半角で自然数を入力してください")

        entry_sheet = {
          "id":id,
          "company_name":request.form['company_name'],
          "selection_kind":request.form['selection_kind'],
          "question_genre_1":request.form['question_genre_1'],
          "word_count":request.form['word_count'],
          "updated_at":str(datetime.now())[:19],
          "submitted_at":request.form['submitted_at'],
          "abstract":request.form['abstract'],
          "content":request.form['content'],
          "acceptance_status":request.form['acceptance_status'],
        }
        return render_template(
          'edit.html',
          entry_sheet = entry_sheet,
        )

  con = sqlite3.connect(DATABASE)
  con.execute('update entry_sheets set company_name=?, selection_kind=?, \
      question_genre_1=?, word_count=?, updated_at=?, submitted_at=?, abstract=?,\
      content=?, acceptance_status=? where id=?',[request.form['company_name'], request.form['selection_kind'],
              request.form['question_genre_1'], request.form['word_count'], str(datetime.now())[:19], request.form['submitted_at'],
              request.form['abstract'], request.form['content'], request.form['acceptance_status'], id])
  con.commit()
  con.close()
  flash("変更しました")

  return redirect('/')


@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
  con = sqlite3.connect(DATABASE)
  con.execute('delete from entry_sheets where id=?',[id])
  con.commit()
  con.close()
  flash("削除しました")

  return redirect('/')


@app.route('/search/', methods = ["POST", "GET"])
def search():
  #プルダウンに表示する値を取得する。追記はここで行う
  columns = ["company_name","selection_kind", "acceptance_status","question_genre_1"]
  column_names = ["企業名","選考種別","選考状況","質問"]
  FIRST_SENTENSE = "選択してください"
  column_infos = []

  #プルダウンに表示したいデータ名の取得
  entry_sheets = {}
  for column in columns:
    entry_sheets[column] = remove_duplicate(column)
 

  #GETならプルダウン表示用データと検索結果用データに全てを表示
  if request.method == "GET":
    con = sqlite3.connect(DATABASE)
    records = con.execute("SELECT * FROM entry_sheets").fetchall()
    con.close()

    results = get_database_dict(records)
    conditions = [FIRST_SENTENSE] * len(columns)

    #プルダウンに表示する情報をcolumn_infosに一括管理
    for column , column_name, condition  in zip(columns,column_names,conditions):
      column_infos.append((column, column + "_select", column_name, condition))
    
    return render_template(
      'search.html',
      column_infos = column_infos,
      entry_sheets = entry_sheets,
      results = results,
      )

  #----#

  #POSTならプルダウンで入力された条件に合ったデータをresultsに格納して送る
  elif request.method == "POST":

    #ANDまたはOR検索で取得情報を変更
    th = request.form["and_or_select"] #論理演算
    if th == "OR":
      con = sqlite3.connect(DATABASE)
      records = con.execute(f"SELECT * FROM entry_sheets WHERE company_name = ? {th} selection_kind = ? {th} acceptance_status = ? {th} question_genre_1 = ?",
      [request.form["company_name_select"], request.form["selection_kind_select"], request.form["acceptance_status_select"], request.form["question_genre_1_select"]]).fetchall()
      con.close()

    #AND検索の場合
    if th == "AND":
      selected_condition = {} #選択された条件だけを取得
      sql_sentences = ""
      for key, value in request.form.items():
        if key != "and_or_select":
          if value != FIRST_SENTENSE:
            key = key.removesuffix('_select')
            selected_condition[key] = value
            sql_sentences += f" {key} = '{value}' {th}"
      sql_sentences = sql_sentences.removesuffix(th)
      con = sqlite3.connect(DATABASE)
      sen = f"SELECT * FROM entry_sheets WHERE{sql_sentences}"
      if sql_sentences != "":
        records = con.execute(sen).fetchall()
      else:
        records = []
      con.close()


    results = results = get_database_dict(records)
    conditions = request.form.values()

    #プルダウンに表示する情報をcolumn_infosに一括管理
    for column , column_name, condition  in zip(columns,column_names,conditions):
      #First Sentenceでなければ、プルダウン下にFirstSentenseを追加
      if condition != FIRST_SENTENSE:
        entry_sheets[column].remove(condition)
        entry_sheets[column].append(FIRST_SENTENSE)
      column_infos.append((column, column + "_select", column_name, condition))
      
    
    return render_template(
      'search.html',
      column_infos = column_infos,
      entry_sheets = entry_sheets,
      results = results,
      th = th
      )

def get_database_dict(records):
  results = []
  for record in records:
    results.append(
      {
        "id": record[0],
      "company_name": record[1],
      "selection_kind": record[2],
      "question_genre_1": record[3],
      "question_genre_2": record[4],
      "question_genre_3": record[5],
      "word_count": record[6],
      "updated_at": record[7],
      "submitted_at": record[8],
      "abstract": record[9],
      "content": record[10],
      "acceptance_status": record[11]
      }
      )
  return results

#重複とNoneを持つrecordは追加しない削除
def remove_duplicate(column_name):
  con = sqlite3.connect(DATABASE)
  records = con.execute(f"SELECT DISTINCT {column_name} FROM entry_sheets").fetchall()
  output = []
  for record in records:
    if record[0] != None:
      output.append(record[0])
  return output



@app.route('/detail/<int:id>')
def detail(id):
  con = sqlite3.connect(DATABASE)
  record = con.execute('select * from entry_sheets where id=?', [id]).fetchall()[0]
  con.commit()
  con.close()

  record_dict = {
        "id": record[0],
        "company_name": record[1],
        "selection_kind": record[2],
        "question_genre_1": record[3],
        "question_genre_2": record[4],
        "question_genre_3": record[5],
        "word_count": record[6],
        "updated_at": record[7],
        "submitted_at": record[8],
        "abstract": record[9],
        "content": record[10],
        "acceptance_status": record[11]
      }

  return render_template(
    'detail.html',
    entry_sheet = record_dict,
    )
