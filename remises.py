from .articles import charger_articles

def gerer_remises_promotions():
    global articles
    articles = charger_articles()

    # Logique de gestion des remises et promotions ici

# Autres fonctions spécifiques à la gestion des remises et promotions
