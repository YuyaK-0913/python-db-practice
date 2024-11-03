LOAD DATA INFILE '/var/lib/mysql-files/pop_data.csv'
INTO TABLE pop
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(name, email, age, city, country, status, phone);
