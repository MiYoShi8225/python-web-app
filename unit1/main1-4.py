import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

#表示を垂れ幕形式で表示できる
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option = st.text_input('あなたの趣味を教えて下さい。')
# # slider の数は 最小値,最大値,デフォルト値で構成される
# condition = st.slider('あなたの今の調子は?', 0, 100, 50)

# 'あなたの趣味は、', option, 'です。'
# 'コンディションは、', condition
