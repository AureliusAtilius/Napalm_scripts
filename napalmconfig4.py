import json
from napalm import get_network_driver

devicelist = ['192.168.255.7',
           '192.168.255.72'
           ]

# Iterate over devices in the device list
for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'josh', 'cisco')
    iosv.open()

    # Load ACL configuration from local file
    iosv.load_merge_candidate(filename='ACL1.cfg')
    diffs = iosv.compare_config()
    # Compare and add changes if no already present.
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required.')
        iosv.discard_config()

    # Load OSPF configuration from local file
    iosv.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosv.compare_config()
    # Compare and add changes if no already present.
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
    	print('No OSPF changes required.')
    	iosv.discard_config()

    iosv.close()




