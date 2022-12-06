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
3.cd is2024_2n-1で移動<br>
4.必要に応じて仮想環境を立ち上げ(pyvenvとか？立てなくても良い)、`python3 -m pip install -r requirements.txt`を実行<br>
5.flaskの環境変数として`FLASK_APP=obog`、`FLASK_ENV=development`を設定(Powershellの場合は`./set_envconst`を実行するれば自動で設定される。PowerShellのスクリプトを実行できない場合は、管理者権限でPowerShellを起動し、`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`を先に実行する。command prompt、linuxの場合は、`set_envconst`を実行すれば自動で設定される。macはわからない。)<br>
6.`flask run`でサーバーを起動<br>
7.Google Chrome等で`localhost:5000`でアクセス。Hello world!!と出力されたら完了。<br>

### 参考URL
githubチーム開発マニュアル：https://qiita.com/siida36/items/880d92559af9bd245c34
gitコミット取消し方：https://qiita.com/shuntaro_tamura/items/06281261d893acf049ed

### Flaskエラー対応
`./set_envconst` でエラーが出たら以下を試してみてください。<br>
https://1130--hq.slack.com/archives/C04A2SWKWM7/p1670216740835959?thread_ts=1670101201.082309&cid=C04A2SWKWM7
