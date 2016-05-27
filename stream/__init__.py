import tweepy
import json
from datetime import datetime

class TweetListener(tweepy.StreamListener):
    '''TweetStreamer
    An overloaded StreamListener to handle tweets
    given our data handler
    '''

    def __init__(self, handler):
        '''__init__
        Initializes the tweet handler with
        the data handler given.

            handler (class) -> Must have a .push_tweet(tweet_json)
                method.
        '''
        self.start       = datetime.utcnow()
        self.tweets_seen = 0
        self.errors      = 0
        self.handler     = handler

    def stats(self):
        '''stats
        Returns the number of time elapsed since
        starting, the number of tweets seen, the
        start time, and the rate of tweets/sec
        '''
        stat = {
            "seen":      self.tweets_seen,
            "errors":    self.errors,
            "start_utc": self.start.strftime("%H:%S %Z %d-%m-%Y"),
            "elapsed":   (datetime.utcnow() - self.start).total_seconds()
        }
        stat['rate'] = stat['seen']/stat['elapsed']
        return stat

    def on_data(self, data):
        '''on_data
        Defines the response to recieving a
        tweet. Just pushes the tweet to the
        handler set during instantiation.

            data (json) -> tweet data
        '''
        self.tweets_seen += 1
        try:
            self.handler.push_tweet(json.loads(data))
        except:
            # ignore errors. Almost always will be from Twitter
            # not passing an expected field.
            self.errors += 1

