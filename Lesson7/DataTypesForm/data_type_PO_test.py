from selenium import webdriver
from DataTypesForm.pages.main_page import MainPage
from DataTypesForm.pages.result_page import ResultPage


def test_data_types_form():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.input_data()
    main_page.click_button_submit()

    result_page = ResultPage(driver)
    red = result_page.red_field()
    assert red == 'rgba(132, 32, 41, 1)'
    green = result_page.green_fields()
    assert green == 'rgba(15, 81, 50, 1)'
    driver.quit()
