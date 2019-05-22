import configparser
import json
from kafka import KafkaConsumer

config = configparser.RawConfigParser()
config.read('config.cfg')

KAFKA_TOPIC = config.get('Kafka', 'topic')


def main():
    consumer = KafkaConsumer(KAFKA_TOPIC)

    for msg in consumer:
        output = []
        output.append(json.loads(msg.value))

        if 'text' in output[0]:
            print(output[0]['text'])
            print('\n')


if __name__ == "__main__":
    main()
