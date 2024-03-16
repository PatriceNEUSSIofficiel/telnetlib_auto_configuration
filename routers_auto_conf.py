import getpass
import telnetlib

# Informations de connexion aux routeurs
routers = [
    {"host": "192.168.1.1", "user": "admin", "config": [
        "enable",
        "configure terminal",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.1 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]},
    {"host": "192.168.1.2", "user": "admin", "config": [
        "enable",
        "configure terminal",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.2 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]},
    {"host": "192.168.1.3", "user": "admin", "config": [
        "enable",
        "configure terminal",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.3 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]},
    {"host": "192.168.1.4", "user": "admin", "config": [
        "enable",
        "configure terminal",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.4 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]},
    {"host": "192.168.1.5", "user": "admin", "config": [
        "enable",
        "configure terminal",
        "interface GigabitEthernet0/0",
        "ip address 192.168.1.5 255.255.255.0",
        "no shutdown",
        "exit",
        "exit"
    ]}
]

def configure_router(router):
    try:
        # Connexion au routeur
        tn = telnetlib.Telnet(router["host"])
        tn.read_until(b"Username: ")

        # Envoyer le nom d'utilisateur
        tn.write(router["user"].encode('ascii') + b"\n")
        tn.read_until(b"Password: ")

        # Envoyer le mot de passe
        tn.write(password.encode('ascii') + b"\n")
        tn.read_until(b">")

        # Envoyer les commandes de configuration
        for command in router["config"]:
            tn.write(command.encode('ascii') + b"\n")
            tn.read_until(b">")

        print(f"Configuration du routeur {router['host']} terminée.")
        tn.write(b"exit\n")

    except Exception as e:
        print(f"Erreur lors de la configuration du routeur {router['host']} :", e)

# Demander le mot de passe une seule fois
password = getpass.getpass("Entrez votre mot de passe : ")

# Configurer chaque routeur
for router in routers:
    configure_router(router)
