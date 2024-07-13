import json
def afficher_stocks_par_emplacement():
    stocks = charger_stocks()
    for stock in stocks:
        print(stock)

def charger_stocks():
    try:
        with open('stocks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Le fichier stocks.json n'existe pas.")
        return []
