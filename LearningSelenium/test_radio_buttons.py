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


def test_radio_buttons():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")

    radio_button = driver.find_element(By.XPATH, "//input[@id='sex-0']")  # Select the Gender
    radio_button.click()

    # Select the YOE
    years_of_experience = driver.find_elements(By.NAME, "exp")

    #Select the value by index
    # years_of_experience[3].click()

    # Verify it's selected
    # assert years_of_experience[3].is_selected()

    # Value you want to select
    select_YOE = "exp-3"

    # Loop through the radio buttons and select the one with the desired value
    for year in years_of_experience:
        if year.get_attribute("id") == select_YOE:
            year.click()
            break

    driver.quit()