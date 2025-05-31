import json
import pytest
from pytest_bdd import scenarios, given, then, parsers


scenarios('./datadrivetests/parameterize.feature')

@pytest.fixture()
def jsonFile(request):
    return {'userName' : request.param.get("jsonFile"), 'password': 'pwd'}

@pytest.fixture
def get_test_data(request):
    print(request)
    file_path = '{"username": "Srinivasu", "password":"Daya", "dataFile" : "Hello"}'
    """if not os.path.exists(file_path):
        # Create a dummy json if it doesn't exists
        with open(file_path, "w") as f:
            json.dump({"key": "value"}, f)
    with open(file_path, "r") as f:
        data = json.load(f)"""
    data = json.loads(file_path)
    #print("Data from Fixture is :", data)
    return data


@given(parsers.parse('I use the "{jsonFile}" to generate fixture'), target_fixture=get_test_data)
def passJsonToFixture(get_test_data, jsonFile):
    print("Current Json File value sent is ", {jsonFile})
    print("Data Returned from Fixture: ", get_test_data)
    pass

@then(parsers.parse('I can use data from fixture'))
def useDataFromFixture(get_test_data):
    print("From Fixture again", get_test_data)
    pass