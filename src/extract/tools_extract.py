from datetime import datetime, timedelta
import pandas as pd
import re
import snscrape.modules.twitter as sntwitter
import time


def _datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


def _make_request(start_dt, start_epoch_time, end_epoch_time, max_count):
    # Creating list to append tweet data to
    tweets_list = []
    search_query = f'#Ukraine since:{start_dt} since_time:{start_epoch_time} until_time:{end_epoch_time} lang:fr min_retweets:10'
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(search_query).get_items()):
        if i > max_count:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.content,
                            tweet.user.username, tweet.likeCount,
                            tweet.retweetCount, tweet.replyCount,
                            tweet.quoteCount])
    cols_names = ['datetime', 'tweet_id', 'text',
                  'username', 'like_count', 'retweet_count',
                  'reply_count', 'quote_count']

    df = pd.DataFrame(tweets_list, columns=cols_names)
    return df


def _save_file(df, root_file, name_file):
    name_file = re.sub("[:-]", "", name_file)
    try:
        df.to_csv(f"{root_file}{name_file}.txt",
                  header=None,
                  index=None,
                  sep=' ',
                  mode='w')
    except Exception as e:
        print(e)


# Creating list to append tweet data to
# Inputs
def extract_tweets(perimeter,
                   max_count=50,
                   max_lines=5000,
                   time_window=29,
                   main_path="C:/Users/vnarv/PycharmProjects/text_mining/"):
    # perimeter = arg
    # max_count = 10
    """
    Perimeter : time period
    max_count : Max tweets per time period
    max lines : Max number of lines before saving the file
    time_window : Window (in minutes) to extract tweets from
    """
    counter = 0

    df_tweets_total = pd.DataFrame(columns=['datetime', 'tweet_id', 'text',
                                            'username', 'like_count', 'retweet_count',
                                            'reply_count', 'quote_count'])
    for dt in perimeter:
        x = dt + timedelta(minutes=time_window)
        tmp_path = f"tw_{dt.date()}_{dt.time()}_{x.time()}"
        # tmp_path = re.sub("[-:]", "", tmp_path)

        print(f"... Extracting tweets from {dt.date()}, from {dt.time()} to {x.time()}")
        df_tweets = _make_request(dt.date(), int(dt.timestamp()), int(x.timestamp()), max_count)
        df_tweets_total = df_tweets_total.append(df_tweets)
        df_tweets_total = df_tweets_total.reset_index(drop=True)

        counter += df_tweets.shape[0]
        time.sleep(5)

        # if more than 1000 tweets already on df, save file
        print(f"counter {counter}")
        if counter > max_lines:
            print("saving file")
            print(df_tweets_total)
            _save_file(df_tweets_total,
                       main_path,
                       tmp_path)
            counter = 0
            df_tweets_total = pd.DataFrame()
        else:
            pass
        # save data if dt equals the last item
        if dt == perimeter[-1]:
            print("last one")
            _save_file(df_tweets_total,
                       main_path,
                       tmp_path)

    return df_tweets_total


def split_dates(start, end, nb_splits, window_size):
    all_dates = [dt for dt in _datetime_range(
        start, end, timedelta(minutes=window_size)
    )]
    sublist_length = len(all_dates) // nb_splits
    return [all_dates[i:i + sublist_length] for i in range(
        0, len(all_dates), sublist_length
    )]


start_date = datetime(2022, 2, 1, 7)
#end_date = date.today()
end_date = datetime(2022, 2, 28, 00, 59)
#end_date = datetime(2022, 3, 31, 00, 59)
test = split_dates(start_date, end_date, 6, 30)


import multiprocessing
from multiprocessing import Pool

if __name__ == '__main__':
    start = time.time()
    with Pool(multiprocessing.cpu_count() - 2) as p:
        p.map(extract_tweets, test)
    end = time.time()
    delta = end - start
    print(f"took {delta:.2} seconds using multiprocessing")



# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))
