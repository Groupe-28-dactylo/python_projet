from articles import charger_articles
from articles import enregistrer_articles
# Ajouter un avis pour un article
def ajouter_avis(numArt, avis, note):
    articles = charger_articles()
    for article in articles:
        if article["Numero article"] == numArt:
            if "Avis" not in article:
                article["Avis"] = []
            article["Avis"].append({"avis": avis, "note": note})
            enregistrer_articles()
            break

# Afficher les avis pour un article
def afficher_avis(numArt):
    articles = charger_articles()
    for article in articles:
        if article["Numero article"] == numArt and "Avis" in article:
            for avis in article["Avis"]:
                print(f"Avis : {avis['avis']}, Note : {avis['note']}")
            break