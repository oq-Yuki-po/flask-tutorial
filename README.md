# 目的

- Flask で使用する DB（PostgreSQL） を Docker を使用して準備する
- DB を pgadmin4 で見れるようにする

## 環境準備

### 前回まで

chapter_002 ブランチ参照

### Docker 環境準備

Mac の場合

```bash
  brew cask install docker
```

ver 確認

```bash
  $ docker -v
    Docker version 18.09.1, build 4c52b90
```

### フォルダ構成

```bash
$ tree
.
├── README.md
├── docker-compose.yml
├── form.html
├── pgadmin
├── postgresql
│   ├── data
│   └── init
│       └── 1_create_db.sql
├── requirements.txt
└── src
    ├── main.py
    └── templates
        └── hello.html

```

## DB 作成

### docker-compose.yml の作成

```docker-compose.yml

version: "3"

services:

  postgresql:
    # イメージの指定
    image: postgres:10.5
    # コンテナの名前
    container_name: flask_tutorial_postgresql
    # hostのport5432とコンテナのport5432を繋ぐ
    # ホスト；コンテナ
    ports:
      - 5432:5432
    # hostとコンテナで共有するファイルやディレクトリを設定
    # ホストのディレクトリ；コンテナのディレクトリ
    volumes:
      # /docker-entrypoint-initdb.dはコンテナ初回起動時に実行されるスクリプトを置く場所
      - ./DB/init/:/docker-entrypoint-initdb.d
      # /var/lib/postgresql/dataはpostgresqlのデータが保存されている場所
      - /var/lib/:/var/lib/postgresql/data
    # コンテナの環境変数設定
    environment:
      # スーパユーザ名(省略時は"postgres")
      POSTGRES_USER: ${POSTGRES_USER}
      # スーパユーザのパスワード(省略時はパスワードなしでログイン可)
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      # postgresqlの初期化時の文字コード
      POSTGRES_INITDB_ARGS: "--encoding=UTF-8"
    # ホスト名
    hostname: postgres
    # Dockerを実行するユーザ
    user: root
    environment:
      TZ: "Asia/Tokyo"

  pgadmin4:
    image: dpage/pgadmin4:3.3
    container_name: flask_tutorial_pgadmin4
    ports:
      - 80:80
    volumes:
      - ./pgadmin:/var/lib/pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD}
    depends_on:
          - postgresql
    hostname: pgadmin4

```

#### ポイント

`${POSTGRES_USER}`や`${POSTGRES_PASSWORD}`の`${}`は変数を表していて
docker-compose.yml と同じ階層にある`.env` ファイルで変数を指定できる。

.env の例

```
POSTGRES_USER=root
POSTGRES_PASSWORD=root
PGADMIN_DEFAULT_EMAIL=root
PGADMIN_DEFAULT_PASSWORD=root
```

### コンテナ操作

`docker-compose.yml`があるディレクトリで`docker-compose up -d`実行

コンテナ起動

```bash
$ docker-compose up -d
Creating network "first_tutorial_default" with the default driver
Creating flask_tutorial_postgresql ... done
Creating flask_tutorial_pgadmin4   ... done
```

コンテナが起動できたか確認

```bash
$ docker ps -a
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                         NAMES
487182403fc2        dpage/pgadmin4:3.3   "/entrypoint.sh"         8 seconds ago       Up 6 seconds        0.0.0.0:80->80/tcp, 443/tcp   flask_tutorial_pgadmin4
1441abbc6c72        postgres:10.5        "docker-entrypoint.s…"   9 seconds ago       Up 7 seconds        0.0.0.0:5432->5432/tcp        flask_tutorial_postgresql
```

コンテナを落とす

```bash
$ docker-compose down
Stopping flask_tutorial_pgadmin4 ... done
Removing flask_tutorial_pgadmin4   ... done
Removing flask_tutorial_postgresql ... done
Removing network first_tutorial_default
```

### 初回実行スクリプトについて

```1_create_db.sql
create database flask_tutorial;
```

#### ポイント

- ファイル名の先頭に数字を入れると、その順番で実行してくれる
- 今回は単純に`flask_tutorial`という DB を作成しているのみ

## DB 確認

### pgadmin4 にアクセス

```docker-compose.ymlの一部抜粋
  pgadmin4:
    image: dpage/pgadmin4:3.3
    container_name: flask_tutorial_pgadmin4
    ports:
      - 80:80
    volumes:
      - ./pgadmin:/var/lib/pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD}
    depends_on:
          - postgresql
    hostname: pgadmin4
```

コンテナ起動を起動した状態で`http://localhost:80`にアクセス

#### ポイント

`Email Address`と`Password`は.env  で設定した値

### サーバ接続

pgadmin4 にログイン
`Servers`を右クリック
`Servers`>`作成`>`サーバ...` を選択すると以下が表示されるので設定していく

#### ポイント

`ホスト名/アドレス` はホストの IP アドレスを調べて入力すること

### DB 確認

flask_tutorial という DB が存在していることを確認

## 次回

- flask で DB に接続してみよう
