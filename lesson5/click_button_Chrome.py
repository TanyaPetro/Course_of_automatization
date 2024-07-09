from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "http://the-internet.herokuapp.com/add_remove_elements/"
    )

button_add = driver.find_element(
    By.XPATH, "//button[text()='Add Element']"
    )

for _ in range(5):
    button_add.click()
    sleep(2)

delete_button = "button.added-manually"
button_list = driver.find_elements(By.CSS_SELECTOR, delete_button)

print("Размер списка Delete - ", len(button_list))

driver.quit()
