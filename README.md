# このシリーズの目的
- PythonのフレームワークであるFlaskを使用してWebアプリに必要な機能の作成と解説をやります。
- 普段の勉強のアウトプットとして書いています。質問や指摘は大歓迎です。


# 今回の目標
- FlaskでHtmlを返してみよう
- ３種類のパラメータの受け取りかたを知ろう
  - urlの場合
  - getの場合
  - postの場合

## 環境準備

chapter_001ブランチ参照

## フォルダ構成

```bash
$ tree
.
├── README.md
├── form.html
├── requirements.txt
└── src
    ├── main.py
    └── templates
        └── hello.html
```

## 解説

<details><summary>そもそもGETとかPOSTって何だっけ？？</summary><div>

ものすごく、ざっくり言うと

GET : 他の人に見られても大丈夫なデータ（Amazonの商品検索とか）
POST : 他の人に見られるのは困るデータ（会員登録とか）

もっと詳しく知りたい場合は、以下を見てみるといいかも
[GETとPOSTの違いについて](https://qiita.com/kanataxa/items/522efb74421255f0e0a1)
[「GETメソッド」と「POSTメソッド」の違い](https://wa3.i-3-i.info/diff7method.html)
[Webを支える技術 -HTTP、URI、HTML、そしてREST (WEB+DB PRESS plus) ](https://www.amazon.co.jp/Web%E3%82%92%E6%94%AF%E3%81%88%E3%82%8B%E6%8A%80%E8%A1%93-HTTP%E3%80%81URI%E3%80%81HTML%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6REST-WEB-PRESS-plus/dp/4774142042)

</div></details>

```main.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<name>')
def hello_world(name):
    # urlから直接パラメータを受け取る
    return render_template("hello.html", name=name, method="URLパラメータ")

@app.route('/param', methods=["GET","POST"])
def hello_world_with_parameter():
    
    if request.method == 'POST':
        # postのパラメータの受け取る
        name = request.form['name']
    else:
        # getのパラメータの受け取る
        name = request.args.get('name')

    return render_template("hello.html", name=name, method=request.method)


if __name__ == '__main__':
    app.run()

```

### ポイント
- `render_template `でhtmlを [レンダリング](https://wa3.i-3-i.info/word1359.html) している。
- `request`でメソッドの判定やパラメータの受け取りを行う。
- `@app.route('/param', methods=["GET","POST"])`の`methods`でリクエストメソッドを絞れる。
- `render_template("hello.html", name=name, method=request.method)`でレンダリング時に使用するパラメータを渡している。

```hello.html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
    <p>こんにちは {{name}} さん</p>
    <p>このページは{{method}}で作られたよ。</p>
    </body>
</html>
```

### ポイント（hello.html）
- `{{パラメータ名}}`でパラメータを表している

## 動作確認

<details><summary>flask の起動</summary><div>

```bash
$ python src/main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

</div></details>

- Htmlの確認  
  - <http://127.0.0.1:5000/Tom> にブラウザからアクセス
  - `form.html`を使用して、テキストを送信してレンダリングされた`hello.html`を確認

## アクセスした際の表示
<http://127.0.0.1:5000/Tom>にブラウザからアクセス

|<img width="1919" alt="sample001.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/04fe7b36-454e-242a-e541-ab6ab15a16a2.png">|
|:-:|

`form.html`を使用して、テキストを送信  

<details><summary>form.html</summary><div>

```form.html
<!DOCTYPE html>
<html>
  <head> </head>
  <body>
    <form method="POST" action="http://127.0.0.1:5000/param">
      <div>
        <input name="name" />
      </div>
      <div>
        <button>POSTで送信</button>
      </div>
    </form>
    <form method="GET" action="http://127.0.0.1:5000/param">
      <div>
        <input name="name" />
      </div>
      <div>
        <button>GETで送信</button>
      </div>
    </form>
  </body>
</html>
```

</div></details>

確認用に以下の様なhtmlを作成

|<img width="580" alt="スクリーンショット 2019-07-13 18.36.07.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/682ed2b7-2a5a-9fec-c80b-f1ebc3ab0335.png">|
|:-:|


- Postで送信

|<img width="708" alt="スクリーンショット 2019-07-13 18.40.42.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/1e5fae7a-a2c1-89ac-b2dc-ac7e4188935b.png">|
|:-:|


- Getで送信


|<img width="662" alt="スクリーンショット 2019-07-13 18.40.58.png" src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/190554/efa97364-b20e-8436-dd11-e3f470604e12.png">|
|:-:|

### 躓いたところ
-  `templates`の置き場所（main.pyと同じ階層に作成しないと読みにいってくれない）

## 参考
- [Flask User’s Guide](https://flask.palletsprojects.com/en/1.1.x/)
