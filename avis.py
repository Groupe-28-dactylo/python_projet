import json
from datetime import datetime

avis_clients = []

def enregistrer_avis():
    with open('avis_clients.json', 'w') as f:
        json.dump(avis_clients, f, indent=4)
    print("Avis clients enregistrés dans avis_clients.json")

def charger_avis():
    try:
        with open('avis_clients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier avis_clients.json n'existe pas.")
        return []

def ajouter_avis_client():
    global avis_clients
    avis_clients = charger_avis()
    
    # Logique d'ajout d'avis client ici

# Autres fonctions spécifiques à la gestion des avis clients
