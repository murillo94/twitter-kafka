from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('topic', b'test')
result = future.get(timeout=60)
