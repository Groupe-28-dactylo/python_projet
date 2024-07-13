from .articles import charger_articles

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

# Autres fonctions spécifiques à la recherche d'articles
