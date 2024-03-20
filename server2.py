#!/usr/bin/env python3

import socket

def start_server():
    
    host= 'localhost'
    port= 1234
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"[+] Servidor en escucha en el puerto {port} y el host {host}")
        s.listen(1)
        conn, addr = s.accept()
        
        with conn :
            print(f" se ha conectado un nuevo cliente: {addr}")
            while True:
                data = conn.recv(1024)
                conn.sendall(data)    
start_server()