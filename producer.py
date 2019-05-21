# https://developer.twitter.com/en/apps

from kafka import KafkaProducer
import ConfigParser
import twitter

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

CONSUMER_KEY = config.get('Twitter', 'consumer_key')
CONSUMER_SECRET = config.get('Twitter', 'consumer_secret')
ACCESS_TOKEN = config.get('Twitter', 'access_token')
ACCESS_TOKEN_SECRET = config.get('Twitter', 'access_token_secret')
TWITTER_STREAMING_MODE = config.get('Twitter', 'streaming_mode')
KAFKA_ENDPOINT = '{0}:{1}'.format(config.get(
    'Kafka', 'kafka_endpoint'), config.get('Kafka', 'kafka_endpoint_port'))
KAFKA_TOPIC = config.get('Kafka', 'topic')
NUM_RETRIES = 3


class Twitter:
    def __init__(self, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.access_token = access_token
    self.access_token_secret = access_token_secret

    def authenticate(self):
        api = twitter.Api(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token, access_token_secret=self.access_token_secret)
        return api

    def get_timeline(self):
        for tweet in authenticate().GetHomeTimeline():
            print(tweet.text)


class Producer(self):
    producer = KafkaProducer(bootstrap_servers=KAFKA_ENDPOINT)

    def get_data(self, data):
        data_json = json.loads(data)
        str_tweet = data_json['text'].encode('utf-8')
        self.producer.send(KAFKA_TOPIC, str_tweet)
        print(str_tweet)
