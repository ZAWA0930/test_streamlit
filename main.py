import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('streamlit 超入門')

st.write("プログレスバーの表示")

latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'




left_column, right_column=st.columns(2)
button=left_column.button('右のカラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

    expander1= st.expander("お問い合わせ1")
    expander1.write('お問合せ1の回答')
    expander2= st.expander("お問い合わせ2")
    expander2.write('お問合せ2の回答')
    expander3= st.expander("お問い合わせ3")
    expander3.write('お問合せ3の回答')
#text =st.text_input('あなたの趣味を教えてください')
#condition=st.slider('あなたの調子は?',0,100,50)



#'あなたの趣味:',text, 'です。'
#"コンディション:",condition

#if st.checkbox("Show Image"):
 #   img=Image.open("space.jpg")
  #  st.image(img, caption="Space" ,use_column_width=True)





