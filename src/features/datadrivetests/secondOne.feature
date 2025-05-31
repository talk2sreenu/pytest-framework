Feature: To test the sending param to fixture

    Scenario Outline: 
        Given I am sending "<user>"
        Then I am using "<language>"
        When I will use jsonDaata
        Examples:
            | user      | language  |
            | Srinivasu | python    |
            | Amrutha   | HTML      |