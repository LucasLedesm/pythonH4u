#!/usr/bin/env python3
import os
import sys
import requests

directorio_actual = os.getcwd()
print(f"Directorio altual de trabajo es: {directorio_actual}")


files =os.listdir(directorio_actual)
for file in files:
    print(file)


print(f"Este es el nombre del script: {sys.argv[0]}")    


#response = requests.get("https://google.com") 
#print(f"el codigo de estado es: {response.status_code}")
#print(f"[+] Mostrando codigo fuente de la pagina:\n")

#with open("index.html", "w") as f:
#    f.write(response.text)


#payload = {'key1', 'value1', 'key2', 'value2', 'key3', 'value3'}
#headers = {'User-Agent': 'My-app/1.0.0'}
#response = requests.post("https://httpbin.org/post", headers=headers)  #data= para POST  #params=  para GET
#print(response.text)

#response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
#print(response.status_code)

#url = 'htpps://httpbin.org/cookies'
#set_cookies_url = 'https://httpbin.org/cookies/set/my_cookies/123123'

#s = requests.Session()

#response = s.get(set_cookies_url)
#response = s.get(url)
### esto es para crear una sesion y  arrastrar la cookies para todas las peticiones
#print(response.text)

url = 'http://github.com'

r = requests.get(url , allow_redirects=False) ### para evitar el redirecionamiento
print(r.status_code)