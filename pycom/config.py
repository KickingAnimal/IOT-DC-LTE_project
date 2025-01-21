import network
import ubinascii

# Initialize WiFi interface
wlan = network.WLAN()
wlan.init(mode=network.WLAN.STA)

# apn settings
apnName = "your_apn" # Replace 'your_apn' with your APN needed for your SIM card

# Get the MAC address
wlan_mac = wlan.mac()
valMac = ubinascii.hexlify(wlan_mac[0]).decode().upper()  # Convert to continuous string of hex characters
val_ID = 5  # for now static, should be based on mac or random.

# Server URLs
connectURL = '/app/connect'
statusURL = '/app/valUpdate'
serverURL = 'www.example.com'

port = 4000 #the port number of the server, change if needed, localhost default is 4000