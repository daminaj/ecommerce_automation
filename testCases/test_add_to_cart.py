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

    # Get and validate prices
    unit_price = product_page.get_unit_price()
    expected_total = unit_price * quantity
    displayed_total = product_page.get_total_price()

    print(f"Unit Price: ${unit_price}")
    print(f"Expected Total: ${expected_total}")
    print(f"Displayed Total: {displayed_total}")

    # Optional: Add assertion to verify totals match
    assert abs(expected_total - float(displayed_total.replace('$', ''))) < 0.01