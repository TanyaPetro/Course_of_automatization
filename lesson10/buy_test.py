from selenium import webdriver
from login_page import LoginPage
from cart_page import CartPage
import allure


@allure.title("Добавление товаров в корзину")
@allure.description("Проверка работы корзины")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_buy():
    with allure.step("Открытие страницы с логином"):
        driver = webdriver.Chrome()
        loginPage = LoginPage(driver)
        loginPage.open()

    with allure.step("Логин"):
        loginPage.login()

    with allure.step("Добавление товаров в корзину"):
        loginPage.add_to_cart()

    with allure.step("Переход на страницу корзины"):
        cartPage = CartPage(driver)

    with allure.step("Чекаут"):
        cartPage.checkout()
        cartPage.fill()

    with allure.step("Получение итоговой суммы в корзине"):
        total = cartPage.get_total()

    with allure.step("Закрытие страницы"):
        driver.quit()

    with allure.step("Проверка общей стоимости корзины"):
        assert total == 'Total: $58.29'
