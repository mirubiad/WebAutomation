import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@allure.title("Cura website login")
@allure.description("Login in to Cura and verify that 'Make Appointment' text is displayed")
def test_make_appointment_text():
    driver = webdriver.Edge()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appoint_button = driver.find_element(By.ID,"btn-make-appointment")
    make_appoint_button.click()

    #Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    WebDriverWait(driver=driver,timeout=3).until(
        EC.visibility_of_element_located((By.ID,"txt-username"))
    )

    username_field = driver.find_element(By.ID,"txt-username")
    password_field = driver.find_element(By.ID, "txt-password")

    username_field.send_keys("John Doe")
    password_field.send_keys("ThisIsNotAPassword")

    WebDriverWait(driver=driver,timeout=3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"#btn-login"))
    )

    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.url_contains("#appointment")
    )

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    make_appoint_text = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
    #assert make_appoint_text.is_displayed()
    assert make_appoint_text.text == "Make Appointment"

    allure.attach(driver.get_screenshot_as_png(),name="Appointment page", attachment_type=AttachmentType.PNG)

