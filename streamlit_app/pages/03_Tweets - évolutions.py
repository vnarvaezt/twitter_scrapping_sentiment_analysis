import os

import pandas as pd
import plotly.express as px
import streamlit as st

st.header(
    "Evolution du nombre de tweets (retweetés au moins 3 fois), par jour, par topic"
)
st.sidebar.markdown("# Tweets evolutions")
st.write("")

# import des données
# path = "C:\\Users\\VIVAN Sabrina"
# os.chdir(path)
df_fr = pd.read_csv(
    "streamlit_app/df_fr.csv",
    sep=",",
)
df_gouv = pd.read_csv("streamlit_app/df_gouv.csv", sep=",")
df_topic_lemma3 = pd.read_csv(
    "streamlit_app/dominant_topics_lemma_3topics.csv",
    sep=";",
)
tweet_date = pd.read_csv(
    "streamlit_app/tweet_date.csv",
    sep=",",
)

df_topic_lemma3_acdate = pd.merge(
    df_topic_lemma3, tweet_date, on="tweet_id", how="left"
)

# line plot evolution du nb de tweets par jour - topic 1
st.subheader("**Topic 1 :** ACTIONS OFFICIELLES")

tpd_topic1 = (
    df_topic_lemma3_acdate[df_topic_lemma3_acdate["dominant_topic"] == 1]
    .groupby("date")["tweet_id"]
    .count()
    .reset_index()
)
fig1 = px.line(tpd_topic1, x="date", y="tweet_id")
st.plotly_chart(fig1, use_container_width=True)
st.write("Rapprochement des pics avec l'actualité")
st.write(
    "22/02 : La Russie reconnaît l'indépendance des territoires séparatistes dans le Donbass (indépendance de la république populaire de Donetsk et de la république populaire de Lougansk)"
)
st.write(
    "24/02 : la guerre éclate / Le G7 s'est mis d'accord sur des sanctions « dévastatrices » contre la Russie, en réponse à l'invasion de l'Ukraine"
)
st.write("27/02 : Menace nucléaire de la Russie / UE envoie des armes à l'Ukraine")
st.write("28/02 : L'Ukraine demande son adhésion à l'Ukraine")
st.write(
    "01/03 : Le ministre de l'Intérieur français Gérald Darmanin prolonge Les titres de séjour des Ukrainiens"
)
st.write(
    "07/03 : Troisième séance de négociations russo-ukrainiennes qui s'est achevée en début de soirée avec quelques résultats positifs sur les couloirs humanitaires"
)
st.write(
    "09/03 : Russes et Ukrainiens sont tombés d'accord pour respecter des cessez-le feu autour d'une série de couloirs humanitaires afin d'évacuer les civils"
)
st.write(
    "14/03 : Un convoi de 210 voitures d'évacuation de la population a pu quitter le port stratégique de Marioupol en direction de Zaporojie / L'UE a décidé de sanctionner de nouveaux oligarques russes"
)
st.write("16/03 : Russie exclue du Conseil de l'Europe")
st.write(
    "23/03 : Le président ukrainien Volodymyr Zelensky s'est exprimé en visioconférence à l'Assemblée nationale et au Sénat. Il appelé au boycott du marché russe et réclamé que « les entreprises françaises quittent le marché russe », en citant les groupes Auchan, Leroy Merlin et Renault. Ce dernier a annoncé mercredi la suspension des activités de son usine à Moscou. Tandis que La holding de Leroy Merlin a décidé de maintenir ses activités en Russie"
)
st.write(
    "24/03 : Sommets du G7 et de l'Otan à Bruxelles. Le G7 veut que Poutine et ses soutiens « rendent des comptes » / L'ONU « exige » la fin immédiate du conflit / Nouvelles sanctions de Londres et Washington / Changement de stratégie du Kremelin pour se concentrer sur le Donbass à l'Est"
)
st.write(
    "16/06 : Visite des présidents français, allemand et italien en Ukraine. Ils ont réaffirmé le soutien de l'Europe à l'Ukraine en guerre. / Bruxelles devrait rendre un avis positif sur la candidature de l'Ukraine à l'UE"
)
st.write("")

# line plot evolution du nb de tweets par jour - topic 2
st.subheader("**Topic 2 :** FRONT ")

