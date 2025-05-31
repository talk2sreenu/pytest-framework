import pytest
from pytest_bdd import given, when, then, scenarios, parsers

scenarios('../features/parsers_example.feature')

cucumber = {'start': 0, 'eat':0}

@given(parsers.parse("there are {start:d} cucumbers"))
def given_cucumbers(start):
    print("Number sent in Given statement")
    cucumber["start"] = start
    print(cucumber["start"])

@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(eat):
    cucumber["eat"] +=eat

@then(parsers.parse("I should have {total:d} cucumbers"))
def count_cucumbers(total):
    finalVal = cucumber["start"] - cucumber["eat"]
    assert finalVal == total
    print("No cucumbers left to eat now")
    cucumber["start"] = 0
    cucumber["eat"] = 0
    pass

