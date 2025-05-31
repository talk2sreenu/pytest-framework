import json
import pytest
from pytest_bdd import given, then, parsers, step


@given(parsers.parse("I have a bar"))
@given(parsers.parse("This is something"))
def given_step():
    print("This is from I have a bar")
    pass

@then(parsers.parse('bar should have value "bar"'))
@then(parsers.parse("This is nothing"))
def then_step():
    print("This is from then step")
    pass

"""def pytest_bdd_before_scenario(request):
    with open("testData/test_data.json", "r") as f:
        test_data = json.load(f)
    request.session.test_data = test_data"""

@given(parsers.parse('the test data is loaded from "{file_path}"'))
def load_test_data(file_path, request):
        with open("testData/"+file_path, "r") as f:
            #global test_data  # Make data accessible across scenarios
            test_data = json.load(f)
            request.session.test_data = test_data
