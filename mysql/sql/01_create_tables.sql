-- バッティングデータ用のテーブル作成
CREATE TABLE IF NOT EXISTS ohtani_batting (
    game_date DATE,
    pitch_type VARCHAR(10),
    release_speed FLOAT NULL,       
    batter_name VARCHAR(100) NULL,  
    events VARCHAR(50) NULL,        
    balls INT NULL,                 
    strikes INT NULL,               
    inning INT NULL,                
    stand VARCHAR(5) NULL,          
    p_throws VARCHAR(5) NULL        
);