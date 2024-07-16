from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "http://uitestingplayground.com/classattr"
    )

blue_button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn-primary')]"
    )

blue_button.click()
driver.switch_to.alert.accept()
sleep(1)

for i in range(3):
    blue_button.click()
    print(i+1)
    sleep(2)
    driver.switch_to.alert.accept()

sleep(2)
driver.quit()
