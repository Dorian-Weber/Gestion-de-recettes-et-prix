import csv
import os
import json


def convertisseur_csv(paths, ligne, head) :
    """ Cette fonction permet d'écrire dans un ficher csv """
    fichier_existe = os.path.exists(paths)
    
    with open(paths, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= head)
        if not fichier_existe:
            writer.writeheader()
        writer.writerow(ligne)


def lecteur_csv(path) :
    '''Cette fonction permet de lire le ficher csv'''
    with open(path, 'r', encoding= 'utf-8', newline='') as file :
        reader = csv.DictReader(file)
        rows = list(reader)
    return rows

def restart_csv(path, ligne, head) :
    '''Cette fonction permet d'effacer le contenu du csv et de le réecrire'''
    with open(path, 'w', encoding= 'utf-8', newline='') as file :
        writer = csv.DictWriter (file, fieldnames= head)
        writer.writeheader()
        writer.writerows(ligne)

def convertisseur_Json(path, data) :
    with open(path, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def lecteur_Json(path) :
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def restart_Json() :
    pass