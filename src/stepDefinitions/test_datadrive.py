import pytest
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("datadriven.feature", "secondDataDriven.feature")

@pytest.fixture()
def getData(request):
    return request.session.test_data
    #return {"userName" : ""}
    #jsonData = {}
    #jsonData = request.session.test_data
    #return jsonData

"""@given(parsers.parse('the user enters "{uname}" from data'))
def getUserName(request, uname, setUser):
    for i in range(0, len(request.session.test_data)):
        uname = request.session.test_data[i]["username"]
        print("Value from JSON", uname)
        setUser["userName"] = uname
        print("Value captured from scenario: ", setUser)"""

@given(parsers.parse('the user enters "{uname}" from data'))
def getUserName(uname, getData):
    print("\nValue from JSON", getData["username"], uname)

@when(parsers.parse("the click login button"))
def clickLoginButton(getData):
    print("Login button is clicked")
    print(getData["city"])

@then(parsers.parse("the login is successful"))
def checkLogin(getData):
    print("Login is successful for the user ")
    print(getData["email"])
    #del getData
