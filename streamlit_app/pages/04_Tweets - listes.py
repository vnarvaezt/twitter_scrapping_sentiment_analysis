import os

import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Liste des tweets les plus et moins contribuants par topics")
st.sidebar.markdown("# Tweets lists")

# import des données
# path = "C:\\Users\\VIVAN Sabrina"
# os.chdir(path)
df_topic_lemma3 = pd.read_csv(
    "streamlit_app/dominant_topics_lemma_3topics.csv",
    sep=";",
)
# tweets les plus et moins contribuants par topics
st.subheader("**Topic 1 :** ACTIONS OFFICIELLES")

st.write("50 tweets les **plus** contribuants")
df_topic1_plus_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 1]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, False])
    .head(50)
)
st.dataframe(df_topic1_plus_contribuants)

st.write("50 tweets les **moins** contribuants")
df_topic1_moins_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 1]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, True])
    .head(50)
)
st.dataframe(df_topic1_moins_contribuants)
st.subheader("")

st.subheader("**Topic 2 :** FRONT ")

st.write("50 tweets les **plus** contribuants")
df_topic2_plus_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 0]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, False])
    .head(50)
)
st.dataframe(df_topic2_plus_contribuants)

st.write("50 tweets les **moins** contribuants")
df_topic2_moins_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 0]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, True])
    .head(50)
)
st.dataframe(df_topic2_moins_contribuants)
st.subheader("")


st.subheader("**Topic 3 :** PERSONNALITÉS PRÉSIDENTIELLES ")

st.write("50 tweets les **plus** contribuants")
df_topic3_plus_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 2]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, False])
    .head(50)
)
st.dataframe(df_topic3_plus_contribuants)

st.write("50 tweets les **moins** contribuants")
df_topic3_moins_contribuants = (
    df_topic_lemma3[df_topic_lemma3["dominant_topic"] == 2]
    .sort_values(by=["dominant_topic", "topic_perc_contrib"], ascending=[True, True])
    .head(50)
)
st.dataframe(df_topic3_moins_contribuants)
