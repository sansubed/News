import streamlit as st
import pandas as pd

st.title('Text Classification')

news = st.text_area('Text to translate')
if st.button('Submit'):
    dict = {'news': [news]}
    df = pd.DataFrame(dict)
    st.dataframe(df)
    st.write('News submitted.')


