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
    assert "danger" in driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "first-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "last-name").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "address").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "city").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "country").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "e-mail").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "phone").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "job-position").get_attribute("class")
    assert "success" in driver.find_element(
        By.ID, "company").get_attribute("class")
    driver.quit()
