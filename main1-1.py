import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DateFrame')

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

# st.write(df)

# いくつか指定できる引数が存在する writeとことなり pixel単位で大きさを指定できる
#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

#highlight_maxで列の中で大きい値をマークする
#st.dataframe(df.style.highlight_max(axis=0))

#tableでは動的な表を作ることができない　静的な表を作る
st.table(df.style.highlight_max(axis=0))

#マークダウンで表示できる↓
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""



