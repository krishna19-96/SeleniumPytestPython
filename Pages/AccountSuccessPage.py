from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    your_account_has_been_created_xpath = "//div[@id='content']//h1"

    def your_account_has_been_created_message(self):
        return self.get_element_text("your_account_has_been_created_xpath", self.your_account_has_been_created_xpath)

