from selenium.webdriver.common.by import By

from Pages.AccountPage import AccountPage
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    empty_login_page_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"


    def enter_email_address(self,email):
        self.type_to_element(email,"email_field_id", self.email_field_id)

    def enter_password(self,password):
        self.type_to_element(password, "password_field_id", self.password_field_id)
    def click_login_button(self):
        self.click_the_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def login_the_user(self,email,password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_login_button()

    def empty_login_warning_message(self):
        return self.get_element_text("empty_login_page_warning_xpath", self.empty_login_page_warning_xpath)