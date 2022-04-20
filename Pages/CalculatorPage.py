import clipboard
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
    Display_Text = By.XPATH, "/*[@AutomationId='CalculatorResults' and @ControlType='ControlType.Text' and " \
                             "@LocalizedControlType='text']"

    def __init__(self, driver):
        super().__init__(driver)

    def clickDigitWaiting(self, number):
        self.find_element_waiting_clickability(By.ID, 'num{}Button'.format(number)).click()

    def clickDigit(self, number):
        self.find_element(By.ID, 'num{}Button'.format(number)).click()

    def getDisplayedNumber(self):
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        return clipboard.paste()
