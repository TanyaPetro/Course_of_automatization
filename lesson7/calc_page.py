from time import sleep
from selenium.webdriver.common.by import By


class CalcPage:
    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def do_calc(self):
        timer = '45'
        delay = self.driver.find_element(
            By.XPATH, "//input[contains(@id, 'delay')]"
            )
        delay.clear()
        delay.send_keys(timer)

        self.driver.find_element(
            By.XPATH, "//span[text()='7']"
            ).click()

        self.driver.find_element(
            By.XPATH, "//span[text()='+']"
            ).click()

        self.driver.find_element(
            By.XPATH, "//span[text()='8']"
            ).click()

        self.driver.find_element(
            By.XPATH, "//span[text()='=']"
            ).click()

        sleep(int(timer))

        result = self.driver.find_element(
            By.XPATH, "//div[contains(@class, 'screen')]"
        ).text

        return result
