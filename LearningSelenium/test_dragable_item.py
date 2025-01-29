import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_dragable_item():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # draggable
    source_element = driver.find_element(By.ID, "draggable")

    #droppable
    target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

    # Create an ActionChains object
    actions = ActionChains(driver)

    #drag and drop by hold and release
    #actions.click_and_hold(on_element=source_element).move_to_element(to_element=target_element).release().perform()

    #Another way is by using drag and drop
    actions.drag_and_drop(source_element, target_element)

    driver.quit()