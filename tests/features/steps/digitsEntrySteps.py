from behave import *

use_step_matcher('re')


@when('I click on the digit "(.*)"')
@Given('I click on the digit "(.*)"')
def step_impl(context, number):
    context.calculator.clickDigitWaiting(number)


@Then('I see the number "(.*)" being displayed')
def step_impl(context, number):
    actualnumber = context.calculator.getDisplayedNumber()
    assert actualnumber == number, "\n The Expected Displayed Number is " + number + "\nActual Number is " + actualnumber


@Given('I click the number "(.*)" on keyboard')
def step_impl(context, number):
    context.calculator.clickNumber(number)


@Given('I press the number "(.*)" on keyboard')
def step_impl(context, number):
    context.calculator.pressKeyBoardKeys(number)


@Given('I click the Multiplication button')
def step_impl(context):
    context.calculator.clickmultiplication()


@When('I click the equals button')
def step_impl(context):
    context.calculator.clickequals()


@Given('I click the Addition button')
def step_impl(context):
    context.calculator.clickaddition()


@Given('I click the Subtraction button')
def step_impl(context):
    context.calculator.clicksubtraction()


@Given('I click the Division button')
def step_impl(context):
    context.calculator.clickdivision()
