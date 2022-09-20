from langdetect import detect
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import nltk
import re
from unidecode import unidecode


def preprocessing(df, verbose=False):

    # lower case tweets
    df["text"] = df["text"].str.lower()

    df["hashtags"] = df["text"].apply(lambda y: [x.group() for x in re.finditer(r'#[a-zA-Z]+', y)])
    # Find all @
    df["arrobas"] = df["text"].apply(lambda y: [x.group() for x in re.finditer(r'@[a-zA-Z]+', y)])

    # replace https links with "link"
    regex_http = r'([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#\.]?[\w-]+)*\/?'
    df["text_clean"] = [re.sub(regex_http, '<link>', doc) for doc in df["text"]]

    # replace years with "annee"
    df["text_clean"] = [re.sub(r"[0-9]{4}", "<annee>", doc) for doc in df["text_clean"]]

    # delete accents and emojis
    df["text_clean"] = [unidecode(doc) for doc in df["text_clean"]]

    # replace all non alphabetic chars with an space
    df["text_clean"] = [re.sub(r"[^a-z<>]+", ' ', doc) for doc in df["text_clean"]]

    # detect language
    tweet_lg = []
    for row in df["text_clean"]:
        tw_lang = detect(row)
        tweet_lg.append(tw_lang)

    # store language into a column
    df["language"] = tweet_lg

    # filter only french tweets
    is_french = "fr"
    df = df[df["language"] == is_french]

    # recover french stopwords
    nltk.download('stopwords')
    french_stopwords_list = stopwords.words('french')
    df["text_clean"] = [' '.join([word for word in doc.split() if word not in french_stopwords_list]) for doc in
                        df["text_clean"]]

    # stem text
    stemmer = SnowballStemmer('french')
    df["text_stem"] = [" ".join([stemmer.stem(word) for word in doc.split()]) for doc in df["text_clean"]]

    # lemmatize text
    lemmatizer = FrenchLefffLemmatizer()
    df["text_lemma"] = [" ".join([lemmatizer.lemmatize(word) for word in doc.split()]) for doc in df["text_clean"]]

    #todo: filter 1 syllables
    return df
