from selenium.webdriver.common.by import By
from data_shop import *


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def authorization(self):
        self._driver.find_element(By.ID, "user-name").send_keys(login)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()
