from kafka import KafkaProducer
import json
import time
import random

# Retry until Kafka is ready (VERY important)
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',  # ✅ FIXED
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        break
    except:
        print("Waiting for Kafka...")
        time.sleep(5)

users = ["user1", "user2", "user3"]

while True:
    data = {
        "user": random.choice(users),
        "activity": random.choice(["login", "logout", "purchase"]),
        "value": random.randint(1, 100)
    }

    producer.send("user_activity", data)
    print(f"Sent: {data}")

    time.sleep(1)
