# elixir-fest.jp

## 開発環境のセットアップ(Docker版)

初回に一度だけ実行する

### 事前準備

- `docker`, `docker-compose`のインストール

```sh
$ git clone git@github.com:elixirjp/elixirfestjp.git
$ cd ./elixirfestjp
$ make build
```

### 起動

```sh
$ make run
$ make migrate
$ make createsuperuser
$ make loaddata
```

http://localhost:8000/ で開く。


### 各種コマンド

#### 管理画面のユーザー作成
```sh
$ make createsuperuser
```

#### 初期データインポート
```sh
$ make loaddata
```

#### マイグレーション作成
```sh
$ make makemigration app=core
```

#### マイグレーション実行
```sh
$ make migrate
```

### 設定

#### GitHubログインに使用
`SOCIAL_AUTH_GITHUB_KEY = ''`
`SOCIAL_AUTH_GITHUB_SECRET = ''`

#### Twitterログインに使用
`SOCIAL_AUTH_TWITTER_KEY = ''`
`SOCIAL_AUTH_TWITTER_SECRET = ''`

#### スピーカー応募時の自動返信メール
`ACCEPTING_EMAIL_TO_USER_SUBJECT = '[Erlang & Elixir Fest 2018] スピーカー応募を受け付けました'`
`ACCEPTING_EMAIL_TO_ADMIN_SUBJECT = '[Erlang & Elixir Fest 2018] スピーカー応募がありました'`

#### 管理者へのメール送信時の送信元・宛先

`ADMIN_EMAIL_FROM = 'no-reply@elixirconf.jp'`
`ADMIN_EMAILS_TO = []`

#### 申し込みURL
`CONNPASS_URL = ''`

#### サイトの公開ステータス
```
PUBLICATION_STATUS = (
    # 情報公開準備中
    PUBLICATION_STATUS_PREPARING = 0
    # スピーカー申し込み受付中
    PUBLICATION_STATUS_ACCEPTING = 1
    # スピーカー申し込み受付終了
    PUBLICATION_STATUS_END_ACCEPTING = 2
    # 公開
    PUBLICATION_STATUS_PUBLIC = 3
)
```
