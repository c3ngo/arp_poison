# ARP Poisoning Script

This script performs ARP poisoning, also known as ARP spoofing, to manipulate the ARP tables of devices on a local network. It allows an attacker to intercept network traffic and potentially carry out various malicious activities.

**WARNING: ARP poisoning is a form of cyberattack and is illegal without proper authorization. This script is intended for educational and testing purposes only.**

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [Important Notes](#important-notes)

## Prerequisites

- Make sure you have Python installed on your system.
- Install the required libraries using the following command:

  ```sh
  pip install scapy
    ```

## Usage
Open a terminal and navigate to the directory containing the script.

Run the script with the following command:

  ```sh
python3 arp_poison.py -t [target_ip] -g [gateway_ip]
  ```
Replace [target_ip] with the IP address of the victim/target device and [gateway_ip] with the IP address of the gateway/router.

## Example
To perform ARP poisoning on a network where the victim's IP is 192.168.1.100 and the gateway IP is 192.168.1.1, you would run:

```sh
python3 arp_poison.py -t 192.168.1.100 -g 192.168.1.1
```

## Important Notes
- ARP poisoning is illegal without proper authorization. Be sure to use this script only in controlled environments and with permission from the network owner.

- This script can disrupt network communication and potentially cause harm to devices on the network.

- The reset() function provided in the script attempts to reset the ARP tables after the attack, but it might not work in all cases.
