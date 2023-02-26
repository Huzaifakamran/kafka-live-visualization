from kafka import KafkaProducer
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    data = random.randint(0, 10)
    producer.send('topic1', str(data).encode('utf-8'))