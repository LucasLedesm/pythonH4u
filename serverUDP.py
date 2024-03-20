#!/usr/bin/env python3

import socket

def start_udp_server():
    host= 'localhost'
    port= 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"[+] servidor inicidado en {port}:{host}")
        
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Mensaje envidado por el cliente: {data.decode()}")
            print(f"informacion del cliente {addr }")
start_udp_server()