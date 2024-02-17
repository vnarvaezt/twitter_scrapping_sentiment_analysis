import re

import nltk
from french_lefff_lemmatizer.french_lefff_lemmatizer import \
    FrenchLefffLemmatizer
from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from unidecode import unidecode

from src.preprocessing.stopwords import stopwords as other_stopwords
from src.preprocessing.tools_preprocessing import generate_ngrams


def preprocessing(df, verbose=True):

    # lower case tweets
    df["text"] = df["text"].str.lower()
    # store all hashtags into a column
    df["hashtags"] = df["text"].apply(
        lambda y: [x.group() for x in re.finditer(r"#[a-zA-Z]+", y)]
    )
    # Find all @
    df["arrobas"] = df["text"].apply(
        lambda y: [x.group() for x in re.finditer(r"@[a-zA-Z]+", y)]
    )
    # find https links and replace by ""
    regex_http = (
        r"([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#\.]?[\w-]+)*\/?"
    )
    # df["text_clean"] = [re.sub(regex_http, '<link>', doc) for doc in df["text"]]
    df["text_clean"] = [re.sub(regex_http, "", doc) for doc in df["text"]]
    # replace years with "annee"
    # df["text_clean"] = [re.sub(r"[0-9]{4}", "<annee>", doc) for doc in df["text_clean"]]
    df["text_clean"] = df["text_clean"].apply(lambda x: re.sub(r"[0-9]{4}", "", x))
    # delete accents and emojis
    df["text_clean"] = df["text_clean"].apply(lambda x: unidecode(x))
    # replace all non alphabetic chars with an space
    df["text_clean"] = df["text_clean"].apply(lambda x: re.sub(r"[^a-z]+", " ", x))
    # delete empty tweets
    df = df[(df["text_clean"] != " ")]
    # delete any nan values
    df = df[~df["text_clean"].isna()]

    # detect language
    tweet_lg = []
    for row in df["text_clean"]:
        tw_lang = detect(row)
        tweet_lg.append(tw_lang)

    # store language into a column
    df["language"] = tweet_lg
    if verbose:
        other_lang = df[df["language"] != "fr"]
        nb_other_lang = other_lang.groupby("language")["tweet_id"].nunique()
        print(f"Nb of tweets detected in other language {nb_other_lang}")
        print(other_lang[["text_clean", "language"]].iloc[:10])

    # filter only french tweets
    is_french = "fr"
    df = df[df["language"] == is_french]

    # recover french stopwords
    nltk.download("stopwords")
    french_stopwords_list = stopwords.words("french")
    all_stopwords_list = french_stopwords_list + list(other_stopwords)

    df["text_clean"] = df["text_clean"].apply(
        lambda x: " ".join(
            [word for word in x.split() if word not in all_stopwords_list]
        )
    )
    # filter words with less than 1 syllables
    df["text_clean"] = df["text_clean"].apply(
        lambda x: " ".join([word for word in x.split() if len(word) > 1])
    )
    # drop duplicates
    print(f"Shape before dropping dups: {df.shape}")
    df = df.drop_duplicates(["text_clean", "username"])
    print(f"Shape after dropping dups: {df.shape}")
    # stem text
    stemmer = SnowballStemmer("french")
    df["text_stem"] = df["text_clean"].apply(
        lambda x: " ".join([stemmer.stem(word) for word in x.split()])
    )

    df["text_stem_bigram"] = df["text_stem"].apply(
        lambda x: " ".join([word for word in generate_ngrams(x, 2) if len(word) > 1])
    )

    df["text_stem_trigram"] = df["text_stem"].apply(
        lambda x: " ".join([word for word in generate_ngrams(x, 3) if len(word) > 1])
    )

    # lemmatize text
    lemmatizer = FrenchLefffLemmatizer()
    df["text_lemma"] = df["text_clean"].apply(
        lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()])
    )

    df["text_lemma_bigram"] = df["text_lemma"].apply(
        lambda x: " ".join([word for word in generate_ngrams(x, 2) if len(word) > 1])
    )

    df["text_lemma_trigram"] = df["text_lemma"].apply(
        lambda x: " ".join([word for word in generate_ngrams(x, 3) if len(word) > 1])
    )

    return df
