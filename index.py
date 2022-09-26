# D07142002、徐樂德、https://thomasschlatter-assigment-1-index-yb1y7x.streamlitapp.com/

import streamlit as st
from snownlp import SnowNLP

if 'sentiment' not in st.session_state:
    st.session_state.sentiment = "😐"

if 'text' not in st.session_state:
    st.session_state.text = ""
 
st.title('Chinese Sentiment Analyzer') 
st.markdown('😄😊😐😟😩') 

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

def sentimentToAlpha(txt):
    returnTxt = ""
    sentiment = SnowNLP(txt)
    for i in range(0,len(sentiment.words)):
        wordSentiment = SnowNLP(sentiment.words[i]).sentiments
        if wordSentiment > 0.5:
            colorString = '0, 255, 0'
            alpha = wordSentiment
        elif wordSentiment < 0.5:
            colorString = '255, 0, 0'
            alpha = wordSentiment
        else:
            colorString = '128, 128, 128'
            alpha = 0.2
        returnTxt += f'<span style="background-color:rgba({colorString}, {alpha});">{sentiment.words[i]}</span>'
    return returnTxt

st.session_state.text = st.text_area('Text to analyze','你好。去死吧。')

st.write('Sentiment:')
st.markdown("<h1>"+sentiment(st.session_state.text)+"</h1>", unsafe_allow_html=True)
st.markdown(sentimentToAlpha(st.session_state.text), unsafe_allow_html=True)

