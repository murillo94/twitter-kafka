# twitter-kafka

Tweets streaming process from Twitter to Kafka and text (tweet) sentiment analysis.

## Running locally

- You must have Java installed.
- You must have an account in `Google Cloud Platform` and generate an `auth.json` to sentiment analysis API and put in the root of the project.

1 - Install Apache Kafka

```
https://www.apache.org/dyn/closer.cgi?path=/kafka/2.2.0/kafka_2.12-2.2.0.tgz
```

2 -Initialize Zookeeper

```
cd kafka_2.12-2.2.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

3 - Initialize Kafka

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

7 - Running `producer`

```
python producer.py
```

8 - Running `consumer`

#### Python

```
python consumer.py
```

#### Node

```
npm i
```

and

```
node consumer.js
```
