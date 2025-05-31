Feature: SCenario Outline with Examples

    @extest
    Scenario Outline: Oulined with Examples
        Given there are <start> cucumbers
        When I eat <eat> cucumbers
        Then I should have <left> cucumbers

        @ex1
        Examples:
        |start|eat|left|
        |12|5|7|
        |5|4|1|

        @ex2
        Examples:
        |start|eat|left|
        |10|5|5|
        |6|4|2|