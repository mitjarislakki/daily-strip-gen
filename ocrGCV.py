import re
import pandas as pd
import os
from google.cloud import vision_v1
import concurrent.futures
debug = False

def preprocess(text):
    text = text.lower()
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('\n', ' ')
    return re.sub(r'\d+', '', text).strip()

lng = 'fi'  # Finnish language hint, if supported
inputDir = 'frameSet/'

client = vision_v1.ImageAnnotatorClient()
try:
    existingDf = pd.read_csv('computerVision.csv')
except FileNotFoundError:
    pass

def process_image(imgPath):
    if debug: print(f'Starting {imgPath}')
    with open(imgPath, 'rb') as image_file:
        content = image_file.read()
    image = vision_v1.types.Image(content=content)
    
    image_context = vision_v1.types.ImageContext(language_hints=[lng])
    textD = client.text_detection(image=image, image_context=image_context)
    
    if textD.text_annotations:
        text = textD.text_annotations[0].description
        text = preprocess(text)
        row = {
            'texts': text,
            'img': imgPath
        }
        return row
    else:
        return {}

# List of image paths
imgPaths = []

for filename in os.listdir(inputDir):
    imgPath = os.path.join(inputDir, filename)
    imgPaths.append(imgPath)

# Paralellized processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    rowList = list(executor.map(process_image, imgPaths))

df = pd.DataFrame(rowList)

if 'existingDf' in locals():
    df = pd.concat([existingDf, df])

df = df.dropna()

df.to_csv("computerVision.csv", index=False, encoding="utf-8")