#imprt Modules
import tweepy
import time

#Authentication Keys
auth = tweepy.OAuthHandler('Api Key', 'APi secret key')
auth.set_access_token('acces token', 'access token secret')

#Don't Get Banned Add Time Limit For Making Request Through API
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Authenticate
user = api.me()


#Serach For Tweet To Like or Retweet
search = 'Python'
numberTweets = 500

#Loop Through All The Tweets in the (numberTweets) range
for tweet in tweepy.Cursor(api.search, search).items(numberTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(3)
        print('Tweet Retweeted')
        tweet.Retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
