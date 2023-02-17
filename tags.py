"""ce script permet d'ajouter les tags aux images du dataset"""

import json
import csv

# Charger le contenu du fichier CSV dans un dictionnaire
tags_dict = {}
with open(r'C:\Users\Tototime\Desktop\Project_DataMining\data\Pokemon.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # on recupere les noms des colonnes
    columns = next(reader)
    for row in reader:
        # on recupere l'id de l'image
        image_id = row[0]
        # on recupere les tags 
        for i in range(1, len(row)):
            if row[i] != '':
                # on ajoute le tag dans le dictionnaire
                if image_id in tags_dict:
                    tags_dict[image_id].append(columns[i]+':'+row[i])
                else:
                    tags_dict[image_id] = [columns[i] + ':' + row[i]]


# Parcourir le fichier JSON et ajouter les tags correspondants
with open('database.json', 'r+') as f:
    data = json.load(f)
    for image in data.values():
        image_id = image['id']
        if image_id in tags_dict:
            image['tags'] = tags_dict[image_id]
    f.seek(0) # on remet le curseur au debut du fichier
    json.dump(data, f, indent=4) # on ecrit le nouveau contenu
    f.truncate() # on supprime le reste du fichier