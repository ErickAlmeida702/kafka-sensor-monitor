import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

SENSOR_IDS = ['sensor_1', 'sensor_2', 'sensor_3']


def generate_sensor_data():
    return {
        'sensor_id': random.choice(SENSOR_IDS),
        'temperature': round(random.uniform(20.0, 40.0), 2),
        'humidity': round(random.uniform(10.0, 90.0), 2),
        'timestamp': datetime.utcnow().isoformat()
    }


if __name__ == '__main__':
    while True:
        data = generate_sensor_data()
        print(f"Enviando: {data}")
        producer.send('sensor-data', value=data)
        time.sleep(2)
