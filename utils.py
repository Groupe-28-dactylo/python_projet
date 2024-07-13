import json

def charger_articles():
    try:
        with open('articles.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier articles.json n'existe pas.")
        return []

def enregistrer_articles(articles):
    with open('articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    print("Articles enregistrés dans articles.json")
