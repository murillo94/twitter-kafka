import configparser
import click
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

config = configparser.RawConfigParser()
config.read('../config.cfg')

CONSUMER_KEY = config.get('Twitter', 'consumer_key')
CONSUMER_SECRET = config.get('Twitter', 'consumer_secret')
ACCESS_TOKEN = config.get('Twitter', 'access_token')
ACCESS_TOKEN_SECRET = config.get('Twitter', 'access_token_secret')
KAFKA_ENDPOINT = config.get('Kafka', 'kafka_endpoint_port')
KAFKA_TOPIC = config.get('Kafka', 'topic')

client = KafkaClient(f'localhost:{KAFKA_ENDPOINT}')
producer = SimpleProducer(client)


class Listener(StreamListener):
    def on_data(self, data):
        producer.send_messages(KAFKA_TOPIC, data.encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)


@click.command()
@click.option('--keyword', '-k', help='Insert a keyword', required=True)
def searchTweets(keyword):

    listen = Listener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listen)
    stream.filter(track=str(keyword))


if __name__ == "__main__":
    searchTweets()
