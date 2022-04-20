from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    Title = By.ID, 'TitleBar'

    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(*self.Title).click()

    def find_element(self, by, value):
        return self.driver.find_element(by,value)

    def find_element_waiting_clickability(self, by, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((by, value)))
        return element

    def find_element_waiting_visibility(self, by, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((by, value)))
        return element
