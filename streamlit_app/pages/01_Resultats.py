import streamlit as st

st.sidebar.markdown("# Resultats de la modélisation")
st.header("Modèle retenu : ")
st.write("LDA : Lemmatisation - 3 topics - unigram")

# image html
import streamlit.components.v1 as components

st.write("")
st.header("Représentation des topics :")
resultat_html_1 = open("streamlit_app/lda_lemma_3topics.html")
components.html(resultat_html_1.read(), scrolling=False, width=1200, height=770)
st.write("")

st.header("Description des topics :")
st.write("**Topic 1 :** ACTIONS OFFICIELLES ")
st.write(
    "Cette topic évoque clairement le conflit à travers les actions et déclarations des grandes instances politiques internationales, comme l'Union Européenne, l'ONU ou l'OTAN ainsi que différentes ONG comme la ligue des droits de l'homme."
)
st.write("")

st.write("**Topic 2 :** FRONT ")
st.write(
    "Ici, c'est l'Ukraine comme théâtre de la guerre qui se profile, avec les actualités militaires et faits des combats sur le terrain. Dans un second temps, les dimensions humaines et sociales directes de ces affrontements apparaissent dans le soutien populaire qui s'organise dans différentes régions du monde, tel que des collectes et envois de biens de première nécessité. "
)
st.write("")

st.write("**Topic 3 :** PERSONNALITÉS PRÉSIDENTIELLES ")
st.write(
    "Cette topic représente les expressions de la guerre en Ukraine par une sorte de prisme présidentiel. Les tweets ne se concentrent ni sur un type de faits ni d'évènements en particulier. On y évoque directement les présidents ( surtout Poutine, Macron et Zélensky) moins en temps que chef d'état mais plutôt de personnalités parfois assez fortes en présence. "
)
