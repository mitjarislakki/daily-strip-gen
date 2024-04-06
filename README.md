# Daily comic strip generator
Tool developed in the Aaltoes AI x Art Build It -hackathon to take input text prompt and output matching frames, trained on Finnish language with FinBERT and Google Cloud Vision OCR.

`python -m venv stripgen`
### Dataset processing:
Store your source set in imageSet/, individual frames in frameSet/

`pip install pandas selenium beautifulsoup4 requests pillow`

Example dataset (fingerPori comic):
- Run fingerporiScraper.py
  - Accept cookies manually (For some reason Selenium can't find the button via XPath or CSS selectors?)
  - Wait for browser to close
- Run downloadImages.py
- Run splitAllStrips


### Image to text
- Install gcloud CLI https://cloud.google.com/sdk/docs/install
- Set up auth in gcloud: `gcloud auth application-default login`

`pip install google-cloud-vision pandas`
- run ocrGCV.py to create computerVision.csv, text data from the images using Google Computer Vision API

### Running model
`pip install transformers torch scikit-learn`

Once you have your frameSet & computerVision.csv set up, follow `Generator.pynb`, changing the input-variable