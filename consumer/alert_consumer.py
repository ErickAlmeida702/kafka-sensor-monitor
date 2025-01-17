import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='sensor-group'
)

print("Aguardando dados...")

for message in consumer:
    data = message.value
    temp = data['temperature']
    hum = data['humidity']
    print(f"Recebido: {data}")

    if temp > 30:
        print(f"🔥 ALERTA: Temperatura alta! {temp}°C - {data['sensor_id']}")
    if hum < 20:
        print(f"💧 ALERTA: Umidade baixa! {hum}% - {data['sensor_id']}")
