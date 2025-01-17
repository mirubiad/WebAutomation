import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType



@allure.title("Verify dropdown selection")
@allure.description("In appointment selection section verify that user is able to select options from dropdown")
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

    #Located the dropdown and select any option from dropdown
    dropdown_element = driver.find_element(By.XPATH, "//select[@id='combo_facility']")
    select_from_dropdown = Select(dropdown_element)

    #Slect 2nd option
    select_from_dropdown.select_by_value("Hongkong CURA Healthcare Center")
    allure.attach(driver.get_screenshot_as_png(),name="Appointment page", attachment_type=AttachmentType.PNG)

    #Slect 3rd Option
    select_from_dropdown.select_by_index(2)
    allure.attach(driver.get_screenshot_as_png(), name="Appointment page", attachment_type=AttachmentType.PNG)

    #Select 1st option
    select_from_dropdown.select_by_visible_text("Tokyo CURA Healthcare Center")
    allure.attach(driver.get_screenshot_as_png(), name="Appointment page", attachment_type=AttachmentType.PNG)

    driver.quit()

