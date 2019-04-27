from flask import Flask, render_template
from tweeter import Tweeter

app = Flask(__name__)

tweetObject = Tweeter("#MLHLocalhost",20)
tweetObject.scrapeTweets()

@app.route('/')
def homepage():
    return render_template('index.html', tweets=tweetObject.getTweets())