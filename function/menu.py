from function.ingredient import ajouter_ingredient, afficher_ingredient,modifier_ingredient,supprimer_ingredient

def menu() :
    """Cette fonction permet d'afficher le menu"""
    while True :
        choix = input((f"""
                    Que voulez vous faire ?
                    1 - Ajouter un ingrédient acheter. (quantité, prix)
                    2 - Afficher ingrédient enregistré. (nom, quantité, prix)
                    3 - Modifier un ingrédient. (prix, quantité)
                    4 - Supprimer un ingrédient. (nom, prix, quantité)
                    5 - Enregistrer une nouvelle recette. (nom, ingrédient, quantité, prix estimée)
                    6 - Afficher des recettes enregistrée.
                    7 - Modifier une recette.
                    8 - Supprimer une recette enregistrée. 
                    0 - Quittez le programme
                    Entrez le nombre de l'action voulu :  
                       """)).strip()
        if choix.isdigit() and 0 <= int(choix) <= 8 :
            choix = int(choix)
            if choix == 0 : 
                break
            elif choix == 1 :
                boucle(ajouter_ingredient)
            elif choix == 2 :
                boucle(afficher_ingredient)
            elif choix == 3 :
                boucle(modifier_ingredient)
            elif choix == 4 :
                boucle(supprimer_ingredient)
            elif choix == 5 :
                pass
            elif choix == 6 :
                pass
            elif choix == 7 :
                pass
            elif choix == 8 :
                pass
        else :
            print("Le nombre saisie n'est pas valide")
            continue

def boucle(function) :
    while True :
        function()
        while True :
            newchoix = input(f'''
                1- continuer ? 
                0- retour au menu
                ''')
            if newchoix.isdigit() and (int(newchoix) == 1 or int(newchoix) == 0) :
                break
            else :
                print("Le nombre saisie n'est pas valide")
                continue
        if int(newchoix) == 0 :
            break