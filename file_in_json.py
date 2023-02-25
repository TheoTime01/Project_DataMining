"""ce script permet de creer un fichier json avec les metadatas des images"""

from PIL import Image
import os
import json
from datetime import datetime

img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\pokemon_jpg" # path to the directory containing the images

# initialize a dictionary to store the metadata for all images
all_metadata = {}

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


# specify the path to the output JSON file
json_path = r"C:\Users\Tototime\Desktop\Project_DataMining\database.json"

# save the metadata for all images in a JSON file
with open(json_path, "w") as f:
    json.dump(all_metadata, f, indent=4)

