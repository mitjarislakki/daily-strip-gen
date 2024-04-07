# Daily comic strip generator
Tool developed in the Aaltoes AI x Art Build It -hackathon to take input text prompt and output matching frames, trained on Finnish language with FinBERT and Google Cloud Vision OCR.

`python -m venv stripgen`

`.\stripgen\Scripts\activate`

### Dataset processing:
Store your source set in imageSet/ (or individual frames in frameSet)

`pip install pandas selenium beautifulsoup4 requests pillow`

Example dataset (fingerPori comic):
- Run fingerporiScraper.py
  - Accept cookies manually (For some reason Selenium can't find the button via XPath or CSS selectors?)
  - Wait for browser to close
- Run downloadImages.py
- Run splitAllStrips.py to separate the strips in imageSet into individual frames in sourceSet


### Image to text
- Install gcloud CLI https://cloud.google.com/sdk/docs/install
- Set up auth in gcloud: `gcloud auth application-default login`

`pip install google-cloud-vision pandas`
- run ocrGCV.py to create computerVision.csv, text data from the images in frameSet/ using Google Computer Vision API

### Running model
`pip install transformers torch scikit-learn`

Once you have your frameSet & computerVision.csv set up, follow `Generator.pynb`, changing the input-variable

# TODO
- [ ] Improve runtime of splitStrip.py
- [ ] Improve splitStrip.py to better handle gutters with text on them (numbers, etc)
- [ ] OCR text data cleanup
- [ ] Separating different speech bubbles in OCR of 1 frame
- [ ] Generative AI descriptions of frame (with object detection/labeling via Google Cloud CV?) as features
- [ ] Method to decide frame output order rather than top 3 best matches (original placement # as feature?)
- [ ] CLI tool for user input
- [ ] Interactive GUI
- [ ] Web application