# Name

タスク管理アプリ

# このアプリでアピールしておきたいポイント

・現在、多くの web 系企業で採用されている react,react-redux,TypeScript でフロントを構築していること

・サーバーサイドの web フレームワーク（今回は django)を用いて CRUD を実装できていること。

・データベースの仕組みを理解した上で、作成されるテーブルに文字数制限や外部キーを利用したりして構築されていること

・非同期処理を実装していること

・開発手順.txt にて、自分がどんな流れでこのアプリを開発したのかが、0 からしっかりメモされていること。

# DEMO
このアプリのデモ動画です。

ご都合により、gitからクローンして起動させるお時間が取れない場合、こちらのデモ動画でこのアプリの実装を確認することができます。

https://github.com/kenshow-blog/task-manage-app/issues/1

# Features

主な機能：

・ログイン、ユーザー登録機能

・タスクの編集、削除、作成が可能

・プロフィールのアバター画像の変更が可能

・タスクの中のカテゴリーの作成が可能。

# Requirement

このタスク管理アプリを動かすのに必要なライブラリなどを列挙する

asgiref==3.2.10

certifi==2020.6.20

dj-database-url==0.5.0

Django==3.1

django-cors-headers==3.4.0

django-environ==0.4.5

django-templated-mail==1.1.1

djangorestframework==3.11.1

djangorestframework-simplejwt==4.1.2

djoser==2.0.3

Pillow==7.2.0

PyJWT==1.7.1

pytz==2020.1

sqlparse==0.3.1

# Installation

1.  src/にて
    pip install -r requirements.txt
    で必要な djangoAPI 構築にライブラリをインストールする

2.  src/にて
    python(python3) manage.py runserver
    でバックエンドを起動する

3.  frontend/
    にて
    npm install

4.  npm start
    でフロントエンドを立ち上げる

# Note

特になし

# Author

作成情報を列挙する

- 作成者　田中 健将
- 所属　学生（明治大学）
- E-mail 　kenshou0213@icloud.com
