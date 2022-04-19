from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class CalculatorPage(BasePage):
    # Nuber Pad Buttons
    Decimal_Separator = By.ID, 'decimalSeparatorButton'
    Positive_Negative = By.ID, 'negateButton'

    # Operators
    Division_Button = By.ID, 'negateButton'
    Multiplication_Button = By.ID, 'multiplyButton'
    Minus_Button = By.ID, 'minusButton'
    Addition_Button = By.ID, 'plusButton'
    Equals_Button = By.ID, 'equalButton'

    # Standard Functions
    Reciprocal_Button = By.ID, 'invertButton'
    Square_Button = By.ID, 'xpower2Button'
    Square_Root_Button = By.ID, 'squareRootButton'

    # Display Controls
    Percent_Button = By.ID, 'percentButton'
    Clear_Entry_Button = By.ID, 'clearEntryButton'
    Clear_Button = By.ID, 'clearButton'
    Backspace_Button = By.ID, 'backSpaceButton'

    # Display
    Display_Element = By.ID, 'CalculatorResults'

    def __init__(self, driver):
        super().__init__(driver)

    def clickDigit(self, number):
        self.find_element(By.ID, 'num{}Button'.format(number)).click()

    def getDisplayedNumber(self):
        self.find_element(*self.Display_Element).text()
