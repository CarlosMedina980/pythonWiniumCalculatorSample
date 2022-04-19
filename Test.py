import os

from selenium import webdriver

os.startfile(r'C:\Users\Carlos_Medina\Documents\pythonWiniumCalculatorSample\Drivers\Winium.Desktop.Driver.exe')

driver = webdriver.Remote(command_executor='http://localhost:9999', desired_capabilities={
    "app": r'C:\Windows\System32\calc.exe',
    "args": '-port 345'
})

driver.find_element_by_name("Two").click()
driver.find_element_by_name("Multiply by").click()
driver.find_element_by_name("Eight").click()
driver.find_element_by_name("Equals").click()
isPresent = driver.find_element_by_name("Display is 16")
assert isPresent.id != 0
driver.find_element_by_name("Close Calculator").click()
os.system("TASKKILL /F /IM Winium.Desktop.Driver.exe")
