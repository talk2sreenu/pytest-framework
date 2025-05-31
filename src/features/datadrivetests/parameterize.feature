Feature: To test the parameterization using fixtures

Scenario Outline: Implement parameterization
    Given I use the "<jsonFile>" to generate fixture
    Then I can use data from fixture

    Examples:
    |jsonFile|
    |testdata.json|
    |sampledata.json|
    |complexdata.json|