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


@allure.title("Login to OrangeHrm, add a user and search the user")
@allure.description("Add a new user and Verify if the user is added successfully")
def test_add_new_user():
    driver = webdriver.Edge()

    #Navigate to the url
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #wait untill username field is displayed
    WebDriverWait(driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username' and @name='username']"))
    )

    #find usermane and password elements
    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username' and @name='username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

    #enter username and password
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")

    #click on login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, timeout=5).until(
        EC.url_contains("dashboard/index")
    )

    #verify that url is changing after login
    assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    #wait for the menu item to load
    WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']"))
    )

    #Goto admin menu
    admin_menu_item = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']")
    admin_menu_item.click()

    WebDriverWait(driver, timeout=5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add') and @type='button']"))
    )

    #click on add user button
    add_user_button = driver.find_element(By.XPATH, "//button[contains(., 'Add') and @type='button']")
    add_user_button.click()

    #wait until form loads
    WebDriverWait(driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Add User']"))
    )


    #find form elements and fill all fields
    user_role = driver.find_element(By.XPATH, "//div[contains(@class, 'oxd-select-text')]")


    driver.quit()


