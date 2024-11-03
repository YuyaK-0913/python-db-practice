# MySQL Guide

## データベースへのログイン
- **MySQLのデータベースへのログイン**
    ```
    mysql -u <ユーザ名> -p<password> -D <データベース名>
    ```
    - ```-p```オプションでパスワードを入力する際は，スペースが不要なので注意．

    - 例えば，dockerコンテナに入って，mysqlのデータベースにログインする際は
        ```
        docker exec -it sample_db mysql -u myuser -p -D <データベース名>
        ```
        を実行．

## テーブルの作成
- **Dockerで初期テーブルを作成する方法**

    - docker-compose.yamlで```/docker-entrypoint-initdb.d```にテーブル作成処理を記述したSQLファイルを配置しておけば，自動で実行される．
        ```yaml
        volumes:
            - ./mysql/data:/docker-entrypoint-initdb.d
        ```
    - ```/docker-entrypoint-initdb.d```に複数のファイルを配置すれば，すべて実行される．

- **手動でSQLファイルを実行する方法**
    - docker-compose.yamlでmysqlコンテナの任意の場所にSQLファイルを配置しておく
        ```yaml
        volumes:
            - ./mysql/data:/work
        ```

    - mysqlコンテナに入る
        ```bash
        docker exec -it <mysqlコンテナ> /bin/bash
        ```
    - mysqlコンテナでルートユーザとしてSQLファイルを実行する
        ```bash
        mysql -u root -p -D <データベース名> < <SQLファイルのパス>
        ```
    - mysqlサーバでデータベースに接続する
        ```bash
        mysql -u <ユーザ名> -p -D <データベース名>
        ```
        もしくは
        ```
        mysql -u <ユーザ名> -p

        # ログイン後
        use <データベース名> # データベースの切り替えコマンド
        ```
    - テーブルが作成されているかの確認
        ```mysql
        show tables;
        ```

## CSVファイルのインポート
- **CSVファイルのデータをテーブルにインポートする方法**
    
    - MySQLにはPostgreSQLのような```COPY```コマンドはないが、代わりに```LOAD DATA INFILE```コマンドを使用してCSVファイルからデータをインポートすることができる．

    - ただし，MySQLでは，データベースサーバーがファイルを読み書きできるディレクトリを制限しており，```secure_file_priv```に登録されているディレクトリ内のファイルのみテーブルへのインポート可能である．
    
    - ```secure_file_priv```に登録されているディレクトリは，下記のコマンドで確認可能である．
        ```mysql
        SHOW VARIABLES LIKE 'secure_file_priv';
        ```
        または
        ```mysql
        select @@global.secure_file_priv;
        ```
        すると，下記のような結果が出力される．
        ```
        +---------------------------+
        | @@global.secure_file_priv |
        +---------------------------+
        | /var/lib/mysql-files/     |
        +---------------------------+
        1 row in set (0.00 sec)」
        ```
    
    - そのため，インポートしたいCSVファイルは，```/var/lib/mysql-files/```に配置して実行しなければならない
        
        - docker-compose.yaml内でCSVファイルを```/var/lib/mysql-files/```に配置．
            ```yaml
            volumes:
            - ./mysql/data:/var/lib/mysql-files/ # 手動でテーブルを作成する場合
            ```
        
        - ルートユーザーとしてsqlファイルをの実行．
            ```bash
            mysql -u root -p -D mydatabase < /var/lib/mysql-files/test2.sql 
            ```
            ちなみに，SQLファイルの内容は下記．
            ```sql
            LOAD DATA INFILE '/var/lib/mysql-files/pop_data.csv'
            ```
            
