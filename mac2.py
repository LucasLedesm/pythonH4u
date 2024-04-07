import subprocess
import re

def get_current_mac(interface):
    result = subprocess.check_output(["ifconfig", interface])
    mac_address = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", result.decode())
    if mac_address:
        return mac_address.group(0)
    else:
        return None

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Aquí se define la interfaz de red que deseas modificar
interface = "wlan0"

# Obtén la dirección MAC actual
current_mac = get_current_mac(interface)
print("Tu dirección MAC actual es: " + str(current_mac))

# Cambia la dirección MAC a la deseada
new_mac = "e8:a4:c1:a0:b1:c2"
change_mac(interface, new_mac)
print("Tu dirección MAC se ha cambiado a: " + str(new_mac))
