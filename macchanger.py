#!/usr/bin/env python3

import argparse
import re
import subprocess
from termcolor import colored



def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar el mac de la interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="nueva direccion MAC para la interfaz de red")
    
    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^[e|w][n|t|l][s|h|a][n]\d{1,2}$', interface)
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)
    
    return is_valid_interface and is_valid_mac_address



def change_mac_address(interface,mac_address):
    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])       
        print(colored(f"[+] Tu nueva mac es {mac_address}",'green'))  
    else:
        print(colored(f"[!]... Algo salio mal..",'yellow'))    
def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)




if __name__ == '__main__':
    main()