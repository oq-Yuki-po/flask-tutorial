# 目的

- Flask で Postgresql に接続
- DB にレコードを登録できること
- DB からレコードを取得できること

# 本編

## 環境準備

### python のパッケージを追加

```requirements.txt
flask
sqlalchemy
psycopg2
```

上記を`pip install -r requirements.txt` でインストール

#### ポイント

[sqlalchemy](https://www.sqlalchemy.org/)は python の ORM ライブラリ（簡単に言うとDB 操作は sqlalchemy が担当するよ）

`psycopg2`は flask と postgresql を繋いでくれる役割

#### <details><summary>インストールしたパッケージを一括でアンインストールする（必要があれば）</summary><div>

- pip でインストールしたパッケージの一覧を取得

```bash
$ pip freeze > piplist.txt
```

- 一括でアンインストール

```bash
$ pip uninstall -y -r piplist.txt
```

</div></details>

### 前回まで

chapter_003 ブランチ参照

### フォルダ構成

```bash
.
├── README.md
├── docker-compose.yml
├── form.html
├── postgresql
│   └── init
│       ├── 1_create_db.sql
│       └── 2_create_table.sh
├── requirements.txt
├── src
│   ├── UserModel.py
│   ├── main.py
│   ├── setting.py
│   └── templates
│       └── hello.html
└── test.http
```

## DB接続の準備

```setting.py
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# postgresqlのDBの設定
DATABASE = "postgresql://postgres:@192.168.1.19:5432/flask_tutorial"

# Engineの作成
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    # TrueにするとSQLが実行される度に出力される
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
```

#### ポイント
- DB の接続先情報  
  `DATABASE = "postgresql://postgres:@192.168.1.19:5432/flask_tutorial`  
  `DATABASE = "postgresql://{DBのユーザ}:{DBのパスワード}@{url}:{ポート番号}/{DB名}`  
  今回のDBは前回用意したDBをそのまま利用  
  {url}は自分のPCのIPを入力

- Engine 作成

```
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    # TrueにするとSQLが実行される度に出力される
    echo=True
)
```

Engine はDBにアクセスするための土台なんだと覚えとけば、とりあえずOK

- Session作成

```
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)
```

SessionはflaskとDBとのやり取りを全て担当してくれるもの

### データを挿入するテーブルを準備

```2_create_table.sh
#!/bin/bash
psql -U postgres -d flask_tutorial << "EOSQL"
CREATE TABLE users (
        id SERIAL NOT NULL, 
        name VARCHAR(200), 
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id)
);
EOSQL
```

```UserModel.py
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from setting import Base
from setting import ENGINE

class User(Base):
    """
    UserModel
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)
```

#### ポイント

- DBのDockerコンテナを初めて起動した際に、`2_create_table.sh`でUserテーブルを作成する  
※ DBが一度作成されている場合は、`/Users/${USER}/Volumes/flask_tutorial/postgres`を削除する
- flask側にDB上に、どんなテーブルがあるのかをsqlarchemyを使用して定義してあげる

### DB 確認

1. コンテナを起動  

```
$ docker-compose up -d
Creating network "flask-tutorial_default" with the default driver
Creating flask_tutorial_postgresql ... done
Creating flask_tutorial_pgadmin4   ... done
```

2. pgadminでUserテーブルが作成されていることを確認

### DB操作準備

```main.py

from flask import Flask, request, render_template
from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *

# appという名前でFlaskのインスタンスを作成
app = Flask(__name__)

# 登録処理
@app.route('/', methods=["POST"])
def register_record():

    name = request.form['name']

    session.add(User(name))

    session.commit()

    return render_template("hello.html", name=name, message="登録完了しました！")

# 取得処理
@app.route('/', methods=["GET"])
def fetch_record():

    name = request.args.get('name')

    db_user = session.query(User.name).\
        filter(User.name == name).\
        all()

    if len(db_user) == 0:
        message = "登録されていません。"
    else:
        message = "登録されています。"

    return render_template("hello.html", name=name, message=message)

if __name__ == '__main__':
    app.run()


```

#### ポイント

- 操作に必要なものをインポート

  - 操作対象のテーブル
  - DBの操作を行うのでsessionが必要

```
from UserModel import User
from setting import session
from sqlalchemy import *
from sqlalchemy.orm import *
```

- 登録処理

```
# 登録処理
@app.route('/', methods=["POST"])
def register_record():

    name = request.form['name']

    session.add(User(name))

    session.commit()

    return render_template("hello.html", name=name, message="登録完了しました！")
```
実際に登録している箇所は以下   

```
    session.add(User(name))

    session.commit()
```

`session.add`でINSERT文を実行  
`session.commit()`コミットしてる

- 取得処理

```
# 取得処理
@app.route('/', methods=["GET"])
def fetch_record():

    name = request.args.get('name')

    db_user = session.query(User.name).\
        filter(User.name == name).\
        all()

    if len(db_user) == 0:
        message = "登録されていません。"
    else:
        message = "登録されています。"

    return render_template("hello.html", name=name, message=message)
```

取得処理は、以下

```
    db_user = session.query(User.name).\
        filter(User.name == name).\
        all()
```

`session.query(User.name)`で取得したい`テーブル.列名`  
`filter(User.name == name)`はWHERE句  
`all()`でクエリを実行

※　今回は単純なSELECT文のみ、テーブル結合などもできるので必要に応じて適宜調べてください。

### DB操作確認

1. コンテナを起動  

```bash
$ docker-compose up -d
Creating network "flask-tutorial_default" with the default driver
Creating flask_tutorial_postgresql ... done
Creating flask_tutorial_pgadmin4   ... done
```

2. flaskを起動

```bash
$ python src/main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

3. form.htmlで確認

# 次回

- nginxのコンテナを使用して静的ページを切り離す