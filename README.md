# is2024_2n-1

### clone

`git clone git@github.com:blueblau3/is2024_2n-1.git`

### github の使い方
1.branch を切る<br>
`git branch 新しいブランチ名(feature/自分の名前)`<br>
`git checkout 新しいブランチ名(feature/自分の名前)`<br>
2.編集をする<br>
3.`git add .`<br>
4.`git commit -m "commit名"`<br>
5.`git push -u origin branch名`<br>
6.Pull Request を出す<br>
7.conflict がなければ merge<br>
※conflict が出たとき、修正できるのであれば、修正後に merge<br>
8.merge したら、毎回`git pull origin main`で自分の環境を最新版にしてください<br>

### flaskサーバーの立て方
1.https://www.curict.com/item/60/60bfe0e.html などを参考にPCにGitをインストール、python3をインストール、pip3をインストール<br>
2.PowerShell等で任意のディレクトリに移動し、clone<br>
3.必要に応じて仮想環境を立ち上げ(pyvenvとか？立てなくても良い)、`python3 -m pip install -r requirements.txt`を実行→flaskの環境設定<br>
4.`python3 test.py`を実行(デバッグモードで実行。開発が進んだあと本文は更新予定)<br>
5.Google Chrome等で`localhost:5000`でアクセス。Hello world!!と出力されたら完了。<br>