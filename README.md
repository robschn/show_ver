# show_version
Script to grab the version number of multiple switches by leveraging multiprocessing.

### Install
- Install required packages using the requirements.txt
```
pip install -r requirements.txt
```

### Usage
1. Open the my_devices.py and input the IPs of the switches you want to connect to.
2. Run the script
```
python show_ver.py
```
3. The script will ask for a username and password. These will be stored to be used on all the switches.
```
Enter standard username: cisco
Enter standard password: 
```
4. The script will log into as many switches as it can and print the `show version` output.
```
TBD
```
5. Done!

### Misc
This script can easily be modified to pull any other command. You use just replace the `sh_ver` and `parse_ver` values. Please reference Netmiko and ntc-templates for more information.
