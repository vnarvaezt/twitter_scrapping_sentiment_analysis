import pandas as pd

from src.model.modelling import run_all

if __name__ == "__main__":
    path = "C:/Users/vnarv/PycharmProjects/twitter_text_mining/"
    # import preprocessed data
    data = pd.read_csv(path + "/data/min_retweet_3/df_prepro.csv", sep=";")

    # run_all(data.copy(deep=True), "text_lemma", "lemma", True)
    run_all(data.copy(deep=True), "text_lemma", "lemma", False, 3)
    run_all(data.copy(deep=True), "text_lemma", "lemma", False, 4)
