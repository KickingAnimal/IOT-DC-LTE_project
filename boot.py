# boot.py -- run on boot-up
import pycom
import network
import time
import wificonfig

# Create an LTE object
lte = network.LTE(debug=True)

# Create WiFi object
wifi = network.WLAN()

# Initialize the LTE object
lte.init()

# Set the SIM PIN
sim_pin = '0000'  # Replace '0000' with your SIM PIN
lte.send_at_cmd('AT+CPIN={}'.format(sim_pin))

# Function to print signal strength
def print_signal_strength():
    signal_strength = lte.send_at_cmd('AT+CSQ')
    print("Signal strength:", signal_strength)

# Print signal strength
print_signal_strength()

# Attach to the LTE network
lte.attach(band=20, apn='advancedinternet')  # Replace 'your_apn' with your APN

# Wait for the LTE network to attach
n = 0
while not lte.isattached() and n < 3:
    time.sleep(1)
    print("Attaching to LTE network...")
    print_signal_strength()
    n += 1
    print(n)

print("Attached to LTE network")

# Connect to the LTE network
if lte.isattached():
    lte.connect()

# Wait for the LTE network to connect
#while not lte.isconnected():
#    time.sleep(1)
#    print("Connecting to LTE network...")

if lte.isconnected():
    print("Connected to LTE network")
    print(lte.ifconfig())  # Print the IP configuration

# Connect to WiFi
wifi_ssid = wificonfig.SSID  # Replace with your WiFi SSID
wifi_password = wificonfig.PASSWORD  # Replace with your WiFi password

wifi.connect(wifi_ssid, auth=(network.WLAN.WPA2, wifi_password))

# Wait for the WiFi connection
while not wifi.isconnected():
    time.sleep(1)
    print("Connecting to WiFi...")

print("Connected to WiFi")
print(wifi.ifconfig())  # Print the IP configuration