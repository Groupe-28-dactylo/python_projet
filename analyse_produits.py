from ventes import charger_articles
from ventes import charger_ventes
# Produits les plus vendus
def produits_les_plus_vendus():
    ventes = charger_ventes()
    articles = charger_articles()
    ventes_par_article = {}
    for vente in ventes:
        numArt = vente["Numero article"]
        quantite_vendue = vente["Quantite vendue"]
        if numArt in ventes_par_article:
            ventes_par_article[numArt] += quantite_vendue
        else:
            ventes_par_article[numArt] = quantite_vendue
    ventes_triees = sorted(ventes_par_article.items(), key=lambda x: x[1], reverse=True)
    for numArt, quantite_vendue in ventes_triees:
        article = next((a for a in articles if a["Numero article"] == numArt), None)
        if article:
            print(f"Article : {article['Nom article']}, Quantité vendue : {quantite_vendue}")

# Produits les moins vendus
def produits_les_moins_vendus():
    ventes = charger_ventes()
    articles = charger_articles()
    ventes_par_article = {}
    for vente in ventes:
        numArt = vente["Numero article"]
        quantite_vendue = vente["Quantite vendue"]
        if numArt in ventes_par_article:
            ventes_par_article[numArt] += quantite_vendue
        else:
            ventes_par_article[numArt] = quantite_vendue
    ventes_triees = sorted(ventes_par_article.items(), key=lambda x: x[1])
    for numArt, quantite_vendue in ventes_triees:
        article = next((a for a in articles if a["Numero article"] == numArt), None)
        if article:
            print(f"Article : {article['Nom article']}, Quantité vendue : {quantite_vendue}")
