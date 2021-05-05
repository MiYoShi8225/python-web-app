import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

#st.write('DateFrame')

st.write('Display Image')

#https://docs.streamlit.io/en/stable/api.html?highlight=image#streamlit.image
#動画もいける
img = Image.open('sample.png')
st.image(img, caption='twitter', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

#tableでは動的な表を作ることができない　静的な表を作る
#st.table(df.style.highlight_max(axis=0))

#折れ線グラフで記載
#st.line_chart(df)

#エリアグラフで記載
#st.area_chart(df)

#棒グラフで記載
#st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)


