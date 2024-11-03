CREATE TABLE IF NOT EXISTS pop (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age INT,
    city VARCHAR(255),
    country VARCHAR(255),
    status VARCHAR(50),
    phone VARCHAR(20)
);

INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('田中太郎', 'tanaka@example.com', 30, '東京', '日本', 'アクティブ', '090-1234-5678');
INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('佐藤花子', 'sato@example.com', 28, '大阪', '日本', '休止中', '080-9876-5432');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('鈴木一郎', 'suzuki@example.com', 35, '福岡', '日本', 'アクティブ', '070-1111-2222');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('高橋洋子', 'takahashi@example.com', 26, '札幌', '日本', 'アクティブ', '090-3333-4444');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('伊藤優子', 'ito@example.com', 40, '名古屋', '日本', '休止中', '080-5555-6666');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('山本健太', 'yamamoto@example.com', 22, '仙台', '日本', 'アクティブ', '070-7777-8888');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('中村純子', 'nakamura@example.com', 32, '広島', '日本', '休止中', '090-9999-0000');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('小林龍之介', 'kobayashi@example.com', 29, '神戸', '日本', 'アクティブ', '080-1212-3434');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('加藤美咲', 'kato@example.com', 27, '福井', '日本', 'アクティブ', '070-5656-7878');
-- INSERT INTO pop (name, email, age, city, country, status, phone) VALUES ('渡辺健', 'watanabe@example.com', 45, '金沢', '日本', '休止中', '090-9090-8080');