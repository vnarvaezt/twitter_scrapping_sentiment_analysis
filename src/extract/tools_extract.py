from datetime import timedelta
import re
import time
import pandas as pd
import snscrape.modules.twitter as sns_twitter


def _datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta


def _make_request(start_dt, start_epoch_time, end_epoch_time, max_count):
    # Creating list to append tweet data to
    tweets_list = []
    search_query = f"#Ukraine since:{start_dt} since_time:{start_epoch_time} until_time:{end_epoch_time} lang:fr -min_retweets:10"
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(
        sns_twitter.TwitterSearchScraper(search_query).get_items()
    ):
        if i > max_count:
            break
        tweets_list.append(
            [
                tweet.date,
                tweet.id,
                tweet.content,
                tweet.user.username,
                tweet.likeCount,
                tweet.retweetCount,
                tweet.replyCount,
                tweet.quoteCount,
            ]
        )
    cols_names = [
        "datetime",
        "tweet_id",
        "text",
        "username",
        "like_count",
        "retweet_count",
        "reply_count",
        "quote_count",
    ]

    df = pd.DataFrame(tweets_list, columns=cols_names)
    return df


def _save_file(df, root_file, name_file):
    name_file = re.sub("[:-]", "", name_file)
    try:
        df.to_csv(
            f"{root_file}{name_file}.txt", header=None, index=None, sep=" ", mode="w"
        )
    except Exception as error_message:
        print(error_message)


# Creating list to append tweet data to:
# Inputs
def extract_tweets(
    perimeter,
    max_count=50,
    max_lines=5000,
    time_window=29,
    main_path="~/PycharmProjects/twitter_text_mining/data/max_retweet_10/",
):

    """
    Perimeter : time period
    max_count : Max tweets per time period
    max lines : Max number of lines before saving the file
    time_window : Window (in minutes) to extract tweets from
    """
    counter = 0

    df_tweets_total = pd.DataFrame(
        columns=[
            "datetime",
            "tweet_id",
            "text",
            "username",
            "like_count",
            "retweet_count",
            "reply_count",
            "quote_count",
        ]
    )
    for dt in perimeter:
        # add time_window to date
        max_interval = dt + timedelta(minutes=time_window)
        tmp_path = f"tw_{dt.date()}_{dt.time()}_{max_interval.time()}"

        print(
            f"... Extracting tweets from {dt.date()}, from {dt.time()} to {max_interval.time()}"
        )
        df_tweets = _make_request(
            dt.date(), int(dt.timestamp()), int(max_interval.timestamp()), max_count
        )
        df_tweets_total = df_tweets_total.append(df_tweets)
        df_tweets_total = df_tweets_total.reset_index(drop=True)

        counter += df_tweets.shape[0]
        time.sleep(5)

        # if more than 1000 tweets already on df, save file
        print(f"counter {counter}")
        if counter > max_lines:
            print("saving file")
            print(df_tweets_total)
            _save_file(df_tweets_total, main_path, tmp_path)
            counter = 0
            df_tweets_total = pd.DataFrame()
        else:
            pass
        # save data if dt equals the last item
        if dt == perimeter[-1]:
            print("last one")
            _save_file(df_tweets_total, main_path, tmp_path)

    return df_tweets_total


def split_dates(start, end, nb_splits, window_size):
    all_dates = [
        dt for dt in _datetime_range(start, end, timedelta(minutes=window_size))
    ]
    sublist_length = len(all_dates) // nb_splits
    list_dates = [
        all_dates[i : i + sublist_length]
        for i in range(0, len(all_dates), sublist_length)
    ]
    return list_dates
