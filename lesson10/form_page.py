from selenium.webdriver.common.by import By
import allure


class FormPage:
    url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'

    def __init__(self, driver: object):
        self.driver = driver

    with allure.step("Открытые страницы"):
        def open(self):
            self.driver.get(self.url)

    with allure.step("Заполнение формы"):
        def fill_form(self):
            first_name = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'first-name')]"
                )
            first_name.send_keys("Иван")

            last_name = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'last-name')]"
                )
            last_name.send_keys("Петров")

            address = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'address')]"
                )
            address.send_keys("Ленина, 55-3")

            email = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'e-mail')]"
                )
            email.send_keys("test@skypro.com")

            phone = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'phone')]"
                )
            phone.send_keys("+7985899998787")

            city = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'city')]"
                )
            city.send_keys("Москва")

            country = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'country')]"
                )
            country.send_keys("Россия")

            position = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'job-position')]"
                )
            position.send_keys("QA")

            company = self.driver.find_element(
                By.XPATH, "//input[contains(@name, 'company')]"
                )
            company.send_keys("SkyPro")

            self.driver.find_element(
                By.XPATH, "//button[contains(@class, 'btn')]"
                ).click()

    with allure.step("Получение цвета поля zip-code"):
        def get_zip_color(self) -> str:
            zip_color = (self.driver.find_element(
                By.XPATH, "//div[contains(@id, 'zip-code')]"
                ).value_of_css_property("color"))
            return zip_color

    with allure.step("Получение цветов корректно заполненных полей"):
        def get_success_elems_color(self) -> list:
            colors = []
            success_elements = self.driver.find_elements(
                By.XPATH, "//div[contains(@class, 'alert-success')]"
                )
            for elem in success_elements:
                colors.append(elem.value_of_css_property("color"))
            return colors
