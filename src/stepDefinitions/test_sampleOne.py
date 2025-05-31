import pytest
import json
from pytest_bdd import given, scenarios, parsers

scenarios('./datadrivetests/sampleOne.feature')
@pytest.fixture
def json_data():
    file_path = '{"username": "Srinivasu", "password":"Daya"}'
    """if not os.path.exists(file_path):
        # Create a dummy json if it doesn't exists
        with open(file_path, "w") as f:
            json.dump({"key": "value"}, f)
    with open(file_path, "r") as f:
        data = json.load(f)"""
    data = json.loads(file_path)
    print("Data from Fixture is :", data)
    return data

@given(parsers.parse("Read data from json file"), target_fixture=json_data)
def printsomething(datatable, json_data):
    print("\nPrinting something here from Data Table of the background")
    for i in range(0, len(datatable)):
        print(datatable[i][0])

    print(json_data)

@given(parsers.parse('I am using "{user}"'))
def printUsingUserName(json_data, user):
    print("Using user value :", user)
    print('Instead can use from fixture : ', json_data['username'])
    pass

@given(parsers.parse('I am giving "{user}"'))
def printGivingUserName(json_data, user):
    print("Giving user value :", user)
    print('Instead can use from fixture : ', json_data['password'])
    pass