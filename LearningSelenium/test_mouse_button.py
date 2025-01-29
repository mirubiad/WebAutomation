from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_mouse_back():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    results_page = driver.find_element(By.XPATH, "//a[@id='click']")
    results_page.click()

    action_builders = ActionBuilder(driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    driver.quit()