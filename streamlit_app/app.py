import streamlit as st
from PIL import Image

# (nom des onglets sur le bandeau de gauche = nom des fichiers .py))
# titre sur le bandeau de gauche
st.sidebar.markdown("# Présentation")
st.markdown("<span style=“background-color:#3d85c6”>", unsafe_allow_html=True)
st.write("")
# titre
t1, t2 = st.columns((1, 0.5))

sda = Image.open("streamlit_app/sda.jpg")
t2.image(sda, width=120)
t1.title("Projet 3 - Text mining")

st.header("Suivi du #Ukraine")
st.write(" Alicia - Anne - Julie - Valentina")

st.write("")
st.subheader("Objectif :")
st.write(
    "Produire une analyse des tweets en français sur la guerre russo-ukrainienne de 2022"
)

st.write("")
st.subheader("Périmètre de l'analyse :")
st.write("**Période :** Du 1er Février 2022 au 30 Juin 2022")
st.write(
    "**Filtres :** Tweets français uniquement et dont le nombre de retweets est supérieur ou égal à 3. Postulat : les tweets les plus relayés montrent des discours qui ont eu le plus d'impact dans ce réseau social."
)
st.write(
    "**Extraction :** 50 tweets extraits dans une fenêtre de temps de 30 minutes tous les jours entre février et juin 2022."
)
st.write("")

# Attention on a plus le meme nb de tweets à analyse dans csv df lda lemma3
st.metric(label="Nombre de tweets analysés :", value=str(19832) + " tweets")

# Contents of ~/appli_streamlit/app.py


def page1():
    st.markdown("# Results")
    st.sidebar.markdown("# Results")


def page2():
    st.markdown("# Wordclouds")
    st.sidebar.markdown("# Wordclouds")


def page3():
    st.markdown("# Tweets_evolutions")
    st.sidebar.markdown("# Tweets_evolutions")


def page4():
    st.markdown("# Tweets_lists")
    st.sidebar.markdown("# Tweets_lists")


page_names_to_funcs = {
    "Results": page1,
    "Wordclouds": page2,
    "Tweets_evolutions": page3,
    "Tweets_lists": page4,
}
