
import network
import socket
import sys
from time import sleep
from machine import Pin
from dht import DHT11


print("libray importted")
sensor = DHT11(Pin(21, Pin.IN, Pin.PULL_UP))
print("sensor set")

IP = "192.168.2.115"
PORT = 2431


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('<wifi SSID>>', '<wifi password>')
        while not sta_if.isconnected():
            pass

do_connect()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((IP, PORT))
client.setblocking(False)

while True:
    try:
        sensor.measure()   # Poll sensor
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, int) and isinstance(h, int):  # Confirm sensor results are numeric
            msg = (b'{0:3d},{1:3d}'.format(t, h)).encode('utf-8')
            client.send(msg)
            print(msg)
        else:
            print('Invalid sensor readings.')
    except KeyboardInterrupt:
        sys.exit()
    sleep(5)
