# revised from T.Richards' streamlit example

import streamlit as st
from snownlp import SnowNLP

if 'sentiment' not in st.session_state:
    st.session_state.sentiment = "😐"

if 'text' not in st.session_state:
    st.session_state.text = '今天是周六。'
 
st.title('Chinese Sentiment Analyzer') 
st.write('😄 😊 😐 😟 😩')

def setText(txt):
    st.session_state.text = txt
    return

def sentiment(txt):
    sentiment = SnowNLP(txt)
    if sentiment.sentiments > 0.55:
        return '😄'
    elif sentiment.sentiments < 0.45:
        return '😩'
    else:
        return '😐'

st.session_state.text = st.text_area('Text to analyze','今天是周六。')

st.write('Sentiment:')
st.write('#', sentiment(st.session_state.text))

