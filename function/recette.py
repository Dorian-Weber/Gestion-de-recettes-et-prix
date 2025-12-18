from function.base_de_donnee import lecteur_csv, lecteur_json, convertisseur_json
from function.utils import demander_nombre, confirmer
import Levenshtein

PATH_RECETTES = "data/recettes.json"
PATH_INGREDIENTS = "data/ingredient.csv"
MARGE_MULTIPLICATEUR = 2.5  # 250%



# Fonction de cacul.

def charger_recettes():
    recettes = lecteur_json(PATH_RECETTES)
    if not isinstance(recettes, list):
        return []
    return recettes


def sauvegarder_recettes(recettes):
    convertisseur_json(PATH_RECETTES, recettes)


def charger_ingredients():
    return lecteur_csv(PATH_INGREDIENTS)


def trouver_ingredient_stock(nom, ingredients):
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


def demander_float(message):
    while True:
        valeur = input(message).replace(",", ".").strip()
        try:
            return float(valeur)
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def calculer_cout_ingredient(ing_stock, quantite_utilisee):
    try:
        quantite_stock = float(str(ing_stock["quantite"]).replace(",", ".").strip())
        prix_stock = float(str(ing_stock["prix"]).replace(",", ".").strip())
    except (KeyError, ValueError):
        print("Données ingrédient invalides dans le CSV.")
        return 0.0

    if quantite_stock == 0:
        return 0.0

    prix_unitaire = prix_stock / quantite_stock
    return prix_unitaire * quantite_utilisee


# Fonction du menu

def ajouter_recette():
    recettes = charger_recettes()
    ingredients_stock = charger_ingredients()

    if not ingredients_stock:
        print("Aucun ingrédient enregistré. Impossible de créer une recette.")
        return

    nom = input("Nom de la recette : ").strip().capitalize()
    if not nom:
        print("Nom de recette invalide.")
        return

    ingredients_recette = []
    cout_total = 0.0

    while True:
        produit = input("Nom de l'ingrédient utilisé (0 pour Quitter) : ").strip()
        if produit == "0":
            break

        ing_stock = trouver_ingredient_stock(produit, ingredients_stock)
        if not ing_stock:
            print("Ingrédient introuvable dans le stock.")
            continue

        quantite_utilisee = demander_float("Quantité utilisée (en g, ml ou unité) : ")

        cout = calculer_cout_ingredient(ing_stock, quantite_utilisee)
        cout_total += cout

        ingredients_recette.append({
            "produit": ing_stock["produit"],
            "quantite": quantite_utilisee,
            "cout": round(cout, 2)
        })

        if not confirmer("Ajouter un autre ingrédient ? (1=oui, 0=non) : "):
            break

    if not ingredients_recette:
        print("Aucun ingrédient ajouté, recette annulée.")
        return

    cout_total = round(cout_total, 2)
    prix_conseille = round(cout_total * MARGE_MULTIPLICATEUR, 2)

    recette = {
        "nom": nom,
        "ingredients": ingredients_recette,
        "cout_matiere": cout_total,
        "prix_conseille": prix_conseille
    }

    recettes.append(recette)
    sauvegarder_recettes(recettes)

    print(f"Recette '{nom}' enregistrée.")
    print(f"Coût matière : {cout_total} €")
    print(f"Prix conseillé (250% du coût) : {prix_conseille} €")


def afficher_recettes():
    recettes = charger_recettes()

    if not recettes:
        print("Aucune recette enregistrée.")
        return

    choix = demander_nombre("""
    1 - Liste des recettes
    2 - Détail d'une recette
    0 - Retour
    Votre choix : """, [0, 1, 2])

    if choix == 0:
        return

    if choix == 1:
        for i, r in enumerate(recettes, start=1):
            print(f"{i}. {r['nom']} - Coût matière : {r['cout_matiere']} € - Prix conseillé : {r['prix_conseille']} €")

    elif choix == 2:
        nom = input("Nom de la recette à afficher : ").strip().capitalize()
        for r in recettes:
            if r["nom"] == nom:
                print(f"Recette : {r['nom']}")
                print(f"Coût matière : {r['cout_matiere']} €")
                print(f"Prix conseillé : {r['prix_conseille']} €")
                print("Ingrédients :")
                for ing in r["ingredients"]:
                    print(f" - {ing['produit']} : {ing['quantite']} (coût {ing['cout']} €)")
                break
        else:
            print("Recette introuvable.")


def modifier_recette():
    recettes = charger_recettes()
    if not recettes:
        print("Aucune recette à modifier.")
        return

    nom = input("Nom de la recette à modifier : ").strip().capitalize()

    for index, r in enumerate(recettes):
        if r["nom"] == nom:
            print(f"Recette trouvée : {r['nom']}")
            choix = demander_nombre("""
            1 - Renommer la recette
            2 - Recréer complètement la recette
            0 - Annuler
            Votre choix : """, [0, 1, 2])

            if choix == 0:
                return

            if choix == 1:
                nouveau_nom = input("Nouveau nom de la recette : ").strip().capitalize()
                if nouveau_nom:
                    recettes[index]["nom"] = nouveau_nom
                    sauvegarder_recettes(recettes)
                    print("Recette renommée.")
                else:
                    print("Nom invalide.")
                return

            if choix == 2:
                del recettes[index]
                sauvegarder_recettes(recettes)
                print("Ancienne recette supprimée, recréons-la.")
                ajouter_recette()
                return

    print("Recette introuvable.")


def supprimer_recette():
    recettes = charger_recettes()
    if not recettes:
        print("Aucune recette à supprimer.")
        return

    nom = input("Nom de la recette à supprimer : ").strip().capitalize()

    for index, r in enumerate(recettes):
        if r["nom"] == nom:
            if confirmer(f"Supprimer la recette '{r['nom']}' ? (1=oui, 0=non) : "):
                del recettes[index]
                sauvegarder_recettes(recettes)
                print("Recette supprimée.")
            else:
                print("Suppression annulée.")
            return

    print("Recette introuvable.")