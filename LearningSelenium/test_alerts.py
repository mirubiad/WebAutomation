import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType

@pytest.fixture
def driver():
    get_driver = webdriver.Edge()
    get_driver.maximize_window()
    get_driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield get_driver  # Provide the driver instance to the test function
    get_driver.quit()


def test_normal_alert(driver):
    js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    js_alert.click()

    #Wait for alert to appear
    WebDriverWait(driver, timeout=5).until(
        EC.alert_is_present()
    )

    alert = driver.switch_to.alert  # Switch to the alert
    assert alert.text == "I am a JS Alert"
    alert.accept()  #Click Ok

    #Verify the result
    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert"


def test_confirmation_alert_accept(driver):
    confirm_alert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    confirm_alert.click()

    alert = driver.switch_to.alert #Swith to alert
    assert alert.text == "I am a JS Confirm"
    alert.accept()

    #Verify the result message
    result = driver.find_element(By.ID, "result")
    assert result.text == "You clicked: Ok"


def test_confirmation_alert_cancel(driver):
    confirm_alert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    confirm_alert.click()

    alert = driver.switch_to.alert #Swith to alert
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()

    #Verify the result message
    result = driver.find_element(By.ID, "result")
    assert result.text == "You clicked: Cancel"


def test_prompt_alert(driver):
    prompt_alert = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    prompt_alert.click()

    alert = driver.switch_to.alert #Switch to Prompt
    alert.send_keys("Hi, I am a prompt")
    alert.accept()
    #Verify the result
    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Hi, I am a prompt"






