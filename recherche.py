from articles import charger_articles

def rechercher_article_par_nom(nom_article):
    articles = charger_articles()
    for article in articles:
        if article.get("Nom article") == nom_article:
            return article
    return None

def rechercher_article_par_id(num_article):
    articles = charger_articles()
    for article in articles:
        if article.get("Numero article") == num_article:
            return article
    return None

def rechercher_par_plage_de_prix(prix_min, prix_max):
    articles = charger_articles()
    resultats = [article for article in articles if prix_min <= article["Prix article"] <= prix_max]
    return resultats
