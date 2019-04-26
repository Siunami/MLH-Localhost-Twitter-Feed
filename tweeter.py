import tweepy
import re
from keys import apiKey,apiKeySecret,accessToken,accessTokenSecret

class Tweeter:
    def __init__(self):
        self.api = self.authenticate()
        self.tweets = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return tweepy.API(auth)

    
    def scrapeTweets(self):
        tweets = []
        pattern = re.compile("#MLHLocalhost")

        # https://tweepy.readthedocs.io/en/latest/cursor_tutorial.html
        # Cursor instead of api call
        for tweet in tweepy.Cursor(self.api.user_timeline,id='mlhacks',tweet_mode='extended').items(100):
            if pattern.search(tweet.full_text):
                tweets.append({
                    "text":tweet.full_text,
                    "date":tweet.created_at
                })
        self.tweets = tweets
    
    def getTweets(self):
        return self.tweets
    