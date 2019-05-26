# twitter-kafka

Tweets streaming process from Twitter to Kafka and text (tweet) sentiment analysis.

## Running locally

- You must have Java installed.
- You must have an account in [Google Cloud Platform](https://cloud.google.com/) and generate an [auth.json](https://cloud.google.com/natural-language/docs/quickstart-client-libraries) to sentiment analysis API and put in the root of the project.

1 - Install Apache Kafka

```
https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz
```

2 -Init Zookeeper

```
cd kafka_2.12-2.2.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

3 - Init Kafka

```
bin/kafka-server-start.sh config/server.properties
```

4 - Create a topic

```
bin/kafka-topics.sh --create --topic topic --partitions 1 --zookeeper localhost:2181 --replication-factor 1
```

5 - Verify if topic was created

```
bin/kafka-topics.sh --describe --topic topic --zookeeper localhost:2181
```

6 - Install repo packages and run inside `python` folder (you must have pipenv installed)

```
pipenv install
```

and

```
pipenv shell
```

7 - Running `producer` (go to python folder)

```
python producer.py --keyword <some_text_here>
```

8 - Running `consumer`

#### Python (go to python folder)

```
python consumer.py
```

#### Node (go to node folder)

```
npm i
```

and

```
node consumer.js
```
