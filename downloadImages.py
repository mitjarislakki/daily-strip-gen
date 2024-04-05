import pandas as pd
import requests
import os

dir = os.path.dirname(__file__)
dir = os.path.join(dir, "imageSet/")
if not os.path.exists(dir): os.mkdir(dir)

src = "links.csv"
df = pd.read_csv(src)
# df = df.head(2)
for index, row in df.iterrows():
    url = row['links']
    data = requests.get(url).content
    f = open(f'{dir}{index}.jpg', 'wb')
    f.write(data)
    f.close()