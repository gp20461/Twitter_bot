
import tweepy
import time

consumer_key = 'c3AvHOYR0uZnHckoYiOBvnZVM'
consumer_secret = 'jB0tUiZy0fSt6KG3JYtjzKBKygEEt6CfnZm9FjXQp8o3da9zkB'
key = '1295681640455315459-GNm6BezuZ4JyD8OywMWcoNgqCflILq'
secret = 'q0G6SwxfJkPZiqe7Z7iRvlSG566DqHlYxmcBOsFf1Y7YC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #100DaysOfCode!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)
