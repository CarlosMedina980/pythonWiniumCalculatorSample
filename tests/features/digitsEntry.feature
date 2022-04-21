Feature: Test sum of numbers in calculator
  The purpose of this is to test multiple sums or addition of numbers
  on the windows 10 calculator using Winium

  Scenario: Verify numbers pad is working correctly clicking
    Given I click on the digit "1"
    And I click on the digit "2"
    And I click on the digit "3"
    And I click on the digit "4"
    And I click on the digit "5"
    And I click on the digit "6"
    And I click on the digit "7"
    And I click on the digit "8"
    And I click on the digit "9"
    When I click on the digit "0"
    Then I see the number "1234567890" being displayed

  Scenario: Verify numbers pad is working correctly clicking
    Given I click the number "9876543210" on keyboard
    Then I see the number "9876543210" being displayed

  Scenario: Verify numbers pad is working correctly typing
    Given I press the number "1234567890" on keyboard
    Then I see the number "1234567890" being displayed

  Scenario: Addition Validation
    Given I press the number "5000000" on keyboard
    And I click the Addition button
    And I press the number "7000000" on keyboard
    When I click the equals button
    Then I see the number "12000000" being displayed

  Scenario: Subtraction Validation
    Given I press the number "5555555" on keyboard
    And I click the Subtraction button
    And I press the number "4444444" on keyboard
    When I click the equals button
    Then I see the number "1111111" being displayed

  Scenario: Multiplication Validation
    Given I press the number "2000000" on keyboard
    And I click the Multiplication button
    And I press the number "40" on keyboard
    When I click the equals button
    Then I see the number "80000000" being displayed


  Scenario: Division Validation
    Given I press the number "1024" on keyboard
    And I click the Division button
    And I press the number "2" on keyboard
    When I click the equals button
    Then I see the number "512" being displayed