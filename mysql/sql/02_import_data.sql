-- 大谷選手のバッティングデータをインポート
LOAD DATA INFILE '/var/lib/mysql-files/ohtani_batting_data.csv'
INTO TABLE ohtani_batting
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(game_date, pitch_type, release_speed, batter_name, events, balls, strikes, inning, stand, p_throws);