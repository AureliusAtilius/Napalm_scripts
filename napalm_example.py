import sys
import json
from napalm import get_network_driver

def err_report(*err_list):
    error_msg = ' '.join(str(x) for x in err_list)
    sys.exit(error_msg.rstrip("\n\r"))

if len(sys.argv) != 3:
    err_report("Usage: get_config hostname")

hostname = sys.argv[2]

try:
    with open('hosts.json', 'r') as f:
        device_db = json.load(f)
except (ValueError, IOError, OSError) as err:
    err_report('Could not read the host file: ', err)

try:
    device_info= device_db[hostname.lower()]
except KeyError:
    err_report("Unkown Device '{}'".format(hostname))

driver = get_network_driver(device_info['type'])
with driver(device_info['IP'], device_info['user'], device_info['password']) as device:
    config = device.get_config()
    print(config['running'])


    device.load_merge_candidate(filename='config.txt')
    diffs= device.compare_config()
    if diffs != "":
        print(diffs)
        yesno = input('\nDo you wish to apply the changes? [y/N] ').lower()
        if yesno == 'y' or yesno == 'yes':
            print("Applying changes... ")
            device.commit_config()
        else:
            print("Discarding changes... ")
            device.discard_config()
    else:
        print("Configuration already present on the device")
        device.discard_config()
