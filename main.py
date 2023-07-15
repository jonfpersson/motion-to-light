import time
import network

from mqtt import MQTTClient
from machine import Pin
from secrets import secrets

RANDOMS_INTERVAL = 20000
previous_sensor_value_random_sent_ticks = 0
led = Pin("LED", Pin.OUT)

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "jonfp"
AIO_KEY = "your_key"
AIO_CLIENT_ID = "pi"
AIO_RANDOMS_FEED = "Your_lights_Feed_Address"
 
def do_connect():
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(secrets["ssid"], secrets["password"])
        print('Waiting for connection...')
        
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.')
            time.sleep(1)
    
    print('\nConnected on {}'.format(wlan.ifconfig()[0]))

def send_message(client, message):
    print("Publishing: {0} to {1} ... ".format(message, AIO_RANDOMS_FEED), end='')
    try:
        client.publish(topic=AIO_RANDOMS_FEED, msg=str(message))
        print("DONE")
    except Exception as e:
        print("apa\n")

        print("FAILED" + e)


try:
    do_connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

adafruit_client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
homeassistant_client = MQTTClient("pi", "ip-address", 1883, "mqtt_user", "password", ssl=False, keepalive=240)

sensor_pin = Pin(13, Pin.IN)

previous_sensor_value = 0
seconds_elapsed = 0
user_is_inactive = True
user_inactive_timeout = 15*60
try:
    while True:
        state = sensor_pin.value()
        if(seconds_elapsed > user_inactive_timeout and not user_is_inactive):
            homeassistant_client.connect()
            send_message(homeassistant_client, "OFF")
            homeassistant_client.disconnect()

            adafruit_client.connect()
            send_message(adafruit_client, "0")
            adafruit_client.disconnect()

            seconds_elapsed = 0 
            user_is_inactive = True

        if(state == 1 ):
            if(previous_sensor_value == 0 and user_is_inactive):
                homeassistant_client.connect()
                send_message(homeassistant_client, "ON")
                homeassistant_client.disconnect()

                adafruit_client.connect()
                send_message(adafruit_client, "1")
                adafruit_client.disconnect()

                time.sleep(3)
            user_is_inactive = False
            seconds_elapsed = 0
        time.sleep(1)
        seconds_elapsed += 1
        previous_sensor_value = state

finally:
    homeassistant_client.disconnect()
    homeassistant_client = None
    print("Disconnected from HA.")