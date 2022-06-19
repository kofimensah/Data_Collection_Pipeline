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
        sleep(2)
        return driver

    def next_page(self, page_number):
        next_page = driver.find_element(By.XPATH, f'//button')
        # locate button id=page_number
        # click button
        'to be defined'
        pass

    #method to accept all cookies by accepting the text on the button as an argument
    def accept_all_cookies(self, button_text):
        try:
            cookies_button = driver.find_element(By.XPATH, f'//button[text()="{str(button_text)}"]')
            cookies_button.click()
        except:
            pass

    def get_container_data(self):
        driver = webdriver.Chrome()
        driver.get("https://www.zoopla.co.uk/for-sale/property/london/?q=London&results_sort=newest_listings&search_source=home")
        houses_container = driver.find_elements(by=By.XPATH, value="//div[@class='css-1itfubx e1c4dna40']//div[@class='e1c4dna41 css-dhlvpc e1h9td4l19']")
        for house in houses_container:
            print(house.find_element(by=By.XPATH, value=".//p[@class='css-1w7anck e1h9td4l31']").text)


    def search(self, driver, search_item='London'):
        '''
        Function for searching in a search field on a webpage.
        '''
        elem = driver.find_element(By.NAME,"typeAheadInputField")
        elem.clear()    # Clear the search field
        elem.send_keys(search_item)     #type search_item='London' in the search field
        elem.send_keys(Keys.RETURN)     #Click enter in the search field

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.zoopla.co.uk/for-sale/property/london/?q=London&results_sort=newest_listings&search_source=home")
houses_container = driver.find_elements(by=By.XPATH, value="//div[@class='css-1itfubx e1c4dna40']//div[@class='e1c4dna41 css-dhlvpc e1h9td4l19']")
for house in houses_container:
    print(house.find_element(by=By.XPATH, value=".//p[@class='css-1w7anck e1h9td4l31']").text)

