from .articles import charger_articles

def alerte_rupture_stock():
    articles = charger_articles()
    seuil = int(input("Saisir le seuil de quantité pour alerte : "))
    resultats = [article for article in articles if article["Quantite article"] <= seuil]
    if resultats:
        for article in resultats:
            print(f"Alerte: {article['Nom article']} est en rupture de stock.")
    else:
        print("Aucun article en rupture de stock.")

# Autres fonctions spécifiques à l'alerte de rupture de stock
