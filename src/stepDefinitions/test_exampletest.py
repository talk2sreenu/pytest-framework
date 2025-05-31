import pytest
from pytest_bdd import given, then, scenarios, parsers, when

scenarios('../features/examplestest.feature')

@given(parsers.parse('there are {start:d} cucumbers'), target_fixture="cucumber")
def create_fixture(start):
    return {'start' : start, 'eat': 0}

@when(parsers.parse('I eat {eat:d} cucumbers'))
def count_cucumbers_ate(cucumber, eat):
    cucumber["eat"] +=eat

@then(parsers.parse("I should have {left:d} cucumbers"))
def verify_leftover_cucumebrs(cucumber, left):
    assert cucumber['start'] - cucumber['eat'] == left

