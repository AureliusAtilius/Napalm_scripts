import json
from napalm import get_network_driver

# Specify vendor driver
driver = get_network_driver('ios')

# Device IP and credentials, open connection
s1= driver('192.168.255.70','josh','cisco')
s1.open()

print('Accessing 192.168.255.70')

# Load configuration from local file and commit, close connection
s1.load_merge_candidate(filename='ACL1.cfg')
s1.commit_config()
s1.close()
