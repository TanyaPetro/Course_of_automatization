from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/inputs")
input_box = driver.find_element(By.TAG_NAME, "input")
sleep(2)
input_box.send_keys("1000")
sleep(2)
input_box.clear()
sleep(2)
input_box.send_keys("999")
sleep(2)

driver.quit()
