from calendar import month_name
from collections import Counter

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import seaborn as sns
from nltk import ngrams
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud


def wordcloud_cols(i, j, data):
    nltk.download("stopwords")
    stopwords_fr = stopwords.words("french")
    for category in data[i].unique():
        wordcloud_col = WordCloud(
            background_color="white",
            stopwords=stopwords_fr,
            max_words=100,
            max_font_size=40,
            random_state=42,
        ).generate(str(data[data[i] == category][j].values))
        plt.imshow(wordcloud_col)
        plt.axis("off")
        plt.title(f"Tweets {month_name[category]} {j}")
        plt.show()


def ngram_top(tokens, n_gram=2, n_top=20):

    list_ngram = list(ngrams(tokens, n_gram))
    counter = Counter(list_ngram)
    ngram_plot = pd.DataFrame(counter.most_common(n_top))
    plt.figure(figsize=(15, 10))
    plot = sns.barplot(x=ngram_plot[1], y=ngram_plot[0], color="#44546a")

    plt.xlabel("occurrence")
    plt.ylabel("n_gram")
    plt.title(f"top {n_top}")
    plt.show()


def get_top_n_words(n_top_words, count_vectorizer, text_data):
    """
    returns a tuple of the top n words in a sample and their
    accompanying counts, given a CountVectorizer object and text sample
    """
    vectorized_headlines = count_vectorizer.fit_transform(text_data.values)
    vectorized_total = np.sum(vectorized_headlines, axis=0)
    word_indices = np.flip(np.argsort(vectorized_total)[0, :], 1)
    word_values = np.flip(np.sort(vectorized_total)[0, :], 1)

    word_vectors = np.zeros((n_top_words, vectorized_headlines.shape[1]))
    for i in range(n_top_words):
        word_vectors[i, word_indices[0, i]] = 1

    words = [
        word[0].encode("ascii").decode("utf-8")
        for word in count_vectorizer.inverse_transform(word_vectors)
    ]

    return (words, word_values[0, :n_top_words].tolist()[0])


def get_tfidf_top_features(documents, n_top=10):

    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=300)
    tfidf = tfidf_vectorizer.fit_transform(documents)
    importance = np.argsort(np.asarray(tfidf.sum(axis=0)).ravel())[::-1]
    tfidf_feature_names = np.array(tfidf_vectorizer.get_feature_names())

    return tfidf_feature_names[importance[:n_top]]
