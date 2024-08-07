from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def login(self):

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'user-name')]"
            ).send_keys('standard_user')

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'password')]"
            ).send_keys('secret_sauce')

        self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'login-button')]"
            ).click()

    def add_to_cart(self):
        show = WebDriverWait(self.driver, 30)
        show.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack"))
            ).click()

        self.driver.find_element(
            By.XPATH,
            "//button[contains(@id, 'add-to-cart-sauce-labs-bolt-t-shirt')]"
            ).click()

        self.driver.find_element(
            By.XPATH,
            "//button[contains(@id, 'add-to-cart-sauce-labs-onesie')]"
            ).click()

        self.driver.find_element(
            By.XPATH,
            "//a[contains(@class, 'shopping_cart_link')]"
            ).click()
