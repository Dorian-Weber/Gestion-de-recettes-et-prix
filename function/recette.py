from base_de_donnee import convertisseur_Json, lecteur_Json,lecteur_csv

def ajouter_recette() :
    recette = []
    data = lecteur_csv
    nbingredient = input(f"Combien y a t'il d'ingredient dans la recette ? ")
    if nbingredient.isdigit() and int(nbingredient) < 0:
        for i in range(int(nbingredient)) :
            ingredient = {'produit': None, 'quantite': None, 'prix': None}
            ingredient['produit'] = input("Quel est le nom du produit ? ")
            ingredient['quantite'] = input("Quel est la quantité pour la recette ? ")
            for produit in data :
                pass
                
    pass

def rechercher_recette() :
    pass

def modifier_recette() :
    pass

def supprimer_recette() :
    pass
