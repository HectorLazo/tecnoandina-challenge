import paho.mqtt.client as mqtt 

from datetime import datetime
import time
import json
import random


broker_address="mosquitto"
client = mqtt.Client("User1")
client.connect(broker_address)


def publicar():

	time.sleep(2)

	now = datetime.today()

	value = random.uniform(0, 1000)
	version = random.randint(1, 2)
	current_time = now.strftime('%Y/%m/%d %H:%M:%S')

	msg = {
	    "time": current_time,
	    "value": value,
	    "version": version
	}

	client.publish("challenge/dispositivo/rx", json.dumps(msg))



while True: publicar()