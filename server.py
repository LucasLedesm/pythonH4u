#!/usr/bin/env python3

import socket
###                       esto es para ipv4 y eso     TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address= ('localhost', 1234)
server_socket.bind(server_address)
## limitar el limite de conexion a 1
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)
    
    print(f"[+] Mensaje recibido del Cliente: {data.decode()}")
    print(f"[+] Informacion del Cliente conectado: {client_address}")
    
    client_socket.sendall(f"un saludo crack\n".encode())
    client_socket.close()