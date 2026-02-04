import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    if msg.payload.decode() == "ON":
        print("💡 LAMPU NYALA")
    else:
        print("⚫ LAMPU MATI")

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("rumah/lampu")
client.loop_forever()