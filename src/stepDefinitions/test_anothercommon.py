from pytest_bdd import scenario

@scenario("anothercommon.feature", "This is for reusing steps")
def test_this_is_for_reusing_steps():
    print("Another try with reusable steps")

