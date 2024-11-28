CREATE USER new_strong_user@'%' IDENTIFIED BY 'password';
GRANT ALL ON mydatabase.* TO 'new_strong_user'@'%';

CREATE USER new_weak_user@'%' IDENTIFIED BY 'password';
GRANT DELETE ON mydatabase.* TO 'new_weak_user'@'%';