tpd_topic2 = (
    df_topic_lemma3_acdate[df_topic_lemma3_acdate["dominant_topic"] == 0]
    .groupby("date")["tweet_id"]
    .count()
    .reset_index()
)
fig2 = px.line(tpd_topic2, x="date", y="tweet_id")
st.plotly_chart(fig2, use_container_width=True)
st.write("Rapprochement des pics avec l'actualité")
st.write(
    "24/02 : la guerre éclate / La Russie a pris le contrôle de la centrale de Tchernobyl"
)
st.write(
    "01/03 : La Russie a intensifié son offensive, notamment à Kharkiv et à Kiev où la tour de télé a été touchée, faisant 5 morts"
)
st.write(
    "04/03 : L'armée russe prend la centrale nucléaire de Zaporijia, la plus grande d'Europe "
)
st.write("09/03 : une maternité bombardée à Marioupol")
st.write("13/03 : Russie bombarde une base Ukrainienne vers la Pologne")
st.write("15/03 : Deux journalistes travaillant pour Fox News tués près de Kiev")
st.write(
    "16/03 : Un théâtre abritant « des centaines de civils » visé par une frappe aérienne russe dans le port assiégé de Marioupol"
)
st.write(
    "03/04 : La région de Kiev a été « libérée de l'envahisseur » / les crimes russes découverts à Boutcha"
)
st.write("14/04 : Naufrage du navire russe, le « Moskva »")
st.write(
    "30/05 : Un journaliste français, Frédéric Leclerc-Imhoff, a été tué lundi près de Severodonetsk, dans l'est de Ukraine"
)
st.write(
    "27/06 : Une frappe de missile russe sur un centre commercial dans le centre de l'Ukraine, faisant au moins 13 morts et plus de 40 blessés / un bombardement russe à Lisichansk, Huit civils tués et 21 blessés"
)
st.write("")

# line plot evolution du nb de tweets par jour - topic 3
st.subheader("**Topic 3 :** PERSONNALITÉS PRÉSIDENTIELLES ")

tpd_topic3 = (
    df_topic_lemma3_acdate[df_topic_lemma3_acdate["dominant_topic"] == 2]
    .groupby("date")["tweet_id"]
    .count()
    .reset_index()
)
fig3 = px.line(tpd_topic3, x="date", y="tweet_id")
st.plotly_chart(fig3, use_container_width=True)
st.write("Rapprochement des pics avec l'actualité")
st.write(
    "22/02 : Joe Biden a dénoncé « le début d'une invasion russe de l'Ukraine », annonçant que les Etats-Unis continueraient à fournir des armes « défensives » à l'Ukraine"
)
st.write(
    "24/02 : Vladimir Poutine annonce des opérations militaires contre l'Ukraine en vidéo / Echange téléphonique « franc » entre Poutine et Macron au sujet de l'opération militaire lancée par Moscou en Ukraine / Joe Biden annonce des sanctions : « Poutine sera un paria sur la scène internationale »"
)
st.write(
    "05/03 : Vladimir Poutine met en garde contre une zone d'exclusion aérienne : la Russie considérerait comme cobelligérant tout pays tentant d'imposer une zone d'exclusion aérienne au-dessus de l'Ukraine"
)
st.write("16/03 : Joe Biden, a qualifié Poutine de « criminel de guerre »")
st.write(
    "24/03 : Sommets du G7 et de l'Otan à Bruxelles. Emmanuel Macron a mis en garde contre une crise alimentaire « gravissime » dans plusieurs régions du monde en raison de ce conflit. / Le président Ukrainien s'est adressé aux chefs d'Etat et de gouvernement de l'Alliance atlantique, réunis en sommet extraordinaire à Bruxelles, réclamant « une aide militaire sans restriction » pour l'Ukraine"
)
st.write(
    "15/05 : Le président ukrainien Volodymyr Zelensky a souligné que la « situation dans le Donbass reste très difficile » et que « les troupes russes tentent d'y obtenir au moins une victoire ». / La Finlande va demander à adhérer à l'Otan, conséquence directe de l'invasion russe. La Suède devrait suivre malgré les avertissements de Vladimir Poutine envers son voisin"
)
st.write(
    "16/06 : Le chef de l'Etat s'est exprimé dans une interview diffusée au 20 Heures de TF1 : « C'est notre devoir de nous tenir aux côtés de l'Ukraine »"
)
st.write("")
