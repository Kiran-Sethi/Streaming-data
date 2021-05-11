
# do check for 10000 tweets
# different hashtag frequency
import pandas as pd
import tweepy
import numpy as np
import csv
consumer_key = 'Bax4ngrLGhI3DYNu0mBHnxadu'
consumer_secret = 'X6U4x3lEU5iPwEq4uwnkOrMvJ9WBxHP11XH66EyoUrIPRKXkLM'
access_token = '1387617215671721989-jrmxmoZ84JXlUKFECmwc2ap3Kb5Yjh'
access_secret ='UTsxCTDK7HWLlKQwDsrOSLjjJuL5JkpVVbGbBRYiKdc9f'
tweetsPerQry = 100
maxTweets = 10000
# hashtag = "#mencatatindonesia"

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
maxId = -1
tweetCount = 0

filename = 'scraped_tweets.csv'
with open(filename, "w", encoding="utf-8") as f:
 writer=csv.writer(f)
 writer.writerow("hashtags")

list_l=[]
qi="#oxygen Shortage OR #cowin OR #Ontario OR #Covishield OR #covax OR #Novavax OR #lockdown OR #Hospital OR #sputnik OR #Astrazeneca OR #Covid"
while tweetCount < maxTweets:
        if(maxId <= 0):
                newTweets = api.search(q=qi, count=tweetsPerQry, result_type="recent", tweet_mode="extended")
        else:
                newTweets = api.search(q=qi, count=tweetsPerQry, max_id=str(maxId - 1), result_type="recent", tweet_mode="extended")
        if not newTweets:
                print("Tweet Habis")
                break
        for tweet in newTweets:
                #print("hello")
                hashtags=tweet.entities['hashtags']
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])
                with open(filename, "a", encoding="utf-8") as f:
                        writer=csv.writer(f)
                        writer.writerow(hashtext)
        tweetCount += len(newTweets)
        maxId = newTweets[-1].id
file.close()
