import time
import pytest
from pytest_bdd import given, when, then, scenarios, scenario

scenarios("../features/basepage.feature")

@given("This is the first step")
def verify_first_step():
    print("This seems to be the first step")
    pass

@when("User performs second step")
@pytest.mark.usefixtures("page")
def verify_second_step(page):
    print("Second step also completed")
    # Launch browser and navigate to Google
    page.goto("https://www.google.com")
    time.sleep(5)  # Wait for the page to load
    assert "Google" in page.title()

@then("Expected Result will display")
def verify_expected_result():
    print("Expected result")
    pass