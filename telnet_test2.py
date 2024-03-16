import telnetlib
import time

# Informations de connexion
HOST = '192.168.0.1'  # Adresse IP du routeur
PORT = 23  # Port Telnet (par défaut : 23)
USERNAME = 'admin'  # Nom d'utilisateur
PASSWORD = 'password'  # Mot de passe

# Commandes à exécuter
COMMANDS = [
    'show interfaces',
    'show ip route',
    'show version'
]

# Établissement de la connexion Telnet
tn = telnetlib.Telnet(HOST, PORT)

# Attendre le prompt de connexion
tn.read_until(b'Username: ')
tn.write(USERNAME.encode('utf-8') + b'\n')

tn.read_until(b'Password: ')
tn.write(PASSWORD.encode('utf-8') + b'\n')

# Attendre que le prompt du routeur apparaisse
time.sleep(2)
tn.read_very_eager()

# Exécuter les commandes et récupérer la sortie
for command in COMMANDS:
    tn.write(command.encode('utf-8') + b'\n')
    time.sleep(2)

    output = tn.read_very_eager().decode('utf-8')

    # Traitement de la sortie
    print(f"=== {command} ===")
    print(output)
    print('=' * 80)

# Fermeture de la connexion Telnet
tn.close()