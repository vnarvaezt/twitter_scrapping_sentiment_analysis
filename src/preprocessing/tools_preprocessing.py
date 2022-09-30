import re
import os
import pandas as pd


# todo : add file path
def read_files(path="", verbose=False):
    print(os.getcwd())
    files = os.listdir(path)

    files_tw = []
    for filename in files:
        try:
            tmp = re.search(r"tw_.*\b", filename)[0]
            if tmp:
                files_tw.append(tmp)
        except TypeError:
            pass

    data = pd.DataFrame()
    for file in files_tw:

        _tx = pd.read_csv(f"{path}{file}", sep=" ")
        _tx.columns = ['datetime', 'tweet_id', 'text',
                       'username', 'like_count', 'retweet_count',
                       'reply_count', 'quote_count']
        if verbose:
            print(f"{file} has {_tx.shape[0]} lines")

        data = pd.concat([data, _tx], axis=0)
    data = data.reset_index(drop=True)

    return data


def transform_dates(df, column="datetime"):
    df[column] = df[column].apply(lambda x: pd.Timestamp(x))
    df["date"] = df[column].dt.date
    df["day"] = df[column].dt.day
    df["month"] = df[column].dt.month
    df["time"] = df[column].dt.time
    df["hour"] = df[column].dt.hour
    df["minute"] = df[column].dt.minute
    return df


def generate_ngrams(s, n):
    tokens = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return ["_".join(ngram) for ngram in ngrams]