#!/usr/bin/env python3

import urllib3


http = urllib3.PoolManager() #controlador de conexiones

data= "esto es una prueba"
encoded_data = data.encode()
response = http.request('POST', 'https://httpbin.org/post', body=encoded_data)
print(response.data.decode())