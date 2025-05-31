Feature: Target fixture

    Scenario: Test given fixture injection
        Given I am passing a value
        Then foo should be 'injected foo'
    