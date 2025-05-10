# conftest.py
import pytest
from utilities.driver_factory import get_driver
from data.test_data import login_data

@pytest.fixture
def setup_driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def test_data():
    return login_data


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        print("\n===== Test Output =====")

        # Print any captured output if available
        if hasattr(report, "caplog"):
            print(report.caplog)
        if hasattr(report, "capstdout"):
            print(report.capstdout)

    return report

