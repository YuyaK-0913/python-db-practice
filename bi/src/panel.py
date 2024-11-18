import panel as pn
import pandas as pd
from service import PitchTypeService, MergedService
from db_client import MySQLClient

pn.extension('tabulator')

# データベースクライアントのインスタンス化
db_client = MySQLClient()

# サービスのインスタンス化
pitch_service = PitchTypeService(db_client=db_client)
merged_service = MergedService(db_client=db_client)

# サイドバーウィジェットの作成
pitch_types = pitch_service.list_pitch_type()
pitch_types.append('All')
pitch_type_select = pn.widgets.Select(
    name='Pitch Type',
    options=pitch_types,
    value=pitch_types[0] if pitch_types else None
)

# データフレーム表示用のウィジェット
data_table = pn.widgets.Tabulator(pd.DataFrame(), width=800, height=400)

# コールバック関数の定義
def update_table(event):
    selected_pitch = event.new
    df = merged_service.retrieve_merged_data(pitch_type=selected_pitch)
    data_table.value = df

# 初期データのロード
if pitch_types:
    initial_pitch = pitch_types[0]
    initial_df = merged_service.retrieve_merged_data(pitch_type=initial_pitch)
    data_table.value = initial_df

# ウィジェットにコールバックを設定
pitch_type_select.param.watch(update_table, 'value')

# FastListTemplate のインポート
# from panel.template import FastListTemplate

# テンプレートの作成
template = pn.template.FastListTemplate(
    title="Pitch Data Dashboard",
    sidebar=[
        "# サイドバー",
        pitch_type_select
    ],
    main=[
        "# データ表示",
        data_table
    ],
    # theme="fast",  # 他にも 'default', 'dark_minimal' など利用可能
    accent_base_color="#88d8b0",  # アクセントカラーを設定
    header_background="#003366"
)

# アプリケーションの表示
template.servable()