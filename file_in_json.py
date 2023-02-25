"""ce script permet de creer un fichier json avec les metadatas des images"""

from PIL import Image
import os
import json
from datetime import datetime
import numpy as np

img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\pokemon_jpg" # path to the directory containing the images

# initialize a dictionary to store the metadata for all images
all_metadata = {}
color_data={}

# loop through all image files in the directory
for img_filename in os.listdir(img_dir):
    if img_filename.endswith(".jpg") or img_filename.endswith(".png"):
        # construct the full path to the image file
        img_path = os.path.join(img_dir, img_filename)

        # open the image file
        with Image.open(img_path) as img:

            # remove images with a name which are not this format: 1.jpg, 2.jpg, 3.jpg, etc.
            if not img_filename.split(".")[0].isdigit():
                continue

            # extract the image metadata
            img_filename= img.filename
            img_format = img.format
            img_size = img.size
            img_orientation = "landscape" if img_size[0] > img_size[1] else "portrait"
            creation_date =  datetime.fromtimestamp(os.path.getctime(img_path)).strftime('%d/%m/%Y')

            # create a dictionary of metadata for this image
            metadata = {
                #on veut juste le nom de l'image
                "id": int((img_filename.split("\\")[-1]).split(".")[0]),
                "format": img_format,
                "size": img_size,
                "orientation": img_orientation,
                "creation_date": creation_date,
                "tags": ""
            }

            # add the metadata for this image to the dictionary of all metadata
            all_metadata[img_filename.split("\\")[-1]] = metadata

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
                "id": int((img_filename.split("\\")[-1]).split(".")[0]),
                "couleur dominante": main_color,
                "rouge": mean_r,
                "vert": mean_g,
                "bleu": mean_b
            }
            # add the color for this image to the dictionary of all colors
            color_data[img_filename.split("\\")[-1]] = color


# Add the the metadata to the JSON file
with open('database.json', "w") as f:
    json.dump(all_metadata, f, indent=4)

# Browse the JSON file and add the corresponding colors
with open('database.json', 'r') as f:
    data = json.load(f)

for key in data:
    for i in range(len(color_data)):
        if data[key]["id"] == color_data[key]["id"]:
            data[key]["color"] = color_data[key]

# Remove the id from the color data and save it in the JSON file
for key in data:
    del data[key]["color"]["id"]

with open('database.json', "w") as f:
    json.dump(data, f, indent=4)


