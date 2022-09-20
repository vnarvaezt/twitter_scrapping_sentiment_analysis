import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from src.preprocessing.tools_preprocessing import *
from src.preprocessing.preprocessing_main import *

# todo : replace by a relative path
path = "C:/Users/vnarv/PycharmProjects/twitter_text_mining/"
os.chdir(path)
raw_data = read_files(os.path.join(path, "data/test/"))
print(raw_data.shape)
df = transform_dates(raw_data)
df = preprocessing(df)
print("done")

# vectorization
vectorizer = CountVectorizer(max_df=0.95, min_df=0.01)
X = vectorizer.fit_transform(df["text_lemma"])

print(f"this is the vocabulary : {vectorizer.get_feature_names_out()}")
print(f"vocabulary length: {len(vectorizer.get_feature_names_out())}")
print(f"X shape {X.toarray().shape}")

df_lemma = pd.DataFrame(X.toarray(),
                        columns=vectorizer.get_feature_names_out())

df_lemma.sum().sort_values(ascending=False)
df_lemma.sum().value_counts(normalize=True).sort_values(ascending=False)