-- game_datesにデータを挿入
SET @@cte_max_recursion_depth = 10000;

SET @start_date = '2020-01-01';
SET @end_date = '2024-11-30';

CREATE TEMPORARY TABLE temp_dates AS
WITH RECURSIVE date_range AS (
  SELECT @start_date AS date
  UNION ALL
  SELECT DATE_ADD(date, INTERVAL 1 DAY)
  FROM date_range
  WHERE date < @end_date
)
SELECT date FROM date_range;

INSERT INTO game_dates (date)
SELECT * FROM temp_dates;

DROP TABLE temp_dates;