from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def checkout(self):
        show = WebDriverWait(self.driver, 30)
        show.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()

    def fill(self):
        show = WebDriverWait(self.driver, 30)
        show.until(
            EC.element_to_be_clickable((By.ID, "first-name"))
            ).send_keys("Test_1")

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'last-name')]"
            ).send_keys("Test_2")

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'postal-code')]"
            ).send_keys("Test_3")

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'continue')]"
            ).click()

    def get_total(self):
        show = WebDriverWait(self.driver, 30)
        total = show.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
            ).text
        return total
