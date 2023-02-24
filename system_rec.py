"""
Ce fichier contient les fonctions de recommandation de systèmes.
Objectif : recommander des pokémons en fonction des préférences de l'utilisateur.
Entrées:
- la couleur préférée de l'utilisateur
- la génération préférée de l'utilisateur
- le type 1 préféré de l'utilisateur
- le type 2 préféré de l'utilisateur (peut être vide)
- si l'utilisateur aime les pokémons légendaires ou non

Sorties:
- une liste de pokémons recommandés (image, nom, type 1, type 2, génération, couleur, légendaire ou non)
"""

import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import pickle
import json
import random
from PIL import Image

#Interface utilisateur
couleur = input("Quelle est votre couleur préférée? ")
generation = input("Quelle est votre génération préférée? ")
type1 = input("Quel est votre type 1 préféré? ")
type2 = input("Quel est votre type 2 préféré? ")
legendary = input("Aimez-vous les pokémons légendaires? ")

# Importer le modèle
with open('model.pkl', 'rb') as file:
    dtc_model = pickle.load(file)

# Créer un dataframe pour le nouveau Pokémon
pokemon = pd.DataFrame([[type1, type2, generation, couleur, legendary]], columns=["Type 1", "Type 2","Generation", "color", "legendary"])

# Prétraiter les données pour les encoder
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
le5 = LabelEncoder()
le6 = LabelEncoder()

pokemon["Type 1"] = le1.fit_transform(pokemon["Type 1"])
pokemon["Type 2"] = le2.fit_transform(pokemon["Type 2"])
pokemon["color"] = le3.fit_transform(pokemon["color"])
pokemon["Generation"] = le4.fit_transform(pokemon["Generation"])
pokemon["legendary"] = le5.fit_transform(pokemon["legendary"])

# Prédire si le Pokémon sera favori ou non
prediction = dtc_model.predict(pokemon)

# Afficher la prédiction
if prediction[0] == 0:
    print("Le Pokémon sera favori")
else:
    print("Le Pokémon ne sera pas favori")

# Importer le fichier json
with open('database.json') as file:
    result={}
    ata=json.load(f)
    #on prend les pokemons non utilisés dans le modèle
    while len(result)>577:
        for i in data:
            result[i]=data[i]

# Créer une liste vide pour les pokémons recommandés
recommandations = []

# Ajouter les pokémons recommandés à la liste
for pokemon in result:
    if result[pokemon]["color"] == couleur and result[pokemon]["Generation"] == generation and result[pokemon]["Type 1"] == type1 and result[pokemon]["Type 2"] == type2 and result[pokemon]["legendary"] == legendary:
        recommandations.append(pokemon)

# Afficher les pokémons recommandés
print("Voici les pokémons recommandés: ")
for id in recommandations:
    # Afficher l'image du Pokémon
    img = Image.open("polemon_jpg/" + str(id) + ".jpg")
img.show()