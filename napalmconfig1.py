import json
from napalm import get_network_driver

# Specify vendor driver
driver = get_network_driver('ios')

# Device IP and credentials, open connection
s1= driver('192.168.255.70','josh','cisco')
s1.open()

print('Accessing 192.168.255.70')

# Load configuration from local file and compare it to running config
s1.load_merge_candidate(filename='ACL1.cfg')

# If changes are not already present in the config, apply changes and commit.
diffs= s1.compare_config()
if len(diffs)> 0:
        print(diffs)
        s1.commit_config()
else:
        print ('No changes required.')
        s1.discard_config()
s1.close()
