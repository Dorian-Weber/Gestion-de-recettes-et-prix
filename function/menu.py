from function.ingredient import (
    ajouter_ingredient,
    afficher_ingredient,
    modifier_ingredient,
    supprimer_ingredient
)
from function.recette import (
    ajouter_recette,
    afficher_recettes,
    modifier_recette,
    supprimer_recette
)
from function.utils import demander_nombre, boucle

ACTIONS = {
    1: ajouter_ingredient,
    2: afficher_ingredient,
    3: modifier_ingredient,
    4: supprimer_ingredient,
    5: ajouter_recette,
    6: afficher_recettes,
    7: modifier_recette,
    8: supprimer_recette,
}

def menu():
    while True:
        choix = demander_nombre("""
        Que voulez-vous faire ?
        1 - Ajouter un ingrédient
        2 - Afficher les ingrédients
        3 - Modifier un ingrédient
        4 - Supprimer un ingrédient
        5 - Enregistrer une recette
        6 - Afficher les recettes
        7 - Modifier une recette
        8 - Supprimer une recette
        0 - Quitter
        Votre choix : """, valeurs_valides=range(0, 9))

        if choix == 0:
            break

        action = ACTIONS.get(choix)

        if action is None:
            print("Fonction non encore implémentée.")
            continue

        boucle(action)