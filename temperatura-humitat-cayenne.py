import random
import time
import cayenne.client

# Informacio Autenticacio Cayenne. Aquesta informacio a la Cayenne Dashboard.

MQTT_USERNAME  = "2dd7a530-d092-11e8-a056-c5cffe7f75f9" 
MQTT_PASSWORD  = "6d63b6a30a53c35a4abd3bc1b1876c470738a485" 
MQTT_CLIENT_ID = "233f16d0-7a6a-11e9-be3b-372b0d2759ae"
client = cayenne.client.CayenneMQTTClient() 
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID) 


# Bucle principal que genera les dades de temperatura  i humitat de forma aleatoria i els escriu en el canal 1 i canal 2

while True:
    client.loop()
    temperatura=random.randrange(0,100)
    humitat=random.randrange(0,100)
    client.virtualWrite(1, temperatura, "temp", "c")
    client.virtualWrite(2, humitat, "rel_hum", "r")
    time.sleep(3)