from PIL import Image
import os
import json
from datetime import datetime

img_dir = r"C:\Users\Tototime\Desktop\Project_DataMining\Ramen"

# initialize a dictionary to store the metadata for all images
all_metadata = {}

# loop through all image files in the directory
for img_filename in os.listdir(img_dir):
    if img_filename.endswith(".jpg") or img_filename.endswith(".png"):
        # construct the full path to the image file
        img_path = os.path.join(img_dir, img_filename)

        # open the image file
        with Image.open(img_path) as img:

            # extract the image metadata
            img_format = img.format
            img_size = img.size
            img_orientation = "landscape" if img_size[0] > img_size[1] else "portrait"
            creation_date =  datetime.fromtimestamp(os.path.getctime(img_path)).strftime('%d/%m/%Y')

            # create a dictionary of metadata for this image
            metadata = {
                "format": img_format,
                "size": img_size,
                "orientation": img_orientation,
                "creation_date": creation_date
            }

            # add the metadata for this image to the dictionary of all metadata
            all_metadata[img_filename] = metadata

# specify the path to the output JSON file
json_path = r"C:\Users\Tototime\Desktop\Project_DataMining\database.json"

# save the metadata for all images in a JSON file
with open(json_path, "w") as f:
    json.dump(all_metadata, f, indent=4)
