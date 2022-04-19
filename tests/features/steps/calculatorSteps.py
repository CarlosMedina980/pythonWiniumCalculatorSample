from behave import *
from Pages.CalculatorPage import CalculatorPage
from Utilities.NumbersEnum import Digits

use_step_matcher('re')


@when('I click on the digit "(.*)"')
@Given('I click on the digit "(.*)"')
def step_impl(context, number):
    calculator = CalculatorPage(context.driver)
    calculator.clickDigit(number)

@Then('I see the number "(.*)" being displayed')
def step_impl(context, number):
    calculator = CalculatorPage(context.driver)
    assert calculator.getDisplayedNumber() == number
