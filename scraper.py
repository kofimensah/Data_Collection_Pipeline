from selenium import webdriver
from time import sleep

class Scraper:

    def __init__(self, url):
        self.url = url

    
    def connect_2_webpage(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        