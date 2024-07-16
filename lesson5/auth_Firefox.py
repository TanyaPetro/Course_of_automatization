from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
login_box = driver.find_element(By.ID, "username")
pwd_box = driver.find_element(By.ID, "password")
auth_button = driver.find_element(
    By.XPATH, "//button[contains(@class, 'radius')]"
    )
sleep(2)
login_box.send_keys("tomsmith")
sleep(1)
pwd_box.send_keys("SuperSecretPassword!")
sleep(2)
auth_button.click()
sleep(2)

driver.quit()
