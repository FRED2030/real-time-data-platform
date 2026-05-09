from kafka import KafkaProducer
import json
import time
import random

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka-service:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka!")
        break
    except:
        print("Waiting for Kafka...")
        time.sleep(5)

users = ["user1", "user2", "user3"]
activities = ["login", "logout", "purchase"]

while True:
    data = {
        "user": random.choice(users),
        "activity": random.choice(activities),
        "value": random.randint(1, 100)
    }

    producer.send("user_activity", data)
    print(f"Sent: {data}")

    time.sleep(2)
