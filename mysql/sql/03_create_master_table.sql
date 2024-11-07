-- game_datesテーブルを作成
CREATE TABLE IF NOT EXISTS game_dates (
    date DATE,
    day_of_week INT AS (DAYOFWEEK(date)) STORED,
    day_name VARCHAR(10) AS (DAYNAME(date)) STORED
);