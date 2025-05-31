@datadriven
Feature: Example Feature

    Background:
        Given the test data is loaded from "backgroundtestdata.json"

    Scenario: To verify the data read from JSON file
        Given the user enters "username" from data
        When the click login button
        Then the login is successful