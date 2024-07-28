from selenium import webdriver
from form_page import FormPage


def test_form_fill():
    driver = webdriver.Chrome()
    formPage = FormPage(driver)
    formPage.open()
    formPage.fill_form()

    zip_color = formPage.get_zip_color()
    assert zip_color == 'rgba(132, 32, 41, 1)'

    colors = formPage.get_success_elems_color()
    for elem in colors:
        assert elem == 'rgba(15, 81, 50, 1)'
    driver.quit()
