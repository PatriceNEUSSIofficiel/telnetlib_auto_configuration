# Automatisation des réseaux avec Python et Telnetlib

Ce script Python automatise la configuration de plusieurs routeurs en utilisant Telnetlib.

## Fonctionnalités

- Configuration automatique de plusieurs routeurs en une seule exécution.
- Sécurisation des mots de passe grâce à l'entrée sécurisée du mot de passe.

## Prérequis

- Python 3.x installé sur votre système.
- Accès aux routeurs via Telnet.
- Autorisations appropriées pour modifier la configuration des routeurs.

## Utilisation

1. Assurez-vous que Python est installé sur votre système.
2. Assurez-vous que les routeurs sont accessibles via Telnet.
3. Modifiez les informations de connexion et les configurations des routeurs dans le script `routers_auto_conf.py`.
4. Lancez le script en exécutant la commande suivante :

    ```bash
    python routers_auto_conf.py
    ```

5. Suivez les instructions et entrez votre mot de passe lorsque vous y êtes invité.

## Configuration des routeurs

Chaque routeur est configuré en utilisant un ensemble de commandes spécifiées dans le script. Vous pouvez personnaliser les configurations en modifiant la liste `config` pour chaque routeur dans le script.

## Avertissement

Assurez-vous d'avoir les autorisations appropriées pour modifier la configuration des routeurs. Veillez à ne pas exposer vos informations d'identification et celles de vos routeurs dans le script.




