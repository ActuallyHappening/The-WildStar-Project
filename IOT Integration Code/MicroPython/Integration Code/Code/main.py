import sys
import gc
import os
from umqtt.robust import MQTTClient
import time
#import network
from networking import *
import secrets
import AIO
print("YAY! main.py is executing ...")

getGoodWIFI()


def receivedMessage(topic, msg):
    print(f"Received: {topic} ;; {msg}")


AIO.begin(receivedMessage)
AIO.subscribe("GET")
AIO.subscribe("POST")
AIO.publish("Hello World!")

try:
    while True:
        #print("Checking ...")
        AIO.check(debug=False)
        time.sleep(2)
except Exception as exc:
    AIO.disconnect()
finally:
    AIO.disconnect()


"""
# the following function is the callback which is
# called when subscribed data is received


def cb(topic, msg):
    print('Subscribe:  Received Data:  Topic = {}, Msg = {}\n'.format(topic, msg))
    free_heap = int(str(msg, 'utf-8'))


# create a random MQTT clientID
random_num = int.from_bytes(os.urandom(3), 'little')
mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')

# connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
#
# To use a secure connection (encrypted) with TLS:
#   set MQTTClient initializer parameter to "ssl=True"
#   Caveat: a secure connection uses about 9k bytes of the heap
#         (about 1/4 of the micropython heap on the ESP8266 platform)
ADAFRUIT_IO_URL = b'io.adafruit.com'
ADAFRUIT_USERNAME = secrets.get_AIO_username()
ADAFRUIT_IO_KEY = secrets.get_AIO_key()
ADAFRUIT_IO_POST_FEEDNAME = b'embedded.embedded-from-test'
ADAFRUIT_IO_GET_FEEDNAME = b'embedded.embedded-to-test'

client = MQTTClient(client_id=mqtt_client_id,
                    server=ADAFRUIT_IO_URL,
                    user=ADAFRUIT_USERNAME,
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)

try:
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

# publish free heap statistics to Adafruit IO using MQTT
# subscribe to the same feed
#
# format of feed name:
#   "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
mqtt_feedname = bytes(
    '{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_POST_FEEDNAME), 'utf-8')
client.set_callback(cb)
client.subscribe(mqtt_feedname)
PUBLISH_PERIOD_IN_SEC = 10
SUBSCRIBE_CHECK_PERIOD_IN_SEC = 0.5
accum_time = 0
while True:
    try:
        # Publish
        if accum_time >= PUBLISH_PERIOD_IN_SEC:
            free_heap_in_bytes = gc.mem_free()
            print('Publish:  freeHeap = {}'.format(free_heap_in_bytes))
            client.publish(mqtt_feedname,
                           bytes(str(free_heap_in_bytes), 'utf-8'),
                           qos=0)
            accum_time = 0

        # Subscribe.  Non-blocking check for a new message.
        client.check_msg()

        time.sleep(SUBSCRIBE_CHECK_PERIOD_IN_SEC)
        accum_time += SUBSCRIBE_CHECK_PERIOD_IN_SEC
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()
"""
