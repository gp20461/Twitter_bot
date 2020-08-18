import tweepy
import time

consumer_key = 'c3AvHOYR0uZnHckoYiOBvnZVM'
consumer_secret = 'jB0tUiZy0fSt6KG3JYtjzKBKygEEt6CfnZm9FjXQp8o3da9zkB'
key = '1295681640455315459-GNm6BezuZ4JyD8OywMWcoNgqCflILq'
secret = 'q0G6SwxfJkPZiqe7Z7iRvlSG566DqHlYxmcBOsFf1Y7YC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()
