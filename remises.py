from articles import charger_articles
from articles import enregistrer_articles

# Ajouter une remise à un article
def ajouter_remise(numArt, remise):
    articles = charger_articles()
    for article in articles:
        if article["Numero article"] == numArt:
            article["Remise"] = remise
            enregistrer_articles()
            break

# Afficher les articles avec remise
def afficher_articles_avec_remise():
    articles = charger_articles()
    for article in articles:
        if "Remise" in article:
            print(f"Article : {article['Nom article']}, Remise : {article['Remise']}")
