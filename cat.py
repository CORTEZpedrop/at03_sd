import time
import statistics
import paho.mqtt.client as mqtt

topic = "temperatura"  # Tópico MQTT para receber as leituras de temperatura
window_size = 120  # Tamanho da janela de tempo para calcular a média

temperatures = []  # Armazena as leituras de temperatura

def on_message(client, userdata, msg):
    global temperatures
    temperature = float(msg.payload.decode())
    temperatures.append(temperature)

    if len(temperatures) > window_size:
        temperatures = temperatures[-window_size:]  # Manter apenas as últimas leituras

    if len(temperatures) >= window_size:
        average = statistics.mean(temperatures)
        print("Média das últimas {} leituras: {:.2f}".format(window_size, average))

        # Verificar condições para publicar mensagens
        if len(temperatures) >= 2:
            last_average = statistics.mean(temperatures[-2:])
            if abs(last_average - average) >= 5:
                client.publish("aumento_temperatura_repentina", "Aumento de temperatura repentina!")

        if average > 200:
            client.publish("temperatura_alta", "Temperatura alta!")

client = mqtt.Client()
client.connect("localhost", 1883)  # Conectar ao servidor MQTT

client.subscribe(topic)
client.on_message = on_message

client.loop_start()  # Iniciar loop para processar as mensagens

try:
    while True:
        time.sleep(1)  # Manter o programa rodando indefinidamente
except KeyboardInterrupt:
    client.loop_stop()  # Parar loop quando o programa for interrompido
    client.disconnect()  # Desconectar do servidor MQTT
