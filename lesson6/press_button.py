from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "http://uitestingplayground.com/ajax"
    )

show = WebDriverWait(driver, 30)

show.until(EC.element_to_be_clickable((By.ID, "ajaxButton"))).click()

print(
    show.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    ).text
    )

driver.quit()
