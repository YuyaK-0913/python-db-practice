# MySQL Tips


- **MySQLのdockerコンテナを立てて，データベースにログインする場合**
        
    - 方法①
        ```
        docker exec -it <コンテナ名> mysql -u <ユーザ名> -p -D <データベース名>
        ```
    
    - 方法②

        ②の方がMySQLサーバのディレクトリなどを確認できたりして便利．
        ```bash
        docker exec -it <コンテナ名> /bin/bash
        ```
        ```bash
        mysql -u <ユーザ名> -p -D <データベース名>
        ```

- **MySQLのデータベースにCSVファイルのデータをインポートする場合**

    - MySQLでは，データの取り扱いやエラーハンドリングをどのように行うかを制御する設定として，```sql_mode```が設定されている．
    
    - デフォルトでは、MySQLはデータ整合性を強制するため、特定のモードが有効になっている。
    
    - このため、NULL値や不完全なデータが含まれるとエラーが発生することがある．

    - 下記のコマンドで```sql_mode```の設定は確認可能．
        ```
        SHOW VARIABLES LIKE 'sql_mode';
        ```
    - ```sql_mode```の設定はmy.cnfで行う．
        ```my.cnf
        [mysqld]
        sql_mode = "NO_ENGINE_SUBSTITUTION"
        ```

- **SQLファイルの手動実行**

    MySQLでSQLファイルを実行する場合，```/docker-entrypoint-initdb.d```ディレクトリにSQLファイルを配置すればよいが，手動実行も可能である．

    - ```/docker-entrypoint-initdb.d```以外の任意の場所にSQLファイルを配置しておく．

    - MySQLサーバ内で，
        ```bash
        mysql -u root -p -D <データベース名> < <SQLファイルのパス>
        ```
        を実行すればOK.


