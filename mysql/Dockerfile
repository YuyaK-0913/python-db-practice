## StatscastのCSVデータを取得しMySQLサーバのディレクトリに配置

## データを取得するコンテナ
FROM python:3.10.6-slim as data-fetcher

RUN pip install --no-cache-dir pybaseball

COPY data/get_baseball_data.py /data/get_baseball_data.py
WORKDIR /data

# CMD ["/bin/bash", "-c", "while true; do sleep 1; done"]
RUN python get_baseball_data.py


## データを取得したデータをMySQLサーバに配置するコンテナ
FROM mysql:8.2.0

COPY --from=data-fetcher /data/ohtani_batting_data.csv /var/lib/mysql-files/ohtani_batting_data.csv

COPY conf.d/my.cnf /etc/mysql/conf.d/my.cnf
RUN chmod 644 /etc/mysql/conf.d/my.cnf

