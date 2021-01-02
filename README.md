# Name

タスク管理アプリ

# このアプリで抑えられているポイント

・react,react-redux,TypeScript でフロントを構築していること

・サーバーサイドの web フレームワーク（今回は django)を用いて CRUD を実装できていること。

・SQLを利用し、作成されるテーブルに文字数制限や外部キーの連携を用いて構築されていること

・非同期処理を実装していること

・開発手順.txt にて、自分がどんな流れや考えでこのアプリを開発したのかが、0 からメモされていること。（私の備忘録と、思考の整理が目的）


# このアプリを作ろうと思ったきっかけ

・基本毎日勉強しているので、自身の生産性を向上させてくれるようなアプリを作りたかった。

・モダン技術を用いたアプリ開発や方式を習得したかったから。
採用技術
（フロント： react,react-redux,TypeScript
 バック： Django(python)
 インフラ： EC2(AWS),NGINX)

・エンジニアとしての自走力を養いたかった。


# DEMO
このアプリのデモ動画です。

こちらのデモ動画で、このアプリの実装を確認することができます。
（視聴時間 1分)

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



# Author

作成情報を列挙する

- 作成者　田中 健将
- 所属　学生（明治大学）
- E-mail 　kenshou0213@icloud.com
