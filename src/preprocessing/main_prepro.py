import os
import time
import pandas as pd

#from langdetect import detect, DetectorFactory
from src.preprocessing.preprocessing import preprocessing
from src.preprocessing.tools_preprocessing import read_files, transform_dates


if __name__ == "__main__":
    path = "C:/Users/vnarv/PycharmProjects/twitter_text_mining/"

    start = time.time()
    # read files
    raw_data = read_files(os.path.join(path, "data/min_retweet_10/"))
    print(raw_data.shape)
    #df_2 = read_files(os.path.join(path, "data/max_retweet_10/"))
    #print(df_2.shape)
    #raw_data = pd.concat([df_1, df_2], axis=0)
    #print(raw_data.shape)

    # drop_duplicates
    raw_data = raw_data.drop_duplicates(["text", "username"])
    print(f"Shape after dropping duplicates {raw_data.shape}")

    # format dates
    data = transform_dates(raw_data)
    # clean tweets
    data = preprocessing(data)
    # save resulting df
    data.to_csv(
        "~/PycharmProjects/twitter_text_mining/data/min_retweet_10/df_prepro.csv",
        sep=";",
        index=False,
    )

    end = time.time()
    delta = (end - start)/60

    print(f"Preprocessing took {delta:.2} minutes")
