from kafka import KafkaConsumer
import json
import time

# ✅ WAIT for Kafka (this is the missing piece)
while True:
    try:
        consumer = KafkaConsumer(
            'user_activity',
            bootstrap_servers='kafka:9092',
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        print("Connected to Kafka!")
        break
    except:
        print("Waiting for Kafka...")
        time.sleep(5)

print("Listening for messages...\n")

for message in consumer:
    data = message.value
    print(f"Received: {data}")

    if data["value"] > 90:
        print("⚠️ ALERT: High value activity detected!")
