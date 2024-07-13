from .articles import charger_articles

def alerte_rupture_stock():
    articles = charger_articles()
    ruptures = [article for article in articles if article["Quantite article"] == 0]
    return ruptures