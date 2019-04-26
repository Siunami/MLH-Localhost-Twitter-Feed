from flask import Flask, render_template
from tweeter import Tweeter

app = Flask(__name__)

tweetObject = Tweeter()
tweetObject.scrapeTweets()

@app.route('/')
def homepage():
    return render_template('index.html', tweets=tweetObject.getTweets())


















# def tweeter():
    
#     apiKey = 'b1UofmQlFdEDpEfS3tRQ19zIV'

#     apiKeySecret = 'HCZYbEWJmOYzMVNWMqw8bmJyNz8iIJnXZlI1nQEfa9mi03ceiT'
#     accessToken = "4741976232-3RtQpqwvz1EtjkGMViwst7W6P0xYkXxs9vKVaMx"

#     accessTokenSecret = "pJC3LMc7uJLjRzsEOVw8ihW3KgDLUQ4B8P3qcUudZbJmx"

#     auth = tweepy.OAuthHandler(apiKey, apiKeySecret)
#     auth.set_access_token(accessToken, accessTokenSecret)

#     api = tweepy.API(auth)
#     tweets = []

#     pattern = re.compile("#MLHLocalhost")

#     # https://tweepy.readthedocs.io/en/latest/cursor_tutorial.html
#     # Cursor instead of api call
#     # Neex to use tweet_mode and full_text instead of text
#     for tweet in tweepy.Cursor(api.user_timeline,id='mlhacks',tweet_mode='extended').items(10):
#         print(tweet)
#         if pattern.search(tweet.full_text):
#             tweets.append({
#                 "text":tweet.full_text
#             })

#     # for tweet in api.user_timeline("mlhacks"):
#     #     tweets.append({
#     #         "text":tweet.text
#     #     })
#     return tweets