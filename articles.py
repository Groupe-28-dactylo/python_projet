import json
from historique import ajouter_historique

articles = []
next_numArt = 1

def validationNomArticle(nomArt):
    return nomArt.isalpha()

def validationPrix(prixArt):
    try:
        return float(prixArt)
    except ValueError:
        return False

def validationQuantite(qteArt):
    try:
        return int(qteArt)
    except ValueError:
        return False

def ajouter_produits():
    global articles, next_numArt
    articles = charger_articles()

    while True:
        nomArt = input("Saisir le nom de l'article : ")
        if validationNomArticle(nomArt):
            if any(article['Nom article'] == nomArt for article in articles):
                print("Un article avec ce nom existe déjà, veuillez en saisir un autre.")
            else:
                break
        else:
            print("Nom d'article invalide, veuillez réessayer.")
    
    while True:
        prixArt = input("Saisir le prix de l'article : ")
        prixArt = validationPrix(prixArt)
        if prixArt:
            break
        print("Prix d'article invalide, veuillez réessayer.")
    
    while True:
        qteArt = input("Saisir la quantité de l'article : ")
        qteArt = validationQuantite(qteArt)
        if qteArt:
            break
        print("Quantité d'article invalide, veuillez réessayer.")

    numArt = next_numArt
    next_numArt += 1

    article = {
        "Numero article": numArt,
        "Nom article": nomArt,
        "Prix article": prixArt,
        "Quantite article": qteArt
    }

    articles.append(article)
    enregistrer_articles()

def afficher_produits():
    global articles
    articles = charger_articles()
    for article in articles:
        print(article)

def rechercher_article_par_nom(nom_article):
    articles = charger_articles()
    for article in articles:
        if article.get("Nom article") == nom_article:
            return article
    return None

def rechercher_article_par_ID(num_article):
    articles = charger_articles()
    for article in articles:
        if article.get("Numero article") == num_article:
            return article
    return None

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

def supprimer_un_article(nom_article):
    global articles
    articles = charger_articles()
    for article in articles:
        if article.get("Nom article") == nom_article:
            articles.remove(article)
            enregistrer_articles()
            return True
    return False

def rechercher_par_plage_de_prix(prix_min, prix_max):
    articles = charger_articles()
    resultats = []
    for article in articles:
        if prix_min <= article["Prix article"] <= prix_max:
            resultats.append(article)
    return resultats

def alerte_rupture_stock():
    articles = charger_articles()
    ruptures = [article for article in articles if article["Quantite article"] == 0]
    return ruptures
