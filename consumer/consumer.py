from kafka import KafkaConsumer
from prometheus_client import start_http_server, Counter
import json
import time

messages_received = Counter(
    'messages_received_total',
    'Total messages received'
)

high_value_alerts = Counter(
    'high_value_alerts_total',
    'Total high value alerts'
)

start_http_server(8001)

while True:
    try:
        consumer = KafkaConsumer(
            'user_activity',
            bootstrap_servers='kafka:9092',
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        print("Connected to Kafka!", flush=True)
        break

    except Exception as e:
        print(f"Waiting for Kafka... {e}", flush=True)
        time.sleep(5)

print("Listening for messages...", flush=True)

for message in consumer:
    data = message.value

    messages_received.inc()

    print(f"Received: {data}", flush=True)

    if data["value"] > 80:
        high_value_alerts.inc()
        print("⚠️ ALERT: High value activity detected!", flush=True)
