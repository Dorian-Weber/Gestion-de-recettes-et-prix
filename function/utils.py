def demander_nombre(message, valeurs_valides=None):
    while True:
        choix = input(message).strip()
        if choix.isdigit():
            choix = int(choix)
            if valeurs_valides is None or choix in valeurs_valides:
                return choix
        print("Le nombre saisi n'est pas valide.")


def confirmer(message="Confirmer ? (1=oui, 0=non) : "):
    return demander_nombre(message, [0, 1]) == 1


def boucle(function):
    while True:
        function()
        choix = demander_nombre("""
        1 - Continuer
        0 - Retour au menu
        Votre choix : """, [0, 1])
        if choix == 0:
            break