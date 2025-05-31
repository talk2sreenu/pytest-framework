Feature: To test the scenario outlines with different scenarios

    Background:
        Given Read data from json file
        |firstdata.json|
        |seconddata.json|
        |{"username": "Srinivasu", "password":"Daya"}|


    Scenario Outline: The First Scenario outline Example
        Given I am using "<user>"

        Examples:
            | user | 
            | Srinivasu|
            | Amrutha|
            #| Rahitya|
    
    Scenario Outline: The Second Scenario outline Example
        Given I am giving "<user>"

        Examples:
            | user | 
            | Tom|
            | Bhayya|
            | Ali|