import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType



def test_windows():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle

    click_here = driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']")
    click_here.click()

    window_handles = driver.window_handles

    for handle in window_handles:
        if handle != parent_window:
            driver.switch_to.window(handle)
            break

    allure.attach(driver.get_screenshot_as_png(), name="New_Window", attachment_type=AttachmentType.PNG)

    driver.quit()
