const ConfigParser = require('configparser');
const language = require('@google-cloud/language');
const { Consumer, KafkaClient } = require('kafka-node');

const config = new ConfigParser();
config.read('../config.cfg');

KAFKA_TOPIC = config.get('Kafka', 'topic');
KAFKA_ENDPOINT_PORT = config.get('Kafka', 'kafka_endpoint_port');
GOOGLE_APPLICATION_CREDENTIALS = config.get(
  'GCP',
  'google_application_credentials'
);

process.env['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS;

const clientKafka = new KafkaClient({
  kafkaHost: `localhost:${KAFKA_ENDPOINT_PORT}`
});
const clientGoogle = new language.LanguageServiceClient();

async function runKafka() {
  const topics = [{ topic: KAFKA_TOPIC }];
  const options = {
    autoCommit: false,
    fetchMaxWaitMs: 1000,
    fetchMaxBytes: 1024 * 1024
  };

  const consumer = new Consumer(clientKafka, topics, options);

  consumer.on('message', async ({ value }) => {
    const { text } = JSON.parse(value);
    await analyzeText(text);
  });

  consumer.on('error', err => {
    console.log('error', err);
  });
}

async function analyzeText(text) {
  const document = {
    content: text,
    type: 'PLAIN_TEXT'
  };

  const [result] = await clientGoogle.analyzeSentiment({ document });
  const { score, magnitude } = result.documentSentiment;

  console.log(`Text: ${text}`);
  console.log(`Score: ${score}`);
  console.log(`Magnitude: ${magnitude}`);
}

runKafka();
