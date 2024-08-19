import allure
from selenium import webdriver
from calc_page import CalcPage


@allure.title("Сложение чисел на калькуляторе")
@allure.description("Тест работы калькулятора")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_calc():
    with allure.step("Открытие страницы в Chrome"):
        driver = webdriver.Chrome()
        calcPage = CalcPage(driver)
        calcPage.open()
    with allure.step("Выполнение скрипта"):
        result = calcPage.do_calc()
    with allure.step("Проверка результата"):
        assert result == '15'
    driver.quit()
