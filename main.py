from articles import *
from ventes import *
from historique import *
from multi_emplacements import *
from avis import *
from remises import *
from alerte import *
from recherche import *
from analyse_produits import *

def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Supprimer produit")
    print("5. Enregistrer vente")
    print("6. Afficher historique des modifications de stock")
    print("7. Recherche par plage de prix")
    print("8. Alerte de produit en rupture de stock")
    print("9. Produits les plus vendus")
    print("10. Produits les moins vendus")
    print("11. Gestion des stocks multi-emplacements")
    print("12. Suivi des avis clients")
    print("13. Gestion des remises et des promotions")
    print("14. Quitter")
    return input("Choisissez une option: ")

def main():
    global articles
    articles = charger_articles()

    while True:
        choix = menu_principal()
        if choix == '1':
            ajouter_produits()
        elif choix == '2':
            afficher_articles()
        elif choix == '3':
            type_recherche = int(input("Comment voulez-vous effectuer la recherche\n 1.Par nom \n 2.Par ID \n : "))
            if type_recherche == 1:
                nom_recherche = input("Entrez le nom de l'article à rechercher: ")
                article_trouve = rechercher_article_par_nom(nom_recherche)
                if article_trouve:
                    print(f"Article trouvé : {article_trouve}")
                else:
                    print(f"Article avec le nom '{nom_recherche}' non trouvé.")
            elif type_recherche == 2:
                num_recherche = int(input("Entrez le numero (ID) de l'article : "))
                num_trouve = rechercher_article_par_id(num_recherche)
                if num_trouve:
                    print(f"ID trouvé {num_trouve}")
                else:
                    print(f"Article avec l'ID  '{num_recherche}' non trouvé .")
        elif choix == '4':
            article_a_supprimer = input("Entrez le nom de l'article à supprimer: ")
            article_supprime = supprimer_un_article(article_a_supprimer)
            if article_supprime:
                print(f"L'article '{article_a_supprimer}' a été supprimé avec succès.")
            else:
                print(f"Article avec le nom '{article_a_supprimer}' non trouvé.")
        elif choix == '5':
            numArt = int(input("Entrez le numéro de l'article vendu : "))
            quantite_vendue = int(input("Entrez la quantité vendue : "))
            enregistrer_vente(numArt, quantite_vendue)
        elif choix == '6':
            afficher_historique()
        elif choix == '7':
            prix_min = float(input("Entrez le prix minimum : "))
            prix_max = float(input("Entrez le prix maximum : "))
            resultats = rechercher_par_plage_de_prix(prix_min, prix_max)
            if resultats:
                for resultat in resultats:
                    print(resultat)
            else:
                print(f"Aucun article trouvé dans la plage de prix {prix_min} - {prix_max}")
        elif choix == '8':
            ruptures = alerte_rupture_stock()
            if ruptures:
                for article in ruptures:
                    print(f"Article en rupture de stock : {article}")
            else:
                print("Aucun article en rupture de stock.")
        elif choix == '9':
            produits_les_plus_vendus()
        elif choix == '10':
            produits_les_moins_vendus()
        elif choix == '11':
            afficher_stocks_par_emplacement()
        elif choix == '12':
            numArt = int(input("Entrez le numéro de l'article pour lequel vous voulez ajouter un avis : "))
            avis = input("Entrez votre avis : ")
            note = int(input("Entrez votre note (1-5) : "))
            ajouter_avis(numArt, avis, note)
            afficher_avis(numArt)
        elif choix == '13':
            numArt = int(input("Entrez le numéro de l'article pour lequel vous voulez ajouter une remise : "))
            remise = float(input("Entrez la remise (%) : "))
            ajouter_remise(numArt, remise)
            afficher_articles_avec_remise()
        elif choix == '14':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()