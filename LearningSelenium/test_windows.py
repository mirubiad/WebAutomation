import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


def test_windows():
    # Step 1: Launch the Edge browser
    driver = webdriver.Edge()
    driver.maximize_window()  # Maximize the browser window

    # Step 2: Navigate to the webpage
    driver.get("https://the-internet.herokuapp.com/windows")

    # Step 3: Store the parent (main) window handle
    parent_window = driver.current_window_handle

    # Step 4: Locate and click the "Click Here" link to open a new window
    click_here = driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']")
    click_here.click()

    # Step 5: Get all open window handles (IDs of all browser tabs/windows)
    window_handles = driver.window_handles

    # Step 6: Loop through all window handles
    for handle in window_handles:
        if handle != parent_window:  # Find the newly opened window
            driver.switch_to.window(handle)  # Switch to the new window
            break  # Exit the loop once switched

    # Step 7: Take a screenshot of the new window for reporting
    allure.attach(driver.get_screenshot_as_png(), name="New_Window", attachment_type=AttachmentType.PNG)

    # Step 8: Close the browser and end the session
    driver.quit()
