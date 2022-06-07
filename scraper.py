from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class Scraper:

    def __init__(self, url):
        self.url = url

    
    def connect_2_webpage(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
    
    def next_page(self, page_number):
        # locate button id=page_number
        # click button
        'to be defined'
        pass

    def clear_cookies(self, id):
        # search for cookies element on page
        # get cookies element
        # search for button with id
        # click to accept all cookies
        pass

    def get_container_data(self):
        pass

    def search(self, driver, search_item='London'):
        '''
        Function for searching in a search field on a webpage.
        '''
        elem = driver.find_element(By.NAME,"typeAheadInputField")
        elem.clear()    # Clear the search field
        elem.send_keys(search_item)     #type search_item='London' in the search field
        elem.send_keys(Keys.RETURN)     #Click enter in the search field

  