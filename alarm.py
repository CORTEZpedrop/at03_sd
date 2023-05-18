import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    if msg.topic == "aumento_temperatura_repentina":
        print("Alarme: Aumento de temperatura repentina!")

    if msg.topic == "temperatura_alta":
        print("Alarme: Temperatura alta!")

client = mqtt.Client()
client.connect("localhost", 1883)  # Conectar ao servidor MQTT

client.subscribe("aumento_temperatura_repentina")
client.subscribe("temperatura_alta")
client.on_message = on_message

client.loop_forever()  # Manter o serviço em execução esperando as mensagens
