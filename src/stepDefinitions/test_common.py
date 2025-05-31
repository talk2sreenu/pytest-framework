import pytest
from pytest_bdd import scenario, parsers

@scenario('common_steps.feature', 'All steps are declared in the conftest')
def test_all_steps_are_declared_in_the_conftest():
    """All steps are declared in the conftest."""
    print("might work")