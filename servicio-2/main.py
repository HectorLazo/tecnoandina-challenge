import paho.mqtt.client as mqtt

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import json
from datetime import datetime

broker="mosquitto"
port=1883
timelive=60


token="TokenPersonal"
org = "tecnoandina"
bucket="system"

influx_client = InfluxDBClient(url='http://influx:8086', token="qJv_NJkPQIIuItUMxqEFqi1VCR_ntBR4YJfu8SYPdObaUB4oHzqVHx4Ghog4kO-R2nC2EgTy7ucJTPNPn_ISgg==", org=org)

write_api = influx_client.write_api(write_options=SYNCHRONOUS)
query_api = influx_client.query_api()


def on_connect(client, userdata, flags, rc):
  client.subscribe("challenge/dispositivo/rx")

def on_message(client, userdata, msg):

    tiempo = json.loads(msg.payload.decode())['time']
    p = Point("dispositivos").tag("version", json.loads(msg.payload.decode())['version']).field("value", json.loads(msg.payload.decode())['value']).time(datetime.strptime(tiempo, "%Y-%m-%d %H:%M:%S"))
    write_api.write(bucket=bucket, record=p)

    
client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()