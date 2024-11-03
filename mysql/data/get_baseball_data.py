from pybaseball import statcast_batter, statcast_pitcher

# 期間設定
start_date = "2023-04-01"
end_date = "2023-09-30"

# 大谷翔平選手のプレイヤーID
ohtani_id = 660271

# バッティングデータを取得し、主要カラムのみを抽出
ohtani_batting_data = statcast_batter(start_date, end_date, ohtani_id)
ohtani_batting_minimal = ohtani_batting_data[['game_date', 'pitch_type', 'release_speed', 'player_name', 'events', 'balls', 'strikes', 'inning', 'stand', 'p_throws']]
ohtani_batting_minimal.to_csv("ohtani_batting_data.csv", index=False)

# # ピッチングデータを取得し、主要カラムのみを抽出
# ohtani_pitching_data = statcast_pitcher(start_date, end_date, ohtani_id)
# ohtani_pitching_minimal = ohtani_pitching_data[['game_date', 'pitch_type', 'release_speed', 'player_name', 'events', 'balls', 'strikes', 'inning', 'stand', 'p_throws']]
# ohtani_pitching_minimal.to_csv("ohtani_pitching_data.csv", index=False)