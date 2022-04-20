from behave import *

from Pages.CalculatorPage import CalculatorPage

use_step_matcher('re')


@when('I click on the digit "(.*)"')
@Given('I click on the digit "(.*)"')
def step_impl(context, number):
    calculator = CalculatorPage(context.driver)
    calculator.clickDigit(number)


@Then('I see the number "(.*)" being displayed')
def step_impl(context, number):
    calculator = CalculatorPage(context.driver)
    actualnumber = calculator.getDisplayedNumber()
    assert actualnumber == number, "\n The Expected Displayed Number is " + number + "\nActual Number is " + actualnumber
