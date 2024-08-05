from selenium import webdriver
from calc_page import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    calcPage = CalcPage(driver)
    calcPage.open()
    result = calcPage.do_calc()
    assert result == '15'
    driver.quit()
