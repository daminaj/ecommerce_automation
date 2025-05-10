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
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

class ProductPage:
    # Fixed locators - using tuples consistently
    quantity_input = (By.XPATH, "//input[@class='cart-quantity-input']")
    update_button = (By.XPATH, "//input[contains(@value, 'Update')]")
    unit_price_element = (By.XPATH, "//span[@class='cart-price cart-column']")
    total_price_element = (By.XPATH, "//span[@class='cart-total-price']")
    check_out_button = (By.XPATH, "//button[@class='btn btn-primary btn-purchase']")
    phone_field = (By.XPATH, "//input[@name='phone']")
    street_address_input = (By.XPATH, "//input[@name='street']")
    city_input = (By.XPATH, "//input[@name='city']")
    country_dropdown_input = (By.XPATH, "//select[@id='countries_dropdown_menu']")
    submit_order_button = (By.XPATH, "//button[@id='submitOrderBtn']")
    success_amount = (By.XPATH, "//*[@id='message']/b[1]")



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
        try:
            # Wait for the quantity field to be available
            qty_field = self.wait.until(EC.element_to_be_clickable(self.quantity_input))
            qty_field.clear()

            actions = ActionChains(self.driver)
            actions.click(qty_field)
            actions.send_keys(Keys.BACK_SPACE)
            actions.send_keys(str(quantity))
            actions.send_keys(Keys.ENTER)
            actions.perform()

            # Wait for the page to process the change
            self.wait.until(lambda driver: self._is_total_updated(quantity))
        except Exception as e:
            raise Exception(f"Failed to update quantity using Enter key: {str(e)}")

    def _is_total_updated(self, quantity):
        """Helper method to verify total price updates after quantity change"""
        try:
            total_element = self.driver.find_element(*self.total_price_element)
            total_text = total_element.text.replace('$', '').replace(',', '')
            unit_price = self.get_unit_price()
            expected_total = unit_price * quantity
            return abs(float(total_text) - expected_total) < 0.01
        except:
            return False

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

    def checkout(self):
        try:
            # Proceed to checkout
            checkout_button = self.wait.until(EC.element_to_be_clickable(self.check_out_button))
            checkout_button.click()
        except (TimeoutException, ElementClickInterceptedException) as e:
            raise Exception(f"Failed to click checkout button: {str(e)}")

    def input_phone(self, number):
        try:
            phone_input = self.wait.until(EC.element_to_be_clickable(self.phone_field))
            phone_input.clear()
            phone_input.send_keys(number)
        except Exception as e:
            raise Exception(f"Failed to input phone number: {str(e)}")

    def input_street_add(self, address):
        try:
            street_input = self.wait.until(EC.element_to_be_clickable(self.street_address_input))
            street_input.clear()
            street_input.send_keys(address)
        except Exception as e:
            raise Exception(f"Failed to input street address: {str(e)}")

    def input_city(self, city):
        try:
            city_field = self.wait.until(EC.element_to_be_clickable(self.city_input))
            city_field.clear()
            city_field.send_keys(city)
        except Exception as e:
            raise Exception(f"Failed to input city: {str(e)}")

    def select_country_by_xpath(self, country_name):
        """
        Selects a country from the dropdown by directly clicking the option
        """
        try:
            # First click the dropdown to open it
            dropdown = self.wait.until(EC.element_to_be_clickable(self.country_dropdown_input))
            dropdown.click()

            # Wait for options to be visible and click the desired one
            xpath = f"//select[@id='countries_dropdown_menu']/option[text()='{country_name}']"
            option = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            option.click()
        except Exception as e:
            raise Exception(f"Failed to select country '{country_name}': {str(e)}")

    def submit_order(self):
        try:
            submit_button = self.wait.until(EC.element_to_be_clickable(self.submit_order_button))
            submit_button.click()

            # Wait for success page to load
            self.wait.until(EC.visibility_of_element_located(self.success_amount))
        except Exception as e:
            raise Exception(f"Failed to submit order: {str(e)}")

    def get_order_amount_on_success_page(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.success_amount))
        except TimeoutException as e:
            raise Exception(f"Could not retrieve success amount: {str(e)}")


