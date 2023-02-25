"""Ce script permet de déterminer la couleur prédominante d'une image."""
import os
from PIL import Image
import numpy as np
import json

img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\pokemon_jpg" # path to the directory containing the images
color_data={}
for img_filename in os.listdir(img_dir):
    if img_filename.endswith(".jpg") or img_filename.endswith(".png"):
        # construct the full path to the image file
        img_path = os.path.join(img_dir, img_filename)
        # Ouvrir l'image
        with Image.open(img_path) as img:
            
            # Extraire la matrice de pixels
            pixel_matrix = np.array(img)

            # Extraire les valeurs R, G, B
            r = pixel_matrix[:, :, 0].flatten()
            g = pixel_matrix[:, :, 1].flatten()
            b = pixel_matrix[:, :, 2].flatten()

            # Calculer la couleur moyenne
            mean_r = np.mean(r)
            mean_g = np.mean(g)
            mean_b = np.mean(b)

            # Déterminer la couleur prédominante
            if mean_r >= mean_g and mean_r >= mean_b:
                main_color = "rouge"
            elif mean_g >= mean_r and mean_g >= mean_b:
                main_color = "vert"
            else:
                main_color = "bleu"

            # create a dictionary of the colors for this image
            color = {
                "couleur dominante": main_color,
                "rouge": mean_r,
                "vert": mean_g,
                "bleu": mean_b
            }
            # add the color for this image to the dictionary of all colors
            color_data[(img_filename.split("\\")[-1]).split(".")[0]] = color

# specify the path to the output JSON file
json_path = r"C:\Users\Tototime\Desktop\Project_DataMining\database.json"

# Browse the JSON file and add the corresponding colors
with open(json_path, 'r+') as f:
    data = json.load(f)
    for image in data.values():
        image_id = image['id']
        if image_id in color_data:
            image['couleur'] = color_data[image_id]
    f.seek(0) # rewind
    json.dump(data, f, indent=4)  # save the colors for all images in a JSON file
    f.truncate() # remove remaining part



