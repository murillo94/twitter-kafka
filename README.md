# twitter-kafka

Tweets streaming process from Twitter to Kafka and text (tweet) sentiment analysis.

## Running locally

You must have Java installed.

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

6 - Install repo packages (you must have pipenv installed)

```
pipenv install
```

7 - Run pipenv

```
pipenv shell
```

8 - Run commands (all in pipenv)

```
First terminal: python producer.py
Second terminal: python consumer.py
```
