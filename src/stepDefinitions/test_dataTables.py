import pytest
from pytest_bdd import given, when, then, scenarios, parsers

scenarios("../features/dataTables.feature")

@given(parsers.parse("User Logs into application"))
def login_to_app():
    print("user logged into the app")
    pass

@when(parsers.parse("User enters the below forms information"))
def user_fills_forms(datatable):
    newList = list()
    newList = datatable[0:]
    for i in range(0, len(newList), 1):
        print("The current value is : ", str(newList[i]))
    pass

@then(parsers.parse("User registration is complete"))
def user_registration_complete():
    print("registration is complete")
    pass

@when(parsers.parse('User enters "{FName}","{LName}","{Email}" details'))
def user_reg_process(FName, LName, Email):
    print("Current user details : %s || %s || %s" %(FName, LName, Email))
    print('Current user details : {} || {} || {}'.format(FName, LName, Email))
    pass