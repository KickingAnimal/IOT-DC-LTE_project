import network
import ubinascii

# Initialize WiFi interface
wlan = network.WLAN()
wlan.init(mode=network.WLAN.STA)

# Get the MAC address
wlan_mac = wlan.mac()
valMac = ubinascii.hexlify(wlan_mac[0]).decode().upper()  # Convert to continuous string of hex characters
val_ID = 5  # for now static, should be based on mac or random.

connectURL = '/app/connect'
statusURL = '/app/valUpdate'
serverURL = 'www.kickinganimal.nl'

port = 4430