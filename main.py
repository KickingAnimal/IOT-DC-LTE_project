import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0x990000)  # Red
    time.sleep(1)
    pycom.rgbled(0x009900)  # Green
    time.sleep(1)
    pycom.rgbled(0x000099)  # Blue
    time.sleep(1)