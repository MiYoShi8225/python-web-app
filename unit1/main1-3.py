import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('Display Image')
st.write('Interactive Widgets')

option = st.text_input('貴方の趣味を教えて下さい。')
'あなたの趣味は、', option, 'です。'

# slider の数は 最小値,最大値,デフォルト値で構成される
condition = st.slider('あなたの今の調子は?', 0, 100, 50)
'コンディションは、', condition

######
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい.',
#     list(range(1,11))
# )
#'あなたの好きな数字は、', option, 'です'
######

######
# if st.checkbox('Show Image'):
#     #https://docs.streamlit.io/en/stable/api.html?highlight=image#streamlit.image
#     #動画もいける
#     img = Image.open('sample.png')
#     st.image(img, caption='twitter', use_column_width=True)
######

