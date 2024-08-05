from selenium import webdriver
from login_page import LoginPage
from cart_page import CartPage


def test_buy():
    driver = webdriver.Chrome()
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login()
    loginPage.add_to_cart()
    cartPage = CartPage(driver)
    cartPage.checkout()
    cartPage.fill()
    total = cartPage.get_total()
    driver.quit()
    assert total == 'Total: $58.29'
