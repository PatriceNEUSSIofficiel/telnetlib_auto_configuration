import platform
import socket
import psutil

# Informations sur le système d'exploitation
os_name = platform.system()
os_version = platform.release()

print('--- Informations sur le système d\'exploitation ---')
print(f'Système d\'exploitation : {os_name}')
print(f'Version : {os_version}\n')

# Informations sur le réseau
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print('--- Informations sur le réseau ---')
print(f'Nom d\'hôte : {hostname}')
print(f'Adresse IP : {ip_address}\n')

# Informations sur la mémoire

memory = psutil.virtual_memory()

print('--- Informations sur la mémoire ---')
print(f'Mémoire totale : {memory.total} bytes')
print(f'Mémoire disponible : {memory.available} bytes')
print(f'Taux d\'utilisation de la mémoire : {memory.percent}%\n')

# Informations sur le processeur
processor = platform.processor()
cpu_count = psutil.cpu_count(logical=False)

print('--- Informations sur le processeur ---')
print(f'Type de processeur : {processor}')
print(f'Nombre de cœurs physiques : {cpu_count}\n')