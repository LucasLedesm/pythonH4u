#!/usr/bin/env python3

import socket
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
import signal
import sys
#host = input(f"\n Introduce la ip: ")
#host = '192.168.1.1'
#port = int(input(f"\n introduce el puerto:"))
#port = 80


open_sockets = []

def def_handler(sig, frame):
    print(colored(f"\n Saliendo ...",'red'))
    for socket in open_sockets:
        socket.close()
    sys.exit(1)
    
signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP port scanner")
    parser.add_argument("-t", "--target", dest="target",required=True, help="Victim target to scan (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="por range to scan (Ex: -p 1-100)")
    options = parser.parse_args()
    options = parser.parse_args()
    

    return options.target, options.port



def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)   #para setear el maximo de tiempo de espera
    open_sockets.append(s)
    return s



def port_scanner(port, host):
   
   s = create_socket()
   
   try:
       s.connect((host, port))
       print(colored(f"\n [+] el puerto {port}, de la ip {host} esta ABIERTO",'green'))
       s.close()
   except (socket.timeout, ConnectionRefusedError):
       s.close()
       #print(colored(f"\n [!] El puerto {port} de la ip {host} esta CERRADO",'red'))



def scan_ports(ports, target):
    with ThreadPoolExecutor(max_workers=100) as executor:
    
        executor.map(lambda port: port_scanner(port, target),ports)
        



def parse_ports(ports_str):
     if '-' in ports_str:
       start, end = map(int, ports_str.split('-'))
       return range(start, end+1)
     elif ',' in ports_str:
       return map(int, ports_str.split(','))
     else:
        return (int(ports_str),)



def main():
    target, ports_str = get_arguments()
    ports= parse_ports(ports_str)
    scan_ports(ports, target)
if __name__ == '__main__':
    main()