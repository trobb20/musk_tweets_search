# Makes the elon_db.csv file by just getting his tweets (date, link, content)
# Teddy Robbins 2022

import pandas as pd
import numpy as np


def make_elon_csv(fname: str):
    files = ['database/20'+str(i+10)+'.csv' for i in range(13)]

    tweets = []
    links = []
    dates = []

    for i, file in enumerate(files):
        print('Looking at %d'%i)
        tweet_year = pd.read_csv(file)
        elon_tweets_year = tweet_year[tweet_year['username']=='elonmusk']
        dates = dates + list(elon_tweets_year['date'].values)
        links = links + list(elon_tweets_year['link'].values)
        tweets = tweets + list(elon_tweets_year['tweet'].values)

    df = pd.DataFrame(columns=['Date', 'Link', 'Tweet'], data=np.array([dates, links, tweets]).T)
    df.to_csv(fname)