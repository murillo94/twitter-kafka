from kafka import KafkaConsumer
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.cfg')

KAFKA_TOPIC = config.get('Kafka', 'topic')

consumer = KafkaConsumer(KAFKA_TOPIC)
for msg in consumer:
    print(msg)
