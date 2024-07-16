from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(
    By.XPATH, "//button[text()='Button with Dynamic ID']"
    )

blue_button.click()

for i in range(3):
    blue_button.click()
    print(i+1)
    sleep(2)

sleep(2)
driver.quit()
