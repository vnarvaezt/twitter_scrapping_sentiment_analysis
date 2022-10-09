import os

from src.preprocessing.preprocessing import preprocessing
from src.preprocessing.tools_preprocessing import read_files, transform_dates

if __name__ == "__main__":
    path = "C:/Users/vnarv/PycharmProjects/twitter_text_mining/"
    raw_data = read_files(os.path.join(path, "data/max_retweet_10/"))
    print(raw_data.shape)
    data = transform_dates(raw_data)
    data = preprocessing(data)
    data.to_csv(
        "~/PycharmProjects/twitter_text_mining/data/max_retweet_10/df_prepro_V3.csv",
        sep=";",
        index=False,
    )
