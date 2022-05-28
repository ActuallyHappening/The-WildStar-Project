from umqtt.robust import MQTTClient
import sys

from networking import *
import secrets
print("AIO.py executing ...")

getGoodWIFI()

AIO_username = secrets.get_AIO_username()
AIO_key = secrets.get_AIO_key()
AIO_url = b'io.adafruit.com'


def makeFeedName(feedName):
    return bytes(f'{str(AIO_username)}/feeds/embedded.embedded-{feedName}', 'utf-8')


AIO_feeds = {
    "POST": makeFeedName('from-test'),
    "GET": makeFeedName('to-test')
}

client_id = bytes("esp32_client_" + str(secrets.get_esp_id()), 'utf-8')

client = MQTTClient(client_id=client_id, server=AIO_url,
                    user=AIO_username,  password=AIO_key, ssl=False)


def _defaultCallback(topic, msg):
    print(f"Received: {topic} ;; {msg}")


__begun__ = False


def checkBegin():
    if not __begun__:
        print("Implicitly Beginning ...")
        begin(_defaultCallback)


def begin(callback):
    try:
        client.connect()
    except Exception as e:
        print(f"MQTT Failed to connect ... {type(e).__name__} ;; {e}")
        sys.exit()
    client.set_callback(callback)
    __begun__ = True
    # client.subscribe(AIO_feeds["GET"])


def publish(data, *, feed="POST"):
    checkBegin()
    print(f"Publishing to {feed}: {data}")
    data = bytes(str(data), 'utf-8')
    client.publish(AIO_feeds[feed], data, qos=0)
    # client.check_msg()


def subscribe(feed="GET"):
    checkBegin()
    print(f"Subscribing to {feed}")
    client.subscribe(AIO_feeds[feed])
    # client.check_msg()


def check():
    client.check_msg()


def disconnect():
    if __begun__:
        print(f"Disconnecting MQTT client ...")
        client.disconnect()
        __begun__ = False
    else:
        print("Disconnected MQTT client (already)")
