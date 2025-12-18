from function.base_de_donnee import convertisseur_csv, lecteur_csv, restart_csv
from function.utils import demander_nombre, confirmer
import Levenshtein

PATH = "data/ingredient.csv"
HEAD = ["produit", "quantite", "prix"]


def trouver_ingredient(nom, ingredients):
    nom = nom.strip().capitalize()

    # Recherche exacte
    for ing in ingredients:
        if ing["produit"] == nom:
            return ing

    # Recherche approximative
    for ing in ingredients:
        if Levenshtein.distance(ing["produit"], nom) < 3:
            if confirmer(f"Voulez-vous dire {ing['produit']} ? (1=oui, 0=non) : "):
                return ing

    return None


def ajouter_ingredient():
    produit = input("Nom de l'ingrédient : ").capitalize()
    quantite = input("Quantité (g, ml ou unité) : ")
    prix = input("Prix (€) : ")

    new_ing = {"produit": produit, "quantite": quantite, "prix": prix}

    if confirmer("Confirmer l'ajout ? (1=oui, 0=non) : "):
        convertisseur_csv(PATH, new_ing, HEAD)
        print("Ingrédient ajouté.")


def afficher_ingredient():
    ingredients = lecteur_csv(PATH)

    choix = demander_nombre("""
    1 - Afficher tous les ingrédients
    2 - Rechercher un ingrédient
    0 - Retour
    Votre choix : """, [0, 1, 2])

    if choix == 1:
        for ing in ingredients:
            print(f"{ing['produit']} - {ing['quantite']} - {ing['prix']} €")

    elif choix == 2:
        nom = input("Nom recherché : ")
        ing = trouver_ingredient(nom, ingredients)
        if ing:
            print(f"{ing['produit']} - {ing['quantite']} - {ing['prix']} €")
        else:
            print("Aucun ingrédient trouvé.")


def modifier_ingredient():
    ingredients = lecteur_csv(PATH)
    nom = input("Quel ingrédient modifier ? ")

    ing = trouver_ingredient(nom, ingredients)
    if not ing:
        print("Aucun ingrédient trouvé.")
        return

    ing["quantite"] = input("Nouvelle quantité : ")
    ing["prix"] = input("Nouveau prix : ")

    restart_csv(PATH, ingredients, HEAD)
    print("Ingrédient modifié.")


def supprimer_ingredient():
    ingredients = lecteur_csv(PATH)
    nom = input("Quel ingrédient supprimer ? ")

    ing = trouver_ingredient(nom, ingredients)
    if not ing:
        print("Aucun ingrédient trouvé.")
        return

    if confirmer(f"Supprimer {ing['produit']} ? (1=oui, 0=non) : "):
        ingredients.remove(ing)
        restart_csv(PATH, ingredients, HEAD)
        print("Ingrédient supprimé.")