from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

show = WebDriverWait(driver, 30)

show.until(EC.visibility_of_element_located((By.ID, "landscape")))

print(driver.find_element(By.ID, "award").get_attribute("src"))

driver.quit()
