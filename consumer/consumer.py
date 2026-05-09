from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'user_activity',
    bootstrap_servers='kafka-service:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for messages...")

for message in consumer:
    data = message.value

    print(f"Received: {data}")

    if data["value"] > 80:
        print("⚠️ ALERT: High value activity detected!")
