from napalm import get_network_driver

# Import the network vendor driver
driver=get_network_driver('ios')

# Provide the device IP address and credentials
s1=driver('192.168.255.70','josh','cisco')

# Open ssh connection to device
s1.Open()

#Get device facts and print them
ios_output = s1.get_facts()
print (ios_output)