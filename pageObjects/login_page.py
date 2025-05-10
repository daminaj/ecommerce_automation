# pages/login_page.py
from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage

class LoginPage(BasePage):
    SHOP_BTN = (By.XPATH, "//*[@id='auth-shop']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    LOGIN_BTN = (By.XPATH, "//button[@id='submitLoginBtn']")

    def login(self, email, password):
        self.click(self.SHOP_BTN)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.click(self.LOGIN_BTN)
