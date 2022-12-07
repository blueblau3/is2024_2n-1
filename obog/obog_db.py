import sqlite3

DATABASE = 'obog/obogs.db'

#obogsテーブルの作成
def create_obogs_table():
    #databaseに接続(file名がなければそのファイルを作成する。)
    con = sqlite3.connect(DATABASE)
    #テーブル作成(カラムは8つ。slack参照。)
    con.execute("create table if not exists obogs \
        (id integer primary key autoincrement, \
        name text not null, \
        email text not null, \
        prefecture text not null, \
        juniorhighschoolname text not null, \
        highschoolname text not null, \
        teaching_area text not null, \
        pr text not null \
        )")
    #テーブルにコミット
    con.commit()

    #DB起動テスト用
    # con.execute("INSERT INTO obogs \
    # (name, email, prefecture, juniorhighschoolname, highschoolname, teaching_area, pr) \
    # values (?,?,?,?,?,?,?)",["kengo","aaa@gmail.com","hyogo","shiomi","kobe","badminton,tabletennis","This record is test."]
    # )
    # con.commit()
    #接続解除
    con.close()

#DB起動テスト用
#create_obogs_table()