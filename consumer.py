from kafka import KafkaConsumer
import twitter

# https://developer.twitter.com/en/apps


class Twitter:
    def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None)
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.access_token = access_token
    self.access_token_secret = access_token_secret

    def authenticate(self):
        api = twitter.Api(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token, access_token_secret=self.access_token_secret)
        return api

    def getTimeline(self):
        for tweet in authenticate().GetHomeTimeline():
            print(tweet.text)
