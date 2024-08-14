from selenium import webdriver
from pages.main_page import MainPage
from pages.result_page import ResultPage


def test_data_types_form():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    main_page.calculator_waits(45)
    main_page.sum("7", "8", "+", "=", "46", "15")

    result_page = ResultPage(driver)
    res = result_page.sum_result()
    assert res == "15"
    driver.quit()
