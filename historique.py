import json
from datetime import datetime

def ajouter_historique(action, article, quantite):
    historique = charger_historique()
    modification = {
        "Action": action,
        "Article": article,
        "Quantite": quantite,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    historique.append(modification)
    enregistrer_historique(historique)

def enregistrer_historique(historique):
    with open('historique.json', 'w') as f:
        json.dump(historique, f, indent=4)
    print("Historique mis à jour dans historique.json")

def charger_historique():
    try:
        with open('historique.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier historique.json n'existe pas.")
        return []
