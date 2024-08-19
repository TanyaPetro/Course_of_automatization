from selenium import webdriver
from form_page import FormPage
import allure


@allure.title("Заполнение формы")
@allure.description("Проверка подсветки при вводе данных")
@allure.feature("CREATE")
@allure.severity("normal")
def test_form_fill():
    with allure.step("Открытие страницы в Chrome"):
        driver = webdriver.Chrome()
        formPage = FormPage(driver)
        formPage.open()
    with allure.step("Заполнение формы"):
        formPage.fill_form()

    with allure.step("Проверка цвета поля zip-code"):
        zip_color = formPage.get_zip_color()
        assert zip_color == 'rgba(132, 32, 41, 1)'

    with allure.step("Проверка цвета корректно заполненных полей"):
        colors = formPage.get_success_elems_color()
        for elem in colors:
            assert elem == 'rgba(15, 81, 50, 1)'

    with allure.step("Закрытие окна"):
        driver.quit()
