from flask import Flask, render_template
from tweeter import Tweeter
from os import environ

app = Flask(__name__)

tweetObject = Tweeter("#MLHLocalhost",20)
tweetObject.scrapeTweets()

@app.route('/')
def homepage():
    return render_template('index.html', tweets=tweetObject.getTweets())

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, port=port)