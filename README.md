`python -m venv stripgen`

### Dataset processing:
`pip install pandas selenium beautifulsoup4 requests pillow --user`
- Run fingerporiScraper.py
  - Accept cookies manually (For some reason Selenium can't find the button via XPath or CSS selectors?)
  - Wait for browser to close
- Run downloadImages.py
- Run splitAllStrips


### Image to text
- Install tesseract with Finnish language data https://tesseract-ocr.github.io/tessdoc/Installation.html
`pip install opencv-python pytesseract`

- Install gcloud CLI https://cloud.google.com/sdk/docs/install
- Set up auth in gcloud: `gcloud auth application-default login`

`pip install google-cloud-vision`

### Text similarity
`pip install scikit-learn --user`
- run textSimilarity.py 

### Display
`pip install matplotlib`