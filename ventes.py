import json
from datetime import datetime
from articles import charger_articles, enregistrer_articles
from historique import ajouter_historique

def enregistrer_vente(numArt, quantite_vendue):
    ventes = charger_ventes()
    vente = {
        "Numero article": numArt,
        "Quantite vendue": quantite_vendue,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    ventes.append(vente)
    enregistrer_ventes(ventes)
    mettre_a_jour_stock(numArt, quantite_vendue)

def enregistrer_ventes(ventes):
    with open('ventes.json', 'w') as f:
        json.dump(ventes, f, indent=4)
    print("Ventes enregistrées dans ventes.json")

def charger_ventes():
    try:
        with open('ventes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier ventes.json n'existe pas.")
        return []

def mettre_a_jour_stock(numArt, quantite_vendue):
    articles = charger_articles()
    for article in articles:
        if article["Numero article"] == numArt:
            article["Quantite article"] -= quantite_vendue
            ajouter_historique("Vente", article, quantite_vendue)
            break
    enregistrer_articles()
