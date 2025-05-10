# tests/test_login.py
from pageObjects.login_page import LoginPage
from utilities.read_conf import ReadConfig

def test_login_valid_user(setup_driver, test_data):
    driver = setup_driver
    base_url = ReadConfig.getApplicationURL()
    driver.get(base_url)
    page = LoginPage(driver)
    page.login(test_data["email"], test_data["password"])
    act_title = driver.title
    if act_title == "QA Practice | Learn with RV":
        assert True
        driver.close()
    else:
        driver.save_screenshot("./Screenshots/" + "test_homepagetitle.png")
        driver.close()
        assert False
