"""
This module contains the functions to visualise the results of the recommended pokemon
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import os
import cv2
import random
from PIL import Image
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import graphviz
import pydotplus
from IPython.display import Image, display
import pickle

def visualisation(id):
    # afficher l'image du pokemon
    img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\pokemon_jpg" # path to the directory containing the images
    # afficher les informations du pokemon
    with open('database.json', 'r') as f:
        data = json.load(f)
    for key in data:
        if data[key]["id"] == id:
            print("Nom du pokemon: ", data[key]["nom"])
            print("Type du pokemon: ", data[key]["tags"]["Type 1"])
            print("Type du pokemon: ", data[key]["tags"]["Type 2"])
            print("Generation: ", data[key]["tags"]["Generation"])
            print("Legendary: ", data[key]["tags"]["Legendary"])
            # print("Total: ", data[key]["tags"]["Total"])

    for img_filename in os.listdir(img_dir):
    if img_filename.endswith(".jpg") or img_filename.endswith(".png"):
        if img_filename.split(".")[0] == str(id):
            img_path = os.path.join(img_dir, img_filename)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img)
    # afficher un histogramme des pokemons de types similaires et leurs generation au pokemon choisi
    # le faire pour Type 1 et Type 2 du pokemon choisi
    sim=[]
    for key in data:
            type1 = data[key]["tags"]["Type 1"]
            type2 = data[key]["tags"]["Type 2"]
            generation = data[key]["tags"]["Generation"]
            if type1 == data[str(id)]["tags"]["Type 1"] or type1 == data[str(id)]["tags"]["Type 2"] or type2 == data[str(id)]["tags"]["Type 1"] or type2 == data[str(id)]["tags"]["Type 2"]:
                sim.append(generation)
    hist=np.histogram(sim, bins=numpy.arange(1, 9, 1))
    bars=plt.bar(hist[1][:-1], hist[0], width=0.8, align='edge')
    for i in range(len(bars)):
            bars[i].set_color(
                "#%02x%02x%02x"
                % (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
            )
    #afficher un graphique circulaire des pokemons de couleur similaire au pokemon choisi et s'ils sont legendary ou non
    leg=[]
    for key in data:
        color = data[key]["tags"]["Color"]
        legendary = data[key]["tags"]["Legendary"]
        if color == data[str(id)]["tags"]["Color"]:
            leg.append(legendary)
    plt.pie([leg.count(False),leg.count(True)], labels=["False","True"], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')

    plt.show()

    

visualisation(1)