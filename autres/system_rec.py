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

satisfait = False

# Importer le fichier json
with open('test.json') as f:
    data=json.load(f)

# Importer le modèle
with open('prediction_model.pkl', 'rb') as file:
    dtc_model = pickle.load(file)

recommandations = []

while not satisfait:
    # Interface utilisateur
    couleur = input("Quelle est votre couleur préférée? ")
    generation = int(input("Quelle est votre génération préférée? "))
    type1 = input("Quel est votre type 1 préféré? ")
    type2 = input("Quel est votre type 2 préféré? ")
    legendary = bool(input("Aimez-vous les pokémons légendaires? "))


    # Créer un dataframe pour le nouveau Pokémon
    pokemon = pd.DataFrame([[type1, type2, generation, couleur, legendary]], columns=["Type 1", "Type 2","Generation", "color", "legendary"])

    # Prétraiter les données pour les encoder
    le1 = LabelEncoder()
    le2 = LabelEncoder()
    le3 = LabelEncoder()
    le4 = LabelEncoder()
    le5 = LabelEncoder()
    le6 = LabelEncoder()

    pokemon["Type 1"] = le1.fit_transform(pokemon["Type 1"].values)
    pokemon["Type 2"] = le2.fit_transform(pokemon["Type 2"].values)
    pokemon["color"] = le3.fit_transform(pokemon["color"].values)
    pokemon["Generation"] = le4.fit_transform(pokemon["Generation"].values)
    pokemon["legendary"] = le5.fit_transform(pokemon["legendary"].values)

    # Prédire si le Pokémon sera favori ou non
    prediction = dtc_model.predict(pokemon.values)

    # Afficher la prédiction
    if prediction[0] == 0:
        print("Le Pokémon sera favori")
        # Ajouter les pokémons recommandés à recommandations 
        for pokemon_id, pokemon_data in data.items():
            if (pokemon_data["color"]["couleur dominante"] == couleur 
                    or pokemon_data["tags"]["Generation"] == generation 
                    or (pokemon_data["tags"]["Type 1"] == type1 and pokemon_data["tags"]["Type 2"] == type2) 
                    or (pokemon_data["tags"]["Type 1"] == type2 and pokemon_data["tags"]["Type 2"] == type1) 
                    or not(pokemon_data["tags"]["Legendary"]^legendary)):
                recommandations.append(pokemon_data)

        # Afficher les pokémons recommandés
        print("Voici les pokémons recommandés:")
        for id in recommandations:
            print(recommandations[id]["tags"]["Name"])
        
        satisfait = True
    else:
        print("Le Pokémon ne sera pas favori")
        satisfait = False

