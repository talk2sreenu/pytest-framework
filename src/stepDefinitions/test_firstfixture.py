import pytest
from pytest_bdd import scenarios, given, then, parsers, when

scenarios('../features/fixtureTests/firstfixture.feature')

@pytest.fixture()
def get_test_data(request):
   return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]

@given(parsers.parse('This is a fixture step'))
def given_fixture_step(get_test_data):
    print("Fixture data:", get_test_data)
    pass

@then(parsers.parse('This is a fixture step'))
def when_using_fixture_data(get_test_data):
    for data in get_test_data:
        print(f"Name: {data['name']}, Age: {data['age']}")

    get_test_data.append({"name": "David", "age": 40})
    print("Updated fixture data:", get_test_data)
    pass

@then(parsers.parse('This is another fixture step'))
def then_verify_fixture_data(get_test_data):
    assert len(get_test_data) == 4, "Expected 4 items in fixture data"
    for data in get_test_data:
        assert 'name' in data and 'age' in data, "Each item should have 'name' and 'age' keys"
    print("Fixture data verification passed")
    pass
