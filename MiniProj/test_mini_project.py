import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@allure.title("Verify Expired msg is displayed for a user whose trail has expired")
@allure.description("Login to idrive360 and verify Expired msg is displayed")
def test_expired_msg():
    # Initialize the Edge WebDriver
    driver = webdriver.Edge()
    # Navigate to the login page
    driver.get("https://www.idrive360.com/enterprise/login")

    WebDriverWait(driver=driver, timeout=10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    email_web_element = driver.find_element(By.ID, "username")
    email_web_element.send_keys("augtest_040823@idrive.com")

    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys("123456")

    sign_in_button = driver.find_element(By.ID, "frm-btn")
    sign_in_button.click()

    WebDriverWait(driver=driver, timeout=30).until(
        EC.visibility_of_element_located((By.ID, "expiredmsg"))
    )

    allure.attach(driver.get_screenshot_as_png(), name="Expired_msg", attachment_type=AttachmentType.PNG)

    expired_msg = driver.find_element(By.ID, "expiredmsg")
    assert expired_msg.is_displayed()

    driver.quit()
