# boot.py -- run on boot-up
import pycom
import network
import time

# Create an LTE object
lte = network.LTE()

# Initialize the LTE object with the SIM PIN
sim_pin = '0000'  # Replace '1234' with your SIM PIN
lte.init(pin=sim_pin)

# Attach to the LTE network
lte.attach(band=20, apn='your_apn')  # Replace 'your_apn' with your APN

# Wait for the LTE network to attach
while not lte.isattached():
    time.sleep(1)
    print("Attaching to LTE network...")

print("Attached to LTE network")

# Connect to the LTE network
lte.connect()

# Wait for the LTE network to connect
while not lte.isconnected():
    time.sleep(1)
    print("Connecting to LTE network...")

print("Connected to LTE network")
print(lte.ifconfig())  # Print the IP configuration