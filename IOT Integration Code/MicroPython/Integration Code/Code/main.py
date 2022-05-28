import sys
import gc
import os
from umqtt.robust import MQTTClient
import time
#import network
from networking import *
import secrets
import AIO
import json
from commands import execute_command


print("YAY! main.py is executing ...")

getGoodWIFI()
printStatus()


def receivedMessage(topic, msg):
    print(f"Received from {topic}: \n{msg}")
    try:
        print('Beginning JSON decode ...')
        message = msg.decode('utf-8')
        print("JSON message .decoded finished ...")
        data = json.load(message)
        print("JSON decode successful ...")
    except ValueError as exc:
        print(f"Received message is not json :( {exc}")
        return
    print(f"Received Command: {data}")
    payload = data["payload"]
    _project, _action, _input = payload["Project"], payload["Action"], payload["Input"]
    execute_command(_project, _action, _input)  # , logger=AIO.publish)


AIO.begin(receivedMessage)
AIO.subscribe("GET")
AIO.subscribe("POST")
AIO.publish("Hello World!")

try:
    while True:
        #print("Checking ...")
        AIO.check(debug=True)
        time.sleep(1)
except Exception as exc:
    print(f"Exiting main.py main loop: {exc}")
    AIO.disconnect()
    raise exc
