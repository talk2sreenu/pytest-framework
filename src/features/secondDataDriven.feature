@datadriven
Feature: Example Feature for second json data

    Background:
        Given the test data is loaded from "seconddata.json"

    Scenario: To verify the data read from JSON file using the second one
        Given the user enters "username" from data
        When the click login button
        Then the login is successful