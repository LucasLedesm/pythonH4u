#!/usr/bin/env python3

import scapy.all as scapy

def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        domain=packet[scapy.DNSQR].qname.decode()
        
        exclude_keywords = ["google", "cloud", "bing", "static"]
        
        if domain not in domains_seen and any(keyword in domain for keyword in exclude_keywords):
            
            domains_seen.add(domain)
            print(f"[+]Dominio: {domain}") 

def main():
   global domains_seen
   domains_seen = set()
   
   interface = "wlan0"
   print(f"[*] Interceptando paquetes..")
   scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0)


if __name__ == '__main__':
    main()