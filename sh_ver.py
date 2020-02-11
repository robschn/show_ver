
import multiprocessing
from netmiko import ConnectHandler
from ntc_templates.parse import parse_output
from secret_devices import device_list


def show_version(a_device):
    """
    Execute show version command using Netmiko
    then parse the output with ntc template
    """
    remote_conn = ConnectHandler(**a_device)
    sh_ver = remote_conn.send_command_expect("show version")

    parse_ver = parse_output(platform='cisco_ios',
                             command='show version', data=sh_ver)
    print(parse_ver[0]['hostname'], parse_ver[0]['version'])


def main():
    """
    Uses multiprocessing and Netmiko to connect to each of the devices. Execute
    'show version' on each device.
    """
    pool = multiprocessing.Pool()
    pool.map(show_version, device_list)


if __name__ == "__main__":
    main()
