import json
from datetime import datetime
from historique import ajouter_historique

def validation_nom_article(nom_art):
    """Permet de verifier la validité du nom de l'article"""
    return nom_art.isalpha()

def validation_prix(prix_art):
    """Permet de verifier la validité du prix de l'article"""
    try:
        prix = float(prix_art)
        return prix > 0
    except ValueError:
        return False

def validation_quantite(qte_art):
    """Permet de verifier la validité de la quantité de l'article"""
    try:
        quantite = int(qte_art)
        return quantite >= 0
    except ValueError:
        return False

def ajouter_produits():
    """Permet de rajouter les articles"""
    global articles, next_numArt

    # Charger les articles depuis le fichier JSON pour éviter la redondance
    articles = charger_articles()

    while True:
        nomArt = input("Saisir le nom de l'article : ")
        if validation_nom_article(nomArt):
            # Vérifier si le nom de l'article existe déjà
            if any(article['Nom article'] == nomArt for article in articles):
                print("Un article avec ce nom existe déjà, veuillez en saisir un autre.")
            else:
                break
        else:
            print("Nom d'article invalide, veuillez réessayer.")
    
    while True:
        prixArt = input("Saisir le prix de l'article : ")
        if validation_prix(prixArt):
            prixArt = float(prixArt)
            break
        print("Prix d'article invalide, veuillez réessayer.")
    
    while True:
        qteArt = input("Saisir la quantité de l'article : ")
        if validation_quantite(qteArt):
            qteArt = int(qteArt)
            break
        print("Quantité d'article invalide, veuillez réessayer.")

    # Générer un numéro d'article unique
    numArt = next_numArt
    next_numArt += 1

    # Créer un dictionnaire pour l'article
    article = {
        "Numero article": numArt,
        "Nom article" : nomArt,
        "Prix article" : prixArt,
        "Quantite article" : qteArt
    }

    # Ajouter l'article à la liste et enregistrer dans le fichier JSON
    articles.append(article)
    enregistrer_articles()

    # Ajouter une entrée dans l'historique des modifications de stock
    ajouter_historique(numArt, nomArt, 0, qteArt)

def afficher_articles():
    """Permet d'afficher les articles enregistrés"""
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
