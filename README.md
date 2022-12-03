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
1.https://www.curict.com/item/60/60bfe0e.html などを参考にPCにGit、python3、pip3をインストール<br>
2.githubの使い方を参考にローカルのブランチにcdコマンドで移動する<br>
3.必要に応じて仮装環境を立ち上げ、`python3 -m pip install -r requirements.txt`を実行<br>
4.flaskの環境変数として`FLASK_APP=es_manager、FLASK_ENV=development`を設定(Powershellの場合は`./set_envconst`を実行すれば自動で設定される。PowerShellのスクリプトを実行できない場合は、管理者権限でPowerShellを起動し、`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`を先に実行する。command prompt、linuxの場合は、`set_envconst`を実行すれば自動で設定される。)　もし実行できない場合は、「Windows 環境変数」等で調べ環境設定を行ってください。<br>
5.`flask run`でサーバーを起動<br>
6.`localhost:5000`にアクセス