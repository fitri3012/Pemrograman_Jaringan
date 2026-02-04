import paho.mqtt.client as mqtt

# Konfigurasi Broker
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "kampus/iot/+"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[SUKSES] Terhubung ke Broker MQTT")
        client.subscribe(TOPIC)
    else:
        print(f"[GAGAL] Kode Error: {rc}")

def on_message(client, userdata, msg):
    lokasi = msg.topic.split("/")[-1]
    nilai = msg.payload.decode()
    print(f"📡 Data dari {lokasi}: {nilai}°C")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print(f"Menghubungkan ke {BROKER}...")
client.connect(BROKER, PORT, 60)

client.loop_forever()