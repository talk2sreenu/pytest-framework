import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from src.greeter.Greeter import Greeter

scenarios("../features/greetings.feature")

@pytest.fixture
def greeter():
    return Greeter()

@given(parsers.parse("a Greeter"))
def a_new_greeter():
    print("New Scenario has been created")
    pass

@when(parsers.parse("I give my name as {name}"))
def assign_name_greeter(greeter, name):
    greeter.my_name(name)

@then(parsers.parse("the greeter says Hello {name}"))
def verify_greeter_message(greeter, name):
    assert greeter.greet() == 'Hello '+name

@then(parsers.parse('the greeter says "{message}"'))
def verify_greeter_message(greeter, message):
    assert greeter.greet() == message

@when(parsers.parse("I don't provide a name"))
def assign_no_name_greet(greeter):
    print("No Name provided")
    pass