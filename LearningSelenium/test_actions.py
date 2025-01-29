import pytest
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys

def test_allcaps_firstname():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")

    firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")

    actions = ActionChains(driver)
    #actions.move_to_element(firstname).key_down(Keys.SHIFT).send_keys("ubaid").key_up(Keys.SHIFT).perform()
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname, "ubaid").key_up(Keys.SHIFT).perform()



    driver.quit()


