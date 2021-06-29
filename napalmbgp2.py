import json
from napalm import get_network_driver

# List of router IP addresses
bgp_list = ['192.168.255.70', '192.168.255.1']

# Iterate over router IP addresses
for ip_address in bgp_list:
        print("Connecting to "+str(ip_address))
        # Connect to router
        driver = get_network_driver('ios')
        iosvrouter = driver(ip_address, 'josh', 'cisco')
        iosvrouter.open()
        # Retrieve and print BGP neighbor information
        bgp_neighbors = iosvrouter.get_bgp_neighbors()
        print (json.dumps(bgp_neighbors, indent=4))

        iosvrouter.close()