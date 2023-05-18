import time
import random
import paho.mqtt.client as mqtt

topic = "temperatura"  # Tópico MQTT para publicar as leituras de temperatura

client = mqtt.Client()
client.connect("localhost", 1883)  # Conectar ao servidor MQTT

try:
    while True:
        temperatura = random.uniform(0, 240)  # Gerar uma leitura de temperatura aleatória
        client.publish(topic, str(temperatura))  # Publicar a leitura no tópico MQTT
        print("Leitura de temperatura publicada: {:.2f}".format(temperatura))
        time.sleep(1)  # Esperar 1 segundo antes de enviar a próxima leitura
except KeyboardInterrupt:
    client.disconnect()  # Desconectar do servidor MQTT
