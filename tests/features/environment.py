# # before all
# def before_all(context):
#     print('Before all executed')
#
#
# # before every scenario
# def before_scenario(scenario, context):
#     print('Before scenario executed')
#
#
# # after every feature
# def after_feature(scenario, context):
#     print('After feature executed')
#
#
# # after all
# def after_all(context):
#     print('After all executed')
import os

from selenium import webdriver


def before_scenario(context, scenario):
    os.startfile(r'C:\Users\Carlos_Medina\Documents\pythonWiniumCalculatorSample\Drivers\Winium.Desktop.Driver.exe')
    context.driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={
        "app": r'C:\Windows\System32\calc.exe',
        "args": '-port 345'})

def after_scenario(context, scenario):
    context.driver.find_element_by_name("Close Calculator").click()
    os.system("TASKKILL /F /IM Winium.Desktop.Driver.exe")
