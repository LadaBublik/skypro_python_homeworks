from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self._driver = driver

    def input_data(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Ivan")
        self._driver.find_element(By.ID, "last-name").send_keys("Ivanov")
        self._driver.find_element(By.ID, "postal-code").send_keys("629002")
        self._driver.find_element(By.ID, "continue").click()
