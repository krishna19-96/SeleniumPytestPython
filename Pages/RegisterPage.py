from selenium.webdriver.common.by import By

from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname_id = "input-firstname"
    lastname_id = "input-lastname"
    email_id = "input-email"
    phone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    subscribe_radio_button_xpath = "(//input[@type='radio'])[2]"
    agree_checkbox_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"

    email_already_register_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    you_must_agree_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_empty_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    lastname_empty_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_empty_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    phone_number_empty_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_empty_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_firstname(self, firstname):
        self.type_to_element(firstname, "firstname_id", self.firstname_id)

    def enter_lastname(self, lastname):
        self.type_to_element(lastname, "lastname_id", self.lastname_id)

    def enter_email(self, email):
        self.type_to_element(email, "email_id", self.email_id)

    def enter_phone(self, phone):
        self.type_to_element(phone, "phone_id", self.phone_id)

    def enter_password(self, password):
        self.type_to_element(password, "password_id", self.password_id)

    def enter_confirm_password(self, confirm_password):
        self.type_to_element(confirm_password, "confirm_password_id", self.confirm_password_id)

    def subscribe_radio_button(self):
        self.click_the_element("subscribe_radio_button_xpath", self.subscribe_radio_button_xpath)

    def agree_checkbox(self):
        self.click_the_element("agree_checkbox_name", self.agree_checkbox_name)

    def click_continue_button(self):
        self.click_the_element("continue_button_xpath", self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def register_the_user(self, firstname, lastname, email, phone, password, confirm_password, subscribe_text,
                          agree_text):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_phone(phone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if subscribe_text == "Yes":
            self.subscribe_radio_button()
        if agree_text == "Yes":
            self.agree_checkbox()
        return self.click_continue_button()

    def email_already_register_warning_message(self):
        return self.get_element_text("email_already_register_warning_xpath", self.email_already_register_warning_xpath)

    def you_must_agree_warning_message(self):
        return self.get_element_text("you_must_agree_warning_xpath", self.you_must_agree_warning_xpath)

    def firstname_empty_warning_message(self):
        return self.get_element_text("firstname_empty_warning_xpath", self.firstname_empty_warning_xpath)

    def lastname_empty_warning_message(self):
        return self.get_element_text("lastname_empty_warning_xpath", self.lastname_empty_warning_xpath)

    def email_empty_warning_message(self):
        return self.get_element_text("email_empty_warning_xpath", self.email_empty_warning_xpath)

    def phone_number_empty_warning_message(self):
        return self.get_element_text("phone_number_empty_warning_xpath", self.phone_number_empty_warning_xpath)

    def password_empty_warning_message(self):
        return self.get_element_text("password_empty_warning_xpath", self.password_empty_warning_xpath)

    def verify_all_warning(self, expected_warning_message, expected_first_name_warning, expected_last_name_warning,
                           expected_email_warning, expected_phone_warning, expected_password_warning):
        actual_warning_message = self.you_must_agree_warning_message()
        actual_first_name_warning = self.firstname_empty_warning_message()
        actual_last_name_warning = self.lastname_empty_warning_message()
        actual_email_warning = self.email_empty_warning_message()
        actual_phone_warning = self.phone_number_empty_warning_message()
        actual_password_warning = self.password_empty_warning_message()

        status = False

        if actual_warning_message.__eq__(expected_warning_message):
            if actual_first_name_warning.__eq__(expected_first_name_warning):
                if actual_last_name_warning.__eq__(expected_last_name_warning):
                    if actual_email_warning.__eq__(expected_email_warning):
                        if actual_phone_warning.__eq__(expected_phone_warning):
                            if actual_password_warning.__eq__(expected_password_warning):
                                status = True

        return status
