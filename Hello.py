import streamlit as st
from utile import valid

import googlesearch

try:
  from googlesearch import Search
  
except Exception:
  st.write(dir(googlesearch))

def f(a, b, c):
    st.write(valid(a, b, c))

def b():
  st.balloons()
  st.snow()

number = st.slider(min_value=1, max_value=80, step=1, label="entrez le nombre de recherches a effectué")
mots = st.text_area("entrez les mots a rechercher")
ban_words = st.text_area("entrez les mots ne devant pas figurer dans les recherches")

st.button("entrez .", on_click=lambda : f(mots, ban_words, number))
st.button("quelque chose de fun .", on_click=lambda:st.balloons())
st.button("autre chose de fun .", on_click=lambda:st.snow())
st.button("derniere chose de fun .", on_click=lambda:b())
