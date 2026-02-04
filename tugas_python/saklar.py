import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

while True:
    cmd = input("Ketik ON / OFF: ")
    client.publish("rumah/lampu", cmd)