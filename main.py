import pycom
import time
import socket
from machine import Pin
from time import sleep
import network
import config
import urequests as requests

pycom.heartbeat(False)

urlStatus = "http://{}:{}{}".format(config.serverURL, config.port, config.statusURL)
urlConnect = "http://{}:{}{}".format(config.serverURL, config.port, config.connectURL)

def cycle_rgb():
    for r in range(0, 256, 5):
        color = (r << 16)
        pycom.rgbled(color)
        time.sleep(0.01)
    for g in range(0, 256, 5):
        color = (255 << 16) | (g << 8)
        pycom.rgbled(color)
        time.sleep(0.01)
    for b in range(0, 256, 5):
        color = (255 << 16) | (255 << 8) | b
        pycom.rgbled(color)
        time.sleep(0.01)

def blink(color, count, flash_time):
    for i in range(count):
        pycom.rgbled(color)
        time.sleep(flash_time)
        pycom.rgbled(0x000000)
        time.sleep(flash_time)

def ping_server(host):
    try:
        addr = socket.getaddrinfo(host, 80)[0][-1]
    except OSError as e:
        print("Error getting address info:", e)
        return False
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect(addr)
        s.send(b"GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(host))
        response = s.recv(100)
        s.close()
        return True
    except:
        return False

def post_request(url, data):
    try:
        response = requests.post(url, json=data)
        return response.json()
    except OSError as e:
        print("Error making HTTP request:", e)
        return None

cycle_rgb()
pycom.rgbled(0x000000)

# Define digital input pins with pull-up resistors
pin18 = Pin('P10', mode=Pin.IN, pull=Pin.PULL_DOWN)  # Use a pin that supports digital input
pin19 = Pin('P11', mode=Pin.IN, pull=Pin.PULL_DOWN)  # Use a pin that supports digital input

n = 0
i = 20
serverStatus = 1

valStatus = pin18.value()

while wifi.isconnected() or lte.isconnected():
    sleep(5)
    n += 5
    i += 5
    if i > 30:
        blink(0x333300, 2, 0.05)
        print("BLINK!")
        i = 0

    buttonPressed = pin19.value()
    valButton = pin18.value()

    if buttonPressed == 1:  # Button pressed (active high)
        print("button was pressed:", buttonPressed, "\ntrying to connect")
        response = post_request(urlConnect, {'valMac': config.valMac, 'val_ID': config.val_ID})
        if response:
            error = response.get('error')
            print("\n-->", error)
            if error == "OK: no errors caught":
                blink(0x00FF00, 5, 0.25)
            else:
                blink(0xFF0000, 5, 0.25)
        n = 0
    elif buttonPressed == 0:  # Button not pressed
        newValStatus = valButton
        if valStatus != newValStatus:
            valStatus = newValStatus
            if newValStatus == 1:  # Active high
                serverStatus = 2
            if newValStatus == 0:  # Active low
                serverStatus = 1

            print("'val' dicht:", bool(valButton == 1), valStatus, "posting status", serverStatus)
            response = post_request(urlStatus, {'valMac': config.valMac, 'val_ID': config.val_ID, 'valStatus': serverStatus})
            if response:
                error = response.get('error')
                print("\n-->", error)
                if error == "Status updated to: '{}'".format(serverStatus):
                    blink(0x00FF00, 10, 0.025)
                else:
                    blink(0xFF0000, 10, 0.25)
            n = 0

    if n > 3600:
        print("'val' heartbeat:", bool(valButton == 1), valStatus, "posting status", serverStatus)
        response = post_request(urlStatus, {'valMac': config.valMac, 'val_ID': config.val_ID, 'valStatus': serverStatus})
        if response:
            error = response.get('error')
            print("\n-->", error)
            corect = "Status updated to: '{}'".format(serverStatus)
            print(error, corect)
            if error == corect:
                blink(0x0000FF, 10, 0.025)
            else:
                blink(0xFF0000, 10, 0.25)
        n = 0