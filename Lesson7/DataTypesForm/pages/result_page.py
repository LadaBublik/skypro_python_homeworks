from selenium.webdriver.common.by import By


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    def red_field(self):
        return self._driver.find_element(
            By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")

    def green_fields(self):
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
            return self._driver.find_element(By.CSS_SELECTOR, green
                                             ).value_of_css_property("color")
