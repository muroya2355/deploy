# ファイル構成
```
deploy
|
|--edited/
|--sounds/
|
|--app.py            # ソースコード (リネーム済)
|--model             # 学習済みモデル
|--Procfile          # アプリの実行方法
|--requirements.txt  # アプリの実行に必要なライブラリ
|--runtime.txt       # pythonのバージョン
```
[参考]https://yukituna.com/1146/
# ファイル内容

runtime.txt

* 最新の python バージョンだと動かないため、3.6.7まで下げたバージョンを指定
```
python-3.6.7
```

Procfile

* gunicorn ← Heroku にデプロイするためのモジュール

* app:app ← [ app.py の名前 ] : [ pyファイル中のアプリ名 ]
```
web: gunicorn app:app
```
requirements.txt

* 実行に必要なモジュールを指定する

* 巨大な torch ライブラリを全部 Heroku上でインポートすると、500MBのファイル容量を超えるため、軽量のCPU版をインポートする

* "cp36-cp36m" の 36 は python-3.6版という意味
```
Flask
gunicorn
numpy
http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-linux_x86_64.whl
```

app.py

* torch の変更に合わせて、ソースコードを修正する
```
device=torch.device('cpu')
net.load_state_dict(torch.load('./model',map_location=device))
```

* あと最後に追加、意味はよくわからない
```
if __name__ == "__main__":
    app.run(debug=True)
```

[参考]https://qiita.com/nori2711/items/615183fdc6858758d380

# デプロイ方法

https://yukituna.com/1146/ に沿って進める

* アプリケーションにアクセスするための URI と、ソースコード配置のための git リモートリポジトリを作成。

* その後、リモートにソースコードを push すると、勝手に Heroku 上でデプロイしてくれるらしい

## Heroku のアカウント登録

* Heroku のサイトからアカウント作成

* https://www.heroku.com/

* Heroku CLI をインストール

* https://devcenter.heroku.com/articles/heroku-cli
 → heroku-x64.exe

## 事前準備

* コマンドプロンプトを立ち上げ、deploy フォルダに移動

```
C:\Users\user\deploy>heroku login
heroku: Press any key to open up the browser to login or q to exit: → [ここでキーを入力]
heroku: Waiting for login... |
```
* ブラウザが立ち上がるので、ブラウザ上でログイン

* ログイン完了後、一応 gunicorn をインストール
```
> pip install gunicorn
```

* 事前に ↑ を見て requirements.txt、Procfile、runtime.txt　の用意

## 空アプリケーションの作成

* heroku の空アプリケーションを作成していく

* 注: アプリケーション名は他の人と被らないようにする (例:muroya2355-deploy)
```
> heroku create [appname]
```

* 作成完了後に個別のURI と、git のリモートリポジトリが割り当てられる
```
Creating ⬢ muroya2355-deploy... done
https://muroya2355-deploy.herokuapp.com/ | https://git.heroku.com/muroya2355-deploy.git
```
* URI にアクセスしてみる(https://muroya2355-deploy.herokuapp.com/)

* エラーが出なければ成功

## git リポジトリの作成、プッシュ

* deploy 内で git リポジトリを作成、コミット

```
> git init
> git add -A .
> git commit -m "first commit"
```
* リモート先 ("heroku") が既に割り当てられてるので、リモートにプッシュ
```
> git push heroku master
```
" [new branch]      master -> master " まで出てきたら成功

## デプロイの確認
* アプリケーションのログ出力先を開く

```
> heroku logs -t
```

* ログを開いたまま、再度 URI にアクセス　

* (https://muroya2355-deploy.herokuapp.com/)

* アプリを消したいときは Heroku のダッシュボードから

* (https://dashboard.heroku.com/apps)