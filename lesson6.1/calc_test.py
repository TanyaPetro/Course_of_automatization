from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

timer = '45'

delay = driver.find_element(
    By.XPATH, "//input[contains(@id, 'delay')]"
    )
delay.clear()
delay.send_keys(timer)

driver.find_element(
    By.XPATH, "//span[text()='7']"
    ).click()

driver.find_element(
    By.XPATH, "//span[text()='+']"
    ).click()

driver.find_element(
    By.XPATH, "//span[text()='8']"
    ).click()

driver.find_element(
    By.XPATH, "//span[text()='=']"
    ).click()

sleep(int(timer))

result = driver.find_element(
    By.XPATH, "//div[contains(@class, 'screen')]"
    ).text

assert result == '15'

driver.quit()
