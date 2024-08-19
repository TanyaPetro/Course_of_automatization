from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver: object):
        self.driver = driver

    with allure.step("Открытие страницы в Chrome"):
        def open(self):
            self.driver.get(self.url)

    with allure.step("Чекаут"):
        def checkout(self):
            show = WebDriverWait(self.driver, 30)
            show.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
                ).click()

    with allure.step("Ввод данных для отправки"):
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

    with allure.step("Получение итоговой суммы в корзине"):
        def get_total(self) -> str:
            show = WebDriverWait(self.driver, 30)
            total = show.until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "summary_total_label"))
                ).text
            return total
