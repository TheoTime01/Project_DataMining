import os
import json
import numpy as np
from PIL import Image
from sklearn.cluster import MiniBatchKMeans
import csv

img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\pokemon_jpg" # path to the directory containing the images
color_data={}
color_map = {}

# Load the color map from CSV
with open(r'C:\Users\Tototime\Desktop\Project_DataMining\data\color_names.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # skip the header
    for row in reader:
        name, hex_value = row[0], row[1]
        color_map[hex_value] = name

for img_filename in os.listdir(img_dir):
    if img_filename.endswith(".jpg") or img_filename.endswith(".png"):
        # construct the full path to the image file
        img_path = os.path.join(img_dir, img_filename)
        # Ouvrir l'image
        with Image.open(img_path) as img:
            # Extraire la matrice de pixels
            pixel_matrix = np.array(img)

            # Extraire les valeurs R, G, B
            pixel_data = pixel_matrix.reshape((-1, 3))

            # Utiliser MiniBatchKMeans pour trouver le cluster le plus grand
            kmeans = MiniBatchKMeans(n_clusters=5, random_state=0).fit(pixel_data)
            main_color = kmeans.cluster_centers_[np.argmax(np.unique(kmeans.labels_, return_counts=True)[1])]
            hex_value = '#{:02x}{:02x}{:02x}'.format(int(main_color[0]), int(main_color[1]), int(main_color[2]))

            # Get the color name from the color map
            color_name = color_map[hex_value]

            # create a dictionary of the colors for this image
            color = {
                "couleur dominante": main_color.tolist(),
                "nom couleur": color_name
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