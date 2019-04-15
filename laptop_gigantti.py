from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

url= "https://www.gigantti.fi/catalog/tietokoneet/fi_kannettavat/kannettavat-tietokoneet"

browser = webdriver.Chrome()

# Tell Selenium to go to url
browser.get(url)

page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
match = False
while (match == False):
    lastCount = page_length
    time.sleep(3) #wait till new products to  be loaded for 3 seconds
    page_length = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
    #when page is not scrollerable anymore

    if lastCount == page_length:
        match = True #stops scrolling

source_data = browser.page_source

with open("gigantti_laptop.html", "w") as file:
    file.write(source_data)

print("Done!")
