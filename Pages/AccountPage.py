from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_account_link_text = "Edit your account information"

    def edit_your_account_info_text(self):
        return self.check_display_status_of_element("edit_account_link_text", self.edit_account_link_text)

