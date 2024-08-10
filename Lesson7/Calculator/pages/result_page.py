from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def sum_result(self):
        return self._driver.find_element(
            By.XPATH, '//div[text()="15"]').text
