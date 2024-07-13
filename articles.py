import json
from datetime import datetime

def validation_nom_article(nom_art):
    return nom_art.isalpha()

def validation_prix(prix_art):
    try:
        prix = float(prix_art)
        return prix > 0
    except ValueError:
        return False

def validation_quantite(qte_art):
    try:
        quantite = int(qte_art)
        return quantite >= 0
    except ValueError:
        return False

def ajouter_article():
    global articles, next_num_art
    articles = charger_articles()

    while True:
        nom_art = input("Saisir le nom de l'article : ")
        if validation_nom_article(nom_art):
            if any(article['Nom article'] == nom_art for article in articles):
                print("Un article avec ce nom existe déjà.")
            else:
                break
        else:
            print("Nom d'article invalide.")

    # Ajouter le reste de la logique d'ajout ici

def afficher_articles():
    global articles
    articles = charger_articles()
    for article in articles:
        print(article)

# Les autres fonctions de gestion d'articles (suppression, recherche, etc.) vont ici

# Fonctions pour charger et enregistrer les articles
def enregistrer_articles():
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    print("Articles enregistrés dans articles.json")

def charger_articles():
    try:
        with open('articles.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier articles.json n'existe pas.")
        return []

# Autres fonctions spécifiques à la gestion des articles
