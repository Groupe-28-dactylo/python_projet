import json
from datetime import datetime

def ajouter_historique(numArt, nomArt, ancienne_quantite, nouvelle_quantite):
    historique = charger_historique()
    modification = {
        "Numero article": numArt,
        "Nom article": nomArt,
        "Ancienne quantite": ancienne_quantite,
        "Nouvelle quantite": nouvelle_quantite,
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

def afficher_historique():
    historique = charger_historique()
    for modification in historique:
        print(modification)