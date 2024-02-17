import streamlit as st
from PIL import Image

st.sidebar.markdown("# Nuages de mots")

# nuages de mots
st.header("Nuages de mots par topic")
st.write("")

st.write("**Topic 1 :** ACTIONS OFFICIELLES")
wordcloud_topic1 = Image.open("streamlit_app/wordcloud_lemma3_topic1.png")
st.image(wordcloud_topic1)
st.write("")

st.write("**Topic 2 :** FRONT ")
wordcloud_topic2 = Image.open("streamlit_app/wordcloud_lemma3_topic2.png")
st.image(wordcloud_topic2)
st.write("")

st.write("**Topic 3 :** PERSONNALITÉS PRÉSIDENTIELLES ")
wordcloud_topic3 = Image.open("streamlit_app/wordcloud_lemma3_topic3.png")
st.image(wordcloud_topic3)
