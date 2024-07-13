from articles import charger_articles
from articles import enregistrer_articles

def ajouter_emplacement(numArt, emplacement, quantite):
    global articles
    articles = charger_articles()
    for article in articles:
        if article["Numero article"] == numArt:
            if "Emplacements" not in article:
                article["Emplacements"] = {}
            article["Emplacements"][emplacement] = quantite
            enregistrer_articles()
            break

# Afficher les stocks par emplacement
def afficher_stocks_par_emplacement():
    articles = charger_articles()
    for article in articles:
        if "Emplacements" in article:
            print(f"Article : {article['Nom article']}")
            for emplacement, quantite in article["Emplacements"].items():
                print(f"Emplacement : {emplacement}, Quantité : {quantite}")
