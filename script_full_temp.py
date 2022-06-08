'''
this will serve as my test center where i will put the full code without any classes.

Eventually, I will use this space to test the class

Target: F1 team -> standings -> merch
'''

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# method to access website
driver = webdriver.Chrome()
url = 'https://www.formula1.com/'
driver.get(url)

# method to navigate to desired pages - by link or by click
teams_page = driver.find_elements(by=By.XPATH, value="//div[@class='css-1itfubx e1c4dna40']//div[@class='e1c4dna41 css-dhlvpc e1h9td4l19']")
for house in houses_container:
    print(house.find_element(by=By.XPATH, value=".//p[@class='css-1w7anck e1h9td4l31']").text)

# method to deal with pop-ups

