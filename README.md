# Gestion d’Ingrédients et de Recettes
📌 Présentation du programme
Ce logiciel permet de gérer :
- des ingrédients (nom, quantité, prix d’achat)
- des recettes composées d’un nombre illimité d’ingrédients
- le coût matière d’une recette
- le prix conseillé (250% du coût matière)
Il fonctionne entièrement en mode console et ne nécessite aucune connaissance technique.


📁 Structure du dossier
Le dossier fourni contient :
MonProgramme/
│
├── main.exe                → programme à lancer
├── data/
│   ├── ingredient.csv      → base de données des ingrédients
│   └── recettes.json       → base de données des recettes
└── README.txt              → ce fichier


▶️ Comment lancer le programme
- Ouvrez le dossier MonProgramme.
- Double‑cliquez sur main.exe.
- Le menu principal s’affiche.
Aucune installation n’est nécessaire.


🧭 Menu principal
Le programme propose les actions suivantes :
1 - Ajouter un ingrédient
2 - Afficher les ingrédients
3 - Modifier un ingrédient
4 - Supprimer un ingrédient
5 - Enregistrer une recette
6 - Afficher les recettes
7 - Modifier une recette
8 - Supprimer une recette
0 - Quitter


🥚 Gestion des ingrédients
➕ Ajouter un ingrédient
Vous devez fournir :
- le nom
- la quantité achetée (en g, ml ou unité)
- le prix total payé
Exemple :
Nom : Oeuf
Quantité : 12
Prix : 3


📄 Afficher les ingrédients
Vous pouvez afficher :
- toute la liste
- un ingrédient précis (avec recherche approximative)
✏️ Modifier un ingrédient
Vous pouvez changer :
- la quantité
- le prix
❌ Supprimer un ingrédient
L’ingrédient est retiré du fichier CSV.


🍽️ Gestion des recettes
➕ Ajouter une recette
Vous devez fournir :
- le nom de la recette
- les ingrédients utilisés
- la quantité utilisée pour chaque ingrédient
Le programme calcule automatiquement :
- le coût matière
- le prix conseillé = coût × 2.5 (250%)
📄 Afficher les recettes
Vous pouvez afficher :
- la liste des recettes
- le détail d’une recette (ingrédients + coûts)
✏️ Modifier une recette
Deux options :
- renommer la recette
- la recréer entièrement
❌ Supprimer une recette
Elle est retirée du fichier JSON.


💾 Où sont stockées les données ?
Les données sont enregistrées automatiquement dans :
- data/ingredient.csv
- data/recettes.json
Vous pouvez les sauvegarder ou les transférer sur un autre ordinateur.

⚠️ Conseils d’utilisation
- Ne modifiez pas les fichiers CSV/JSON à la main si vous n’êtes pas sûr de ce que vous faites.
- Ne supprimez pas le dossier data.
- Si vous déplacez le programme, gardez le dossier data avec lui.


✅ Support
Si vous rencontrez un problème, contactez la personne qui vous a fourni le programme.

Merci d’utiliser ce logiciel ! Bon appétit ! 🍽️