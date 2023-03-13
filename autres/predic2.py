from sklearn import tree
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus
from IPython.display import Image, display
import json
import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
import random


# Importer le modèle
with open('prediction_model.pkl', 'rb') as file:
    dtc_model = pickle.load(file)

# Créer un dataframe pour le nouveau Pokémon
golurk = pd.DataFrame([["Grass", "Poison", "3", "vert", False]], columns=["Type 1", "Type 2","Generation", "color", "legendary"])

# Prétraiter les données pour les encoder
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()
le5 = LabelEncoder()
le6 = LabelEncoder()

golurk["Type 1"] = le1.fit_transform(golurk["Type 1"])
golurk["Type 2"] = le2.fit_transform(golurk["Type 2"])
golurk["color"] = le3.fit_transform(golurk["color"])
golurk["Generation"] = le4.fit_transform(golurk["Generation"])
golurk["legendary"] = le5.fit_transform(golurk["legendary"])

# Prédire si le Pokémon sera favori ou non
prediction = dtc_model.predict(golurk)

# Afficher la prédiction
if prediction[0] == 0:
    print("Le Pokémon sera favori")
else:
    print("Le Pokémon ne sera pas favori")

with open('database.json') as f:
    data=json.load(f)

print(len(data))