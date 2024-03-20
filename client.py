#!/usr/bin/env python3
import socket   

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_address = ('localhost', 1234)
client_socket.connect(sever_address)

try:
    message = b"este es un mensaje de prueba que se manda al servidor"
    client_socket.sendall(message)
    data = client_socket.recv(1024)
    
    print(f"el servidor nos ah respondido con este mensaje: {data.decode()}")
finally:
    client_socket.close()