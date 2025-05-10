import time

# from pageObjects.login_page import LoginPage
# from utilities.read_conf import ReadConfig
# from pageObjects.product_page import ProductPage
#
#
# def test_add_multiple_items(setup_driver, test_data):
#     driver = setup_driver
#     base_url = ReadConfig.getApplicationURL()
#     driver.get(base_url)
#     page = LoginPage(driver)
#     page.login(test_data["email"], test_data["password"])
#
#     product_page = ProductPage(driver)
#     # add product to cart
#     product_page.add_to_cart_by_name("Apple iPhone 12, 128GB, Black")
#     # product_page.add_to_cart_by_name("Samsung Galaxy A32, 128GB, White")
#
#     # Define quantity to test
#     # quantity = 3
#     # product_page.update_quantity(quantity)
#
#     quantity = 3
#     product_page.input_quantity_with_enter(quantity)
#
#
#
#     # unit_price_1 = product_page.get_unit_price()
#     # expected_total_1 = unit_price_1 * quantity
#     displayed_total_1 = product_page.get_total_price()
#     print(f"{displayed_total_1}")
    #
    # if round(expected_total_1) == round(displayed_total_1):
    #     print(" First item: Total price is correct.")
    # else:
    #     print(f" First item: Total incorrect. Expected: {expected_total_1}, Displayed: {displayed_total_1}")

    # --- Step 2: Reset quantity to 1 ---
    # product_page.input_quantity_with_enter(1)

    # Calculate expected and get actual total
    # expected_total = product_page.calculate_expected_total(quantity)
    # ProductPage.update_quantity(driver, new_quantity)
    # actual_total = product_page.get_displayed_total

    # Use if-statement for result check
    # if abs(expected_total == actual_total):
    #     print("✅ The total price displayed is correctly calculated.")
    # else:
    #     print("❌ The total price displayed is not correct.")
    #     print(f"Expected: ${expected_total}, Got: ${actual_total}")


from pageObjects.login_page import LoginPage
from utilities.read_conf import ReadConfig
from pageObjects.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_add_multiple_items(setup_driver, test_data):
    driver = setup_driver
    base_url = ReadConfig.getApplicationURL()
    driver.get(base_url)
    page = LoginPage(driver)
    page.login(test_data["email"], test_data["password"])

    product_page = ProductPage(driver)
    # add product to cart
    product_page.add_to_cart_by_name("Apple iPhone 12, 128GB, Black")
    # product_page.add_to_cart_by_name("Samsung Galaxy A32, 128GB, White")

    # Define quantity to test
    quantity = 3
    product_page.input_quantity_with_enter(quantity)

    try:
        # Update the quantity
        product_page.input_quantity_with_enter(quantity)

        # Get and validate prices
        unit_price = product_page.get_unit_price()
        expected_total = unit_price * quantity
        displayed_total = product_page.get_total_price()

        print(f"Unit Price: ${unit_price}")
        print(f"Expected Total: ${expected_total}")
        print(f"Displayed Total: {displayed_total}")

        # Assertion to verify totals match (allowing for small floating-point differences)
        assert abs(expected_total - float(displayed_total.replace('$', ''))) < 0.01

        # Proceed to checkout - corrected method name
        product_page.checkout()

        # Fill checkout form
        country = "Albania"
        number = "08160006355"
        street = "2, ajobiowe ajangbadi street"
        city = "Sokka"

        # Input form details
        product_page.input_phone(number)
        product_page.input_street_add(street)
        product_page.input_city(city)
        product_page.select_country_by_xpath(country)

        # Submit order
        product_page.submit_order()

        # Verify success message/amount after order submission
        success_amount_element = product_page.get_order_amount_on_success_page()
        success_amount_text = success_amount_element.text

        print(f"Order confirmed with amount: {success_amount_text}")

        # Verify the order amount matches expected total
        order_amount = float(success_amount_text.replace('$', '').strip())
        assert abs(expected_total - order_amount) < 0.01

    except Exception as e:
        # Take screenshot on failure
        driver.save_screenshot(f"test_add_order_failure_{driver.name}.png")
        pytest.fail(f"Test failed with error: {str(e)}")