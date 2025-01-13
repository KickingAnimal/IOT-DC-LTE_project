# boot.py -- run on boot-up
import pycom
import network
import time
import wificonfig
import socket
from time import sleep
import machine
import sys
from machine import Pin


# Create an LTE object
lte = network.LTE()
# Create WiFi object
wifi = network.WLAN()

# Initialize the LTE object
lte.init(debug=False)

# Function to print signal strength
def print_signal_strength():
    if not lte.isconnected():
        signal_strength = lte.send_at_cmd('AT+CSQ')
        print("Signal strength:", signal_strength)
    else:
        print("Cannot send AT commands, LTE modem is in data state")

# Print signal strength
print_signal_strength()

# Attach to the LTE network
lte.attach(band=None, apn='iot.1nce.net')  # Replace 'your_apn' with your APN

# Wait for the LTE network to attach
n = 0
while not lte.isattached() and n < 15:
    time.sleep(5)
    print("Attaching to LTE network...")
    print(n)
    print_signal_strength()
    n += 1
    


# Connect to the LTE network
if lte.isattached():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Attached to LTE network")
    lte.connect()

# Wait for the LTE network to connect
i = 0
while not lte.isconnected():
    time.sleep(1)
    print("Connecting to LTE network...")
    i += 1

if lte.isconnected():
    print("Connected to LTE network")


if not lte.isconnected():
    
    # Connect to WiFi
    wifi_ssid = wificonfig.SSID  # Replace with your WiFi SSID
    wifi_password = wificonfig.PASSWORD  # Replace with your WiFi password

    wifi.connect(wifi_ssid, auth=(network.WLAN.WPA2, wifi_password))

    # Wait for the WiFi connection
    while not wifi.isconnected():
        time.sleep(10)
        print("Connecting to WiFi...")

    print("Connected to WiFi")
    print(wifi.ifconfig())  # Print the IP configuration

print("boot.py -- end")
print("")
print("")