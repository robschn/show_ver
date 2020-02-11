from getpass import getpass

username = input("Enter standard username: ")
password = getpass("Enter standard password: ")

device_ips = {
    "192.168.1.10",
    "192.168.1.8",
    "192.168.1.7",
    "192.168.1.3",
    "192.168.1.6"
}

device_list = []

for ip_address in device_ips:
    curr_device = {
        "device_type": "cisco_ios",
        "ip": ip_address,
        "username": username,
        "password": password,
    }
    device_list.append(curr_device)

