import os

from behave import *
from selenium import webdriver

use_step_matcher('re')


@given('I open the windows 10 calculator')
def step_impl(context):
    os.startfile(r'C:\Users\Carlos_Medina\Documents\pythonWiniumCalculatorSample\Drivers\Winium.Desktop.Driver.exe')
    driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={
        "app": r'C:\Windows\System32\calc.exe',
        "args": '-port 345'
    })
