from selenium.webdriver.common.by import By


class OverviewPage:

    def __init__(self, driver):
        self._driver = driver

    def get_price(self):
        return self._driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label').text
