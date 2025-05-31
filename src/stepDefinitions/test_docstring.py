import pytest
from pytest_bdd import given, then, scenarios, parsers

scenarios('../features/docstring.feature')

@pytest.fixture
def assign_fixture():
    return "foo"

@given(parsers.parse('I am passing a value'), target_fixture="assign_fixture")
def assign_value_to_fixture():
    return "injected foo"

@then(parsers.parse("foo should be '{val}'"))
def assert_fixture_value(assign_fixture, val):
    print("\nvalue from feature file : %s <==> %s" %(val, assign_fixture))
    assert assign_fixture == val
