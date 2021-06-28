from napalm import get_network_driver
import json

# Import the network vendor driver
driver=get_network_driver('ios')

# Provide the device IP address and credentials
s1=driver('192.168.255.70','josh','cisco')

# Open ssh connection to device
s1.open()

#Get device facts and print them
ios_output = s1.get_facts()
print (json.dumps(ios_output, indent = 4))

# Get device interfaces counters
ios_output = s1.get_interfaces_counters()
print (json.dumps(ios_output, indent = 4))