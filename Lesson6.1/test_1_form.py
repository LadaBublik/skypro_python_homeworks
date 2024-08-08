from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_data_form():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR,
                        "input[name='company']").send_keys("SkyPro")
    
    waiter = WebDriverWait(driver, 15)
    waiter.until(EC.element_to_be_clickable(
        (By.TAG_NAME, "button")))
        
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    red_form = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
    assert red_form == 'rgba(132, 32, 41, 1)' 
    locators = [
        "#first-name",
        "#last-name",
        "#address",
        "#city",
        "#country",
        "#e-mail",
        "#phone",
        "#job-position",
        "#company"
    ]
    for green in locators:
        green_forms = driver.find_element(By.CSS_SELECTOR, green).value_of_css_property("color")
        assert green_forms == 'rgba(15, 81, 50, 1)'
    driver.quit()
