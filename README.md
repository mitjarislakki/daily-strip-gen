
### Dataset processing:
`pip install pandas selenium beautifulsoup4 requests pillow --user`
- Run fingerporiScraper.py
  - Accept cookies manually (For some reason Selenium can't find the button via XPath or CSS selectors?)
  - Wait for browser to close
- Run downloadImages.py
- Run splitAllStrips


### Image to text
TODO

### Text similarity
`pip install scikit-learn --user`
- run textSimilarity.py 