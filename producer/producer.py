from kafka import KafkaProducer
from prometheus_client import start_http_server, Counter
import json
import time
import random

messages_sent = Counter(
    'messages_sent_total',
    'Total messages sent'
)

start_http_server(8000)

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        print("Connected to Kafka!", flush=True)
        break

    except Exception as e:
        print(f"Waiting for Kafka... {e}", flush=True)
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

    messages_sent.inc()

    print(f"Sent: {data}", flush=True)

    time.sleep(2)
