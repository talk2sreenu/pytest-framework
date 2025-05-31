Feature: TO verify the DataTables in pytest bdd framework

    Background:
        Given User Logs into application

    Scenario: To check how datatables used in pytest
        When User enters the below forms information
        |Srinivasu|
        |Kaki|
        |Wake Forest|
        |North Carolina|
        Then User registration is complete

    Scenario Outline: Verify registration functionality
        When User enters "<FName>","<LName>","<Email>" details
        Then User registration is complete
        Examples:
        |FName|LName|Email|
        |Srinivasu|Kaki|abcd@gmail.com|
        |Kaki|sdfskh|ertyihjk@dhfds.com|
        |tesiuf|efefsdj|7dshfkjsd@75jd.com|