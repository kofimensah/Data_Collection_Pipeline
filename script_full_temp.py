from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# method to access website
def website_pointer(url):
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(2)
    return driver

#method to by-pass cookies
def accept_all_cookies(driver, text):
    try:
        cookies_button = driver.find_element(By.XPATH, f'//button[text()="{str(text)}"]')
        cookies_button.click()
    except:
        pass

driver = website_pointer('https://www.formula1.com/')
accept_all_cookies(driver, "Accept All")



# method to navigate to desired pages - by link or by click
driver.find_elements(By.XPATH, f"//span[text()='Teams']").click()

#for team in teams_page:
#    print(team.find_element(by=By.XPATH, value=".//d[@class='css-1w7anck e1h9td4l31']").text)


#method to deal with pop-ups
alert = driver.switch_to.alert

#close driver
driver.close()
