# 目的

- 非同期通信でflaskに問い合わせをしてみよう

# 本編

### 前回まで
chapter_005参照

前回まではnginxを使用して静的コンテンツの分離を行ってみました。
今回はJavaScriptを使用して、Webサーバ（flask）にアクセスしてみましょう。

### フォルダ構成

```bash
.
├── README.md
├── client
│   ├── css
│   │   └── index.css
│   ├── html
│   │   └── index.html
│   └── js
│       └── index.js
├── docker-compose.yml
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
├── postgresql
│   └── init
│       ├── 1_create_db.sql
│       └── 2_create_table.sh
├── requirements.txt
├── src
│   ├── UserModel.py
│   ├── main.py
│   └── setting.py
└── test.http
```

### イメージ図

![flask.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/246efd72-91b2-9b00-03fa-ff501e3f38ce.png)

投稿数が多くなってきたので、一旦整理してみます。

まず、サーバは全部で３つあります。

* nginx ・・・ htmlやcssなどの静的コンテンツの置き場所 
* Flask ・・・ アプリケーションのCRUD処理を担当（データの保存や読み込み）
* PostgreSQL  ・・・  DBとして使用

FlaskとPostgreSQLの繋ぎ役は`SQLAlchmy`にお願いしています。
今回の記事では、NginxとFlaskとの繋ぎ役の部分を`JavaScript`で実装していきます。

### Flaskの準備

Flask側の準備からしていきましょう。
処理は簡単に、登録と取得の処理を実装します。
単純に、登録と取得の結果を返しているのみです。

```Python
from flask import Flask, request
from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
# 登録処理
@app.route('/', methods=["POST"])
def register_record():

    name = request.form['name']

    session.add(User(name))

    session.commit()

    message = name + "の登録が完了しました！"

    return message

# 取得処理
@app.route('/', methods=["GET"])
def fetch_record():

    name = request.args.get('name')

    db_user = session.query(User.name).\
        filter(User.name == name).\
        all()

    if len(db_user) == 0:
        message = "は登録されていません。"
    else:
        message = "は登録されています。"

    return name + message

if __name__ == '__main__':
    app.run()

```

### 非同期通信の準備（JavaScript）

次にJavaScriptでの非同期通信の実装を行います。

最初にボタン押下時の関数（`check`と`register`）をそれぞれセットしています。

ここでのポイントは`XMLHttpRequest`オブジェクトです。

このオブジェクトは簡単に言うと非同期通を実現させる為に使用しています。

非同期通信を行うことで、ページ全体を再読み込みさせることなく部分的に更新させることが可能になります。

身近な例だとGoogleMapとかがそうです。

拡大や縮小をする度に、ページ全体が更新されてたら検索しにくいですよね？？

下記の記事で詳しく説明してくれています。

https://qiita.com/hisamura333/items/e3ea6ae549eb09b7efb9

https://developer.mozilla.org/ja/docs/Web/API/XMLHttpRequest


```JavaScript
document.getElementById('check').onclick = function () {
    check();
}

document.getElementById('register').onclick = function () {
    register();
}


function check() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('message').innerText = this.responseText;
        }
    };
    const user_name = document.getElementById('user_name').value;
    // ここのURLはFlask起動時に表示されるURLにすること
    xhttp.open("GET", `http://127.0.0.1:5000/?name=${user_name}`, true);
    xhttp.send();
}

function register() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('message').innerText = this.responseText;
        }
    };
    const user_name = document.getElementById('user_name').value;
    xhttp.open("POST", "http://127.0.0.1:5000/", true);
    // POSTはURLにパラメータを載せないので、以下のようにやるよ
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(`name=${user_name}`);
}
```

### 動作確認
ここまで準備ができたら

docker-compose up -dでコンテナを立ち上げて

falskも起動して、動作を確認してみよう

ブラウザ上から
http://localhost/
にアクセス

# 次回

- flaskをコンテナ化してみよう（uwsgiの利用）
