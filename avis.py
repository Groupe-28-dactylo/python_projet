import json
from articles import charger_articles
from datetime import datetime

# Charger les avis depuis un fichier JSON
def charger_avis():
    try:
        with open('avis.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier avis.json n'existe pas.")
        return []

# Enregistrer les avis dans un fichier JSON
def enregistrer_avis(avis):
    with open('avis.json', 'w') as f:
        json.dump(avis, f, indent=4)
    print("Avis enregistrés dans avis.json")

# Ajouter un avis pour un article
def ajouter_avis(nomArt, avis_texte, note):
    articles = charger_articles()
    avis = charger_avis()

    for article in articles:
        if article["Nom article"] == nomArt:
            if "Avis" not in article:
                article["Avis"] = []

            article["Avis"].append({
                "avis": avis_texte,
                "note": note,
                "date": str(datetime.now())
            })
            enregistrer_avis(avis)
            break

# Afficher les avis pour un article
def afficher_avis(nomArt):
    articles = charger_articles()
    for article in articles:
        if article["Nom article"] == nomArt and "Avis" in article:
            for avis in article["Avis"]:
                print(f"Avis : {avis['avis']}, Note : {avis['note']}, Date : {avis['date']}")
            break
