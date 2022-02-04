import paho.mqtt.client as mqtt

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import json
from datetime import datetime

broker="mosquitto"

#port
port=1883
#time to live
timelive=60
token="Dc9KtGhxqTRL-1H7AcnxECSmoOK-BmV_LZ2CA1v93kWb3Cm4s4U2rcVSzKvnIVViQkZ3nizaw1WYTLYYatA_Vw=="

influx_client = InfluxDBClient(url='192.168.18.66:8086', token=token, org="tecnoandina")
bucket="system"
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
query_api = influx_client.query_api()


def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("challenge/dispositivo/rx")

def on_message(client, userdata, msg):

    tiempo = json.loads(msg.payload.decode())['time']
   
    p = Point("dispositivos").tag("version", json.loads(msg.payload.decode())['version']).field("tiempo",tiempo ).field("value", json.loads(msg.payload.decode())['value'])

    write_api.write(bucket=bucket, record=p)

    
client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()