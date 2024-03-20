#!/usr/bin/env python3

import socket

def start_client():
    
    host= 'localhost'
    port= 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"hola, Servidor!")
        data= s.recv(1024)
        
    print(f"Mensaje recibido del servidor: {data.decode()}")
start_client()