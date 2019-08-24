# このシリーズの目的
- PythonのフレームワークであるFlaskを使用してWebアプリに必要な機能の作成と解説をやります。
- 普段の勉強のアウトプットとして書いています。質問や指摘は大歓迎です。

# 今回の目標
- 『Hello World』をFlaskで出力してみよう！

## 環境準備

- python の ver 確認

```bash
$ python -V
Python 3.6.5
```

## フォルダ構成

```bash
$ tree
.
├── README.md
├── requirements.txt
└── src
    └── main.py
```

## flaskのインストール

<details><summary>requirements.txtって何？？</summary><div>

python は他の人が作成してくれたパッケージ（便利な機能の集まり）をインストールして使うことができます。    
その時に使用するのが`pip`と言うパッケージ管理ツールです。  
今回は、flaskと言うパッケージをインストールしています。  
ただ単純にインストールする場合は、以下のコマンドを実行すればいいのですが  

```bash
pip install flask
```

これだと、沢山のパッケージをインストールしたいときに毎回

```bash
pip install パッケージ①
pip install パッケージ②
pip install パッケージ③
pip install パッケージ④
```

と書かないといけません。

これだと大変面倒なので一括でインストールしたい。。。  
そこで、使用するのが`requirements.txt` です。  
テキスト形式で開発に必要なパッケージの一覧を保存できます。  
コマンド`pip install -r requirements.txt`を使用して一括インストールができます。

</div></details>


```requirements.txt
flask
```

```bash
$ pip install -r requirements.txt
Collecting flask (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl
Collecting itsdangerous>=0.24 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Werkzeug>=0.15 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl
Collecting click>=5.1 (from flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl
Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/f0/00/a6aea33f5598b080b86d6b6d1214b51afe3ffa6100b902d5aa465080083f/MarkupSafe-1.1.1-cp36-cp36m-macosx_10_6_intel.whl
Installing collected packages: itsdangerous, Werkzeug, MarkupSafe, Jinja2, click, flask
Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.4 click-7.0 flask-1.1.1 itsdangerous-1.1.0
```

インストール確認

```bash
$ pip list
Package      Version
------------ -------
Click        7.0
Flask        1.1.1
itsdangerous 1.1.0
Jinja2       2.10.1
MarkupSafe   1.1.1
pip          19.1.1
setuptools   39.0.1
Werkzeug     0.15.4
```

flaskを使用するのに必要なパッケージをpipが自動でインストールしてくれているので
flask以外のがインストールされていてもOK!

## ソース解説

```src/main.py

# インストールしたパッケージのインポート
from flask import Flask

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

# どこのアドレスで実行するか指定
# 今回は http://127.0.0.1:5000/ にアクセスされたらhello_worldを実行するよ
@app.route('/')
def hello_world():
    
    message = "Hello World"
    
    return message

if __name__ == '__main__':
    # 作成したappを起動
    # ここでflaskの起動が始まる
    app.run()
```

### ポイント
- `from flask import Flask`でインストールしたpythonのパッケージを使用できるようにしてる。
- `app = Flask(__name__)`でFlaskのインスタンスを作成している。
- `app.run()`でFlaskを起動。
- `@app.route('/')`以下でアクセスした際の動作を紐付けられる。(今回は`hello_world()`に紐付けている)
- `if __name__ == '__main__':`は、このファイルが起点としてプログラムが実行されているか判定している。



## flask の起動

```bash
$ python src/main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- 起動の確認

  - <http://127.0.0.1:5000/> にブラウザからアクセス


## アクセスした際の表示
|<img width="1920" alt="sample.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/76de53ee-f5c4-1225-5107-e10ca9712c71.png">|
|:-:|

## おまけ
僕の大好きなエディタVSCodeの[REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)を使用してもok。
|<img width="1920" alt="sample.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/76de53ee-f5c4-1225-5107-e10ca9712c71.png">|
|:-:|



## 参考
- [Flask User’s Guide](https://flask.palletsprojects.com/en/1.1.x/)
