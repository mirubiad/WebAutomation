import time

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


def test_search():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://www.makemytrip.com/")

    wait = WebDriverWait(driver, timeout=10)
    actions = ActionChains(driver)

    #close the popup window
    try:
        close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']")))
        close_modal.click()
    except:
        print("No modal found, continuing...")

    # Select one way trip
    one_way = driver.find_element(By.XPATH, "//li[@data-cy='oneWayTrip']")
    one_way.click()

    # locate from city and enter desired city
    from_city = driver.find_element(By.XPATH, "//input[@data-cy='fromCity']")
    from_city.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-cy='fromCity']")))
    actions.send_keys("Mumbai").pause(2).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    # locate to city and enter desired city
    to_city = driver.find_element(By.XPATH, "//input[@data-cy='toCity']")
    to_city.click()
    actions.send_keys("Pune").pause(2).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    # Wait until picker is displayed
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class ='DayPicker-Day']")))

    # Select any date
    pick_a_date = driver.find_element(By.XPATH, "//div[@aria-label='Sun Feb 02 2025']")
    pick_a_date.click()


    # Click on search button
    search_button = driver.find_element(By.XPATH, "//p[@data-cy='submit']")
    actions.move_to_element(to_element=search_button).click().perform()

    # Verify that flights list page is loaded
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    wait.until(EC.url_contains("flight/search"))

    # Verify if the current URL contains "flight/search"
    current_url = driver.current_url
    assert "flight/search" in current_url, f"Expected 'flight/search' in URL, but got {current_url}"

    # Take a screenshot
    allure.attach(driver.get_screenshot_as_png(), name="flight_list_page", attachment_type=AttachmentType.PNG)

    driver.quit()