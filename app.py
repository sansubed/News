import streamlit as st
import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

st.title('Text Classification')

#load stopwords
nltk.download('stopwords')
words = stopwords.words('english')
stemmer = PorterStemmer()

# load model
dbFile = open('LogisticRegression.pickle', 'rb')
model = pickle.load(dbFile)

# taking data from user and convert to dataframe
news = st.text_area('Text to translate')
if st.button('Submit'):
    dict = {'news': [news]}
    df = pd.DataFrame(dict)
    df['news'] = list(map(lambda x: " ".join([j for j in re.sub('[^a-zA-Z]', ' ', x).lower().split() if j not in words]), df['news']))
    df['news'] = list(map(lambda x: " ".join([stemmer.stem(j) for j in x.split()]), df['news']))
    #predict the news
    result = model.predict(df['news'])[0]
    st.dataframe(df)
    st.write('News submitted.')
    st.write('Prediction:', result)