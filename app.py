from flask import Flask, render_template
from tweeter import Tweeter
import os

app = Flask(__name__)

tweetObject = Tweeter("#MLHLocalhost",20)
tweetObject.scrapeTweets()

@app.route('/')
def homepage():
    return render_template('index.html', tweets=tweetObject.getTweets())

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)