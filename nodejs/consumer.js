const ConfigParser = require('configparser');
const language = require('@google-cloud/language');
const { SimpleConsumer } = require('no-kafka');

const config = new ConfigParser();
config.read('../config.cfg');

KAFKA_TOPIC = config.get('Kafka', 'topic');
KAFKA_ENDPOINT_PORT = config.get('Kafka', 'kafka_endpoint_port');
GOOGLE_APPLICATION_CREDENTIALS = config.get(
  'GCP',
  'google_application_credentials'
);

process.env['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_APPLICATION_CREDENTIALS;

const clientGoogle = new language.LanguageServiceClient();

function initKafka() {
  const consumer = new SimpleConsumer({
    connectionString: `localhost:${KAFKA_ENDPOINT_PORT}`
  });

  const data = messageKafka => {
    messageKafka.forEach(async ({ message }) => {
      const value = message.value.toString('utf8');
      const { text } = JSON.parse(value);

      if (text) await analyzeText(text);
    });
  };

  return consumer.init().then(() => {
    return consumer.subscribe(KAFKA_TOPIC, data);
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
  console.log(`Magnitude: ${magnitude}\n`);
}

initKafka();
