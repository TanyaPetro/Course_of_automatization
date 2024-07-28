from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "http://uitestingplayground.com/textinput"
    )

show = WebDriverWait(driver, 10)

show.until(
    EC.element_to_be_clickable((By.TAG_NAME, "input"))
    ).send_keys("SkyPro")

show.until(EC.element_to_be_clickable((By.ID, "updatingButton"))).click()

new_button_text = show.until(
        EC.visibility_of_element_located((By.ID, "updatingButton"))
    ).text

print(new_button_text)

driver.quit()
