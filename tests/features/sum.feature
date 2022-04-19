Feature: Test sum of numbers in calculator
  The purpose of this is to test multiple sums or addition of numbers
  on the windows 10 calculator using Winium

  Scenario: Summing positive numbers
    Given I open the windows 10 calculator
    When I click on the number "5"
    And I click on the "Addition" button
    And  I click on the number "10"
    And I click on the "Equals" button
    Then The result displayed is "15"