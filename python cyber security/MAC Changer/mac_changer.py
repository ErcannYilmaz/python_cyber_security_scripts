import random
import subprocess
import re
import time

hex_chars = ['0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def get_current_mac(interface):
    ip_link_result = subprocess.check_output(["ip", "link", "show", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"ether (\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ip_link_result)
    if mac_address_search_result:
        return mac_address_search_result.group(1)
    else:
        return None


def main():	
	new_mac = ""
	old_mac = get_current_mac("eth0")

	for i in range(12):
		new_mac = new_mac + random.choice(hex_chars)
		if i % 2 != 0 and i != 11:
			new_mac = new_mac + ':' 

	print(f"Old MAC Address: {old_mac}")
	print(f"Randomly created MAC Address: {new_mac}")

	print("#### Disabling Network Interface ####")
	subprocess.run("ip link set dev eth0 down", shell=True)
	time.sleep(1)

	print("#### Changing Network Interface ####")
	subprocess.run(f"ip link set dev eth0 address {new_mac}", shell=True)
	time.sleep(1)

	print("#### Enabling Network Interface ####")
	subprocess.run("ip link set dev eth0 up", shell=True)
	time.sleep(1)

	changed_mac = get_current_mac("eth0")

	if changed_mac != old_mac:
		print(f"Your MAC Address changed from {old_mac} to {changed_mac}")
	else:
		print("!!! ERROR MAC Address can't changed, try again !!!")


if __name__ == '__main__':
	main()