Feature: Test sum of numbers in calculator
  The purpose of this is to test multiple sums or addition of numbers
  on the windows 10 calculator using Winium

  Scenario: Summing positive numbers
    Given I click on the digit "1"
    And I click on the digit "2"
    And I click on the digit "3"
    And I click on the digit "4"
    And I click on the digit "5"
    And I click on the digit "6"
    And I click on the digit "7"
    And I click on the digit "8"
    When I click on the digit "9"
    Then I see the number "123456789" being displayed