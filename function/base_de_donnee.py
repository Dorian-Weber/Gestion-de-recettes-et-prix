import csv
import os
import json

def convertisseur_csv(path, ligne, head):
    fichier_existe = os.path.exists(path)
    with open(path, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=head)
        if not fichier_existe:
            writer.writeheader()
        writer.writerow(ligne)


def lecteur_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


def restart_csv(path, lignes, head):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=head)
        writer.writeheader()
        writer.writerows(lignes)


def convertisseur_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def lecteur_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)