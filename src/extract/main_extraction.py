import multiprocessing
import os
import time
from datetime import datetime
from multiprocessing import Pool

from src.extract.tools_extract import extract_tweets, split_dates


if __name__ == "__main__":
    start_date = datetime(2022, 2, 1, 7)
    # end_date = date.today()
    end_date = datetime(2022, 9, 2, 1, 7)
    # end_date = datetime(2022, 2, 2, 1, 7)

    # end_date = datetime(2022, 3, 31, 00, 59)
    test = split_dates(start_date, end_date, 6, 30)
    start = time.time()
    with Pool(multiprocessing.cpu_count() - 2) as p:
        p.map(extract_tweets, test)
    end = time.time()

    delta = (end - start) / 60
    print(f"Extraction took {delta:.2} minutes using multiprocessing")
