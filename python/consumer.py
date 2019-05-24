import configparser
import json
import six
import os
from google.cloud import language
from google.cloud.language import enums
from kafka import KafkaConsumer

config = configparser.RawConfigParser()
config.read('../config.cfg')

KAFKA_TOPIC = config.get('Kafka', 'topic')
GOOGLE_APPLICATION_CREDENTIALS = config.get(
    'GCP', 'google_application_credentials')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS


def main():
    consumer = KafkaConsumer(KAFKA_TOPIC)
    client = language.LanguageServiceClient()

    for msg in consumer:
        output = []
        output.append(json.loads(msg.value))

        if 'text' in output[0]:
            content = output[0]['text']

            if isinstance(content, six.binary_type):
                content = content.decode('utf-8')

            type_ = enums.Document.Type.PLAIN_TEXT
            document = {'type': type_, 'content': content}

            response = client.analyze_sentiment(document)
            sentiment = response.document_sentiment

            print(f'Text: {content}')
            print(f'Score: {sentiment.score}')
            print(f'Magnitude: {sentiment.magnitude}\n')


if __name__ == "__main__":
    main()
