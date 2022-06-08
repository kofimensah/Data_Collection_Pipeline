'''
This my twitter scraper, where I will scrape my own twitter information to see how people interact and think
'''

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# method to access website
driver = webdriver.Chrome()
url = 'https://twitter.com/'
driver.get(url)

# method for cookies
delay = 10
try:
    WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, '')))
    print("Frame Ready!")
    driver.switch_to.frame('') # name of frame
except TimeoutException:
    print("loading timeout")


'''
        print("Frame Ready!")
        driver.switch_to.frame('gdpr-consent-notice')
        accept_cookies_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="save"]')))
        print("Accept Cookies Button Ready!")
        accept_cookies_button.click()
        time.sleep(1)
    except TimeoutException:
        print("Loading took too much time!")

'''    


# method to navigate to desired pages - by link or by click
teams_page = driver.find_elements(by=By.XPATH, value="//div[@class='css-1itfubx e1c4dna40']//div[@class='e1c4dna41 css-dhlvpc e1h9td4l19']")
for house in houses_container:
    print(house.find_element(by=By.XPATH, value=".//p[@class='css-1w7anck e1h9td4l31']").text)

# method to deal with pop-ups

