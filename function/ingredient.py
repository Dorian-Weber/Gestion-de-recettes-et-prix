from function.base_de_donnee import convertisseur_csv, lecteur_csv,restart_csv
import Levenshtein

def ajouter_ingredient() :
    '''Cette fonction sert a ajouter un ingrédient '''
    while True :
        produit = input("Quel est l'ingrédient ? ").capitalize()
        quantite = input("Quelle est la quantité (g, ml ou nombre) ? ")
        prix = input("Quel est le prix (en €)? ")

        newIngredient = {'produit': produit, 'quantite': quantite, 'prix': prix}
        while True :
            choix = input(f''' 
                        Voulez vous ajouter : 
                        Produit : {produit}
                        Quantité : {quantite} (g, ml ou nombre)
                        Prix : {prix} €

                        1- Oui 
                        2- Non 
                        0- Quitter
                        ''')
        
            if choix.isdigit() and int(choix) == 1 :
                convertisseur_csv('ingredient.csv', newIngredient ,['produit','quantite','prix'])
                break
            elif choix.isdigit() and  int(choix) == 2 :
                continue
            elif choix.isdigit() and  int(choix) == 0 :
                break
            else :
                print("Le chiffre écris n'est pas valide")
                continue
        if choix.isdigit() and (int(choix) == 1 or int(choix) ==0):
            break





def afficher_ingredient():
    ingredients = lecteur_csv('ingredient.csv')
    while True :
        choix = input(f'''
                    Que voulez vous afficher ? 
                    1- La liste de tout les ingrédients enregistré ? 
                    2- Un ingrédient de votre choix ?
                    0- Retour Menu 
                    ''')

        if choix.isdigit() and int(choix) == 1 :
            for ingredient in ingredients :
                print(f'''
                    Produit : {ingredient['produit']}
                    Quantité : {ingredient['quantite']}g
                    Prix : {ingredient['prix']} €''')

        elif choix.isdigit() and int(choix) == 2 :
            newchoix = str(input(f"Quel ingrédient chercher vous ? ").capitalize())
            for ingredient in ingredients :
                if ingredient['produit'] == newchoix :
                    print(f'''
                        Produit : {ingredient['produit']}
                        Quantité : {ingredient['quantite']}(g, ml ou nombre)
                        Prix : {ingredient['prix']} € ''')
                    break

            else :
                for ingredient in ingredients :
                    dst = Levenshtein.distance(ingredient['produit'], newchoix.strip())
                    if dst < 3 :
                        newChoix = input(f'''
                                Vous chercher {ingredient['produit']} ?
                                1- Oui 
                                0- Non ''')
                        if newChoix.isdigit() and int(newChoix) == 1:
                            print(f'''
                            Produit : {ingredient['produit']}
                            Quantité : {ingredient['quantite']}(g, ml ou nombre)
                            Prix : {ingredient['prix']} € ''')
                            break
                        elif newChoix.isdigit() and int(newChoix) == 0:
                            continue

        elif choix.isdigit() and int(choix) == 0 :
            break
        else :
            print("Le nombre saisis n'est pas valide.")
            continue

def modifier_ingredient():
    ingredients = lecteur_csv('ingredient.csv')
    choix = str(input(f'''Quel ingrédient voulez vous modifier ? ''').capitalize())
    for ingredient in ingredients :
        if ingredient['produit'] == choix :
            newChoix = input(f'''Voulez vous modifier {ingredient['produit']} ?
                                1- Oui 
                                0- Non (retour) 
                             ''')
            if newChoix.isdigit() and int(newChoix) == 1 :
                ingredient['quantite'] = input(f"Qu'elle est la quantite de {ingredient['produit']} ? ")
                ingredient['prix'] = input(f"Quel est le prix de {ingredient['produit']} ? ")
                restart_csv('ingredient.csv',ingredients,['produit','quantite','prix'])
            elif newChoix.isdigit() and int(newChoix) == 0 :
                break
    else :
        for ingredient in ingredients :
            dst = Levenshtein.distance(ingredient['produit'], choix.strip())
            if dst < 3 :
                newChoix = input(f'''
                                Vous voulez modifier {ingredient['produit']} ?
                                1- Oui 
                                0- Non
                                ''')
                if newChoix.isdigit() and int(newChoix) == 1 :
                    ingredient['quantite'] = input(f"Qu'elle est la quantite de {ingredient['produit']} ? ")
                    ingredient['prix'] = input(f"Quel est le prix de {ingredient['produit']} ? ")
                    restart_csv('ingredient.csv',ingredients,['produit','quantite','prix'])
                elif newChoix.isdigit() and int(newChoix) == 0 :
                    continue

def supprimer_ingredient() :
    ingredients = lecteur_csv('ingredient.csv')
    choix = str(input(f'''Quel ingrédient voulez vous supprimer ? ''').capitalize())
    for ingredient in ingredients.copy() :
        if ingredient['produit'] == choix :
            newChoix = input(f'''Voulez vous supprimer {ingredient['produit']} ?
                                1- Oui 
                                0- Non (retour) 
                             ''')
            if newChoix.isdigit() and int(newChoix) == 1 :
                ingredients.remove(ingredient)
                print(f"{ingredient['produit']} supprimer ! ")
                restart_csv('ingredient.csv',ingredients,['produit','quantite','prix'])
            elif newChoix.isdigit() and int(newChoix) == 0 :
                break

            