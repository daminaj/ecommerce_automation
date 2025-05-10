# # pages/product_page.py
# import selenium
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class ProductPage:
#     quantity_input = "//input[@class='cart-quantity-input']"
#     update_button = (By.XPATH, "//input[contains(@value, 'Update')]")
#     unit_price_element = (By.XPATH, "//span[@class='cart-price cart-column']")
#     total_price_element = (By.XPATH, "//span[@class='cart-total-price']")
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def add_to_cart_by_name(self, exact_product_name):
#         xpath = f"//span[@class='shop-item-title' and normalize-space(text())='{exact_product_name}']/ancestor::div[contains(@class, 'shop-item')]//button[contains(text(), 'ADD TO CART')]"
#         self.driver.find_element(By.XPATH, xpath).click()
#
#
#     def get_unit_price(self):
#         price_text = self.driver.find_element(By.XPATH, self.unit_price_element)
#         return float(price_text.replace('$', '').replace(',', ''))
#
#     def input_quantity_with_enter(self, quantity):
#         qty_field = self.driver.find_element(By.XPATH, self.quantity_input)
#         qty_field.clear()
#
#         actions = ActionChains(self.driver)
#         actions.click(qty_field)
#         actions.send_keys(Keys.BACK_SPACE)
#         actions.send_keys(str(quantity))
#         actions.send_keys(Keys.ENTER)
#         actions.perform()
#
#     # def update_quantity(self, quantity):
#     #     # self.driver.find_element(By.XPATH, self.quantity_input).clear()
#     #     self.driver.find_element(By.XPATH, self.quantity_input).send_keys(quantity)
#     #     actions = ActionChains(self.driver)
#     #     quantity_field = self.driver.find_element(By.XPATH, self.quantity_input).clear()
#     #     # quantity_field = WebDriverWait(self.driver, 10).until(
#     #     #     EC.element_to_be_clickable(By.XPATH, self.quantity_input)
#     #     # )
#     #
#     #     actions.click(quantity_field) \
#     #         .key_down(Keys.CONTROL) \
#     #         .send_keys(Keys.DELETE) \
#     #         .key_up(Keys.CONTROL) \
#     #         .send_keys(str(quantity)) \
#     #         .send_keys(Keys.ENTER) \
#     #         .perform()
#     #
#     #     WebDriverWait(self.driver, 10).until(
#     #         EC.text_to_be_present_in_element(self.total_price_element, "")
#     #     )
#     #     # quantity_field = WebDriverWait(self.driver, 10).until(
#     #     #     EC.element_to_be_clickable(self.quantity_input)
#     #     # )
#     #     # quantity_field.clear()
#     #     # quantity_field.send_keys(quantity)
#     #     # # Wait for total to update
#     #     # WebDriverWait(self.driver, 10).until(
#     #     #     EC.text_to_be_present_in_element(self.total_price_element, "$")
#     #     # )
#
#     def get_total_price(self):
#         total_text = self.driver.find_element(By.XPATH, self.total_price_element).text
#         return total_text
        # return float(total_text.replace('$', '').replace(',', ''))



    # def get_displayed_total(self):
    #     total_text = WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located(self.total_price_element)
    #     ).text
    #     return float(total_text.replace('$', '').replace(',', ''))

    # def calculate_expected_total(self, quantity):
    #     return self.get_unit_price() * quantity





# pageObjects/product_page.py
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    # Fixed locators - using tuples consistently
    quantity_input = (By.XPATH, "//input[@class='cart-quantity-input']")
    update_button = (By.XPATH, "//input[contains(@value, 'Update')]")
    unit_price_element = (By.XPATH, "//span[@class='cart-price cart-column']")
    total_price_element = (By.XPATH, "//span[@class='cart-total-price']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart_by_name(self, exact_product_name):
        xpath = f"//span[@class='shop-item-title' and normalize-space(text())='{exact_product_name}']/ancestor::div[contains(@class, 'shop-item')]//button[contains(text(), 'ADD TO CART')]"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_unit_price(self):
        # Wait for the element to be visible
        price_element = self.wait.until(EC.visibility_of_element_located(self.unit_price_element))
        price_text = price_element.text
        # Remove currency symbol and commas, then convert to float
        return float(price_text.replace('$', '').replace(',', ''))

    def input_quantity_with_enter(self, quantity):
        # Wait for the quantity field to be available
        qty_field = self.wait.until(EC.element_to_be_clickable(self.quantity_input))
        qty_field.clear()

        actions = ActionChains(self.driver)
        actions.click(qty_field)
        actions.send_keys(Keys.BACK_SPACE)
        actions.send_keys(str(quantity))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def update_quantity(self, quantity):
        # Alternative method if input_quantity_with_enter doesn't work
        qty_field = self.wait.until(EC.element_to_be_clickable(self.quantity_input))
        qty_field.clear()
        qty_field.send_keys(str(quantity))
        update_button = self.wait.until(EC.element_to_be_clickable(self.update_button))
        update_button.click()

    def get_total_price(self):
        # Wait for the total price to be visible
        total_element = self.wait.until(EC.visibility_of_element_located(self.total_price_element))
        total_text = total_element.text
        return total_text
