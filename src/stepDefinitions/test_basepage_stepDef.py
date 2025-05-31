from pytest_bdd import given, when, then, scenarios, scenario

scenarios("../features/basepage.feature")

@given("This is the first step")
def verify_first_step():
    print("This seems to be the first step")
    pass

@when("User performs second step")
def verify_second_step():
    print("Second step also completed")
    pass

@then("Expected Result will display")
def verify_expected_result():
    print("Expected result")
    pass