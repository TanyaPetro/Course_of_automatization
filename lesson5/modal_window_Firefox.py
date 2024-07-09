from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")
show = WebDriverWait(driver, 10)
modal_window = show.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal"))
    )
close_button = driver.find_element(
    By.XPATH, "//div[contains(@class, 'modal-footer')]"
    )
sleep(2)
close_button.click()

sleep(2)
driver.quit()
