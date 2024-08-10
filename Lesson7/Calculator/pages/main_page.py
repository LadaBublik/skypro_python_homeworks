from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def calculator_waits(self):
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys("45")

    def sum(self):
        self._driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="="]').click()
        waiter = WebDriverWait(self._driver, 46)
        waiter.until(EC.text_to_be_present_in_element(
            (By.XPATH, '//div[text()="15"]'), "15"))
