from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.maximize_window()

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

first_name = driver.find_element(
    By.XPATH, "//input[contains(@name, 'first-name')]"
    )
first_name.send_keys("Иван")

last_name = driver.find_element(
    By.XPATH, "//input[contains(@name, 'last-name')]"
    )
last_name.send_keys("Петров")

address = driver.find_element(
    By.XPATH, "//input[contains(@name, 'address')]"
    )
address.send_keys("Ленина, 55-3")

email = driver.find_element(
    By.XPATH, "//input[contains(@name, 'e-mail')]"
    )
email.send_keys("test@skypro.com")

phone = driver.find_element(
    By.XPATH, "//input[contains(@name, 'phone')]"
    )
phone.send_keys("+7985899998787")

city = driver.find_element(
    By.XPATH, "//input[contains(@name, 'city')]"
    )
city.send_keys("Москва")

country = driver.find_element(
    By.XPATH, "//input[contains(@name, 'country')]"
    )
country.send_keys("Россия")

position = driver.find_element(
    By.XPATH, "//input[contains(@name, 'job-position')]"
    )
position.send_keys("QA")

company = driver.find_element(
    By.XPATH, "//input[contains(@name, 'company')]"
    )
company.send_keys("SkyPro")

driver.find_element(
    By.XPATH, "//button[contains(@class, 'btn')]"
    ).click()

zip_color = (driver.find_element(
    By.XPATH, "//div[contains(@id, 'zip-code')]"
    ).value_of_css_property("color"))
assert zip_color == 'rgba(132, 32, 41, 1)'

success_elements = driver.find_elements(
    By.XPATH, "//div[contains(@class, 'alert-success')]"
    )

for elem in success_elements:
    assert (elem.value_of_css_property("color")) == 'rgba(15, 81, 50, 1)'


driver.quit()
