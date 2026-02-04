import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_BASE = "kampus/iot"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        suhu_lab = random.uniform(20.0, 25.0)
        suhu_kantin = random.uniform(28.0, 32.0)

        client.publish(f"{TOPIC_BASE}/lab_komputer", f"{suhu_lab:.2f}", qos=1)
        print(f"Mengirim suhu Lab: {suhu_lab:.2f}")

        client.publish(f"{TOPIC_BASE}/kantin", f"{suhu_kantin:.2f}", qos=1)
        print(f"Mengirim suhu Kantin: {suhu_kantin:.2f}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Publisher dihentikan")
    client.loop_stop()
    client.disconnect()