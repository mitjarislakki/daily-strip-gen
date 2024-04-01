import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://www.hs.fi/fingerpori/")
results = []
count = 0

def parse_image_urls(classes, location, source):
    for a in soup.findAll(attrs={'class': classes}):
        name = a.find(location)
        if name not in results:
            result = name.get(source)
            if result is not None: results.append(f'https:{result[:-6]}') # Drop last 6 chars

def recursivePress():
    try:
        element = driver.find_element(By.XPATH, "//a[@class='is-more-items-link lazyload']")
        driver.execute_script("arguments[0].scrollIntoView(false);", element)
        driver.execute_script("arguments[0].click();", element)
        global count
        count += 1
        print(count)
        if count == 60: return
        time.sleep(0.5)
        return recursivePress()
    except NoSuchElementException:
        return

# driver.find_element(By.XPATH, "//button[@title='OK']").click()
time.sleep(5)  
# driver.find_element(By.CSS_SELECTOR, "button[title='OK']").click()


recursivePress()

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

driver.quit()

parse_image_urls("cartoon image scroller", "img", "srcset")


df = pd.DataFrame({"links": results})
df.to_csv("links.csv", index=False, encoding="utf-8")