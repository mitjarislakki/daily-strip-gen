from google.cloud import vision_v1
import os
import pandas as pd
import re

def preprocess(text):
    text = text.lower()
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('\n', ' ')
    return re.sub(r'\d+', '', text).strip()

def describe_local_image(image_path, language_hint=None):
    client = vision_v1.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    if language_hint:
        image_context = vision_v1.types.ImageContext(language_hints=[language_hint])
        response = client.label_detection(image=image, image_context=image_context)
    else:
        response = client.label_detection(image=image)

    labels = response.label_annotations

    return [label.description for label in labels]

def ocr(imgPath, languageHint = None):
    client = vision_v1.ImageAnnotatorClient()

    with open(imgPath, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    if languageHint:
        image_context = vision_v1.types.ImageContext(language_hints=[languageHint])
        response = client.text_detection(image=image, image_context=image_context)
    else:
        response = client.text_detection(image=image)

    texts = response.text_annotations

    return [text.description for text in texts]

# Example usage
# descriptions = describe_local_image(image_path, language_hint)
# print(descriptions)

# text = ocr(image_path, lng)
# descriptions = describe_local_image(image_path, lng)
# print(text)
# print(descriptions)

lng = 'fi'  # Finnish language hint, if supported
inputDir = 'frameSet/'

rowList = [] # Accumulator for dataframe

run = True
count = 0
if run: 
    for filename in os.listdir(inputDir):
        imgPath = os.path.join(inputDir, filename)
        client = vision_v1.ImageAnnotatorClient()
        with open(imgPath, 'rb') as image_file:
            content = image_file.read()
        image = vision_v1.types.Image(content=content)
        
        image_context = vision_v1.types.ImageContext(language_hints=[lng])
        textD = client.text_detection(image=image, image_context=image_context)
        # objectD = client.object_detection(image=image, image_context=image_context)
        # labelD = client.label_detection(image=image, image_context=image_context)
        
        if textD.text_annotations:
            text = textD.text_annotations[0].description
            text = preprocess(text)
            # labels = labelD.label_annotations
            row = {
                'texts': text,
                'img': imgPath
                # 'labels': labels
            }
            rowList.append(row)
        count += 1
        print(count)
        if count == 50: break


df = pd.DataFrame(rowList)
df.to_csv("computerVision.csv", index=False, encoding="utf-8")