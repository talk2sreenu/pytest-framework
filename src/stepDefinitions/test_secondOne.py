import pytest
import json
from pytest_bdd import given, scenarios, parsers, then, when

scenarios('./datadrivetests/secondOne.feature')
@pytest.fixture
def jsonData():
    def _jsonData(name: str):
        print("Value from given step :", name)
        return "Hello "+name.upper() + "!!!"
    return _jsonData

@given(parsers.parse('I am sending "{user}"'))
def sendingval(user, jsonData):
    print("\nThe value Examples : " , user)
    print("Value Returned from Fixture : ", jsonData(user))
    pass

@then(parsers.parse('I am using "{lang}"'))
def sendingval(lang, jsonData):
    print("\nThe value Examples : " , lang)
    print("Value Returned from Fixture : ", jsonData(lang))
    pass

@when(parsers.parse('I will use jsonDaata'))
def sendingval(jsonData):
    print("Value Returned from Fixture : ", jsonData)
    pass