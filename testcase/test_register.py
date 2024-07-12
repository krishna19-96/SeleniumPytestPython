from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from testcase.BaseTest import BaseTest
from Utilities import Readexcel

class TestRegister(BaseTest):
    @pytest.mark.parametrize("firstname,lastname,phone,password,confrim_password", Readexcel.readExcel("Register"))
    def test_valid_register(self, firstname, lastname, phone, password, confrim_password):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        global email
        email = self.fake_email()
        account_success_page = register_page.register_the_user(firstname, lastname, email, phone, password, confrim_password, "No", "Yes")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.your_account_has_been_created_message().__eq__(expected_text)

    def test_valid_with_sub_register(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_the_user("test", "123456", self.fake_email(), "1231231331", "1234", "1234",
                                                               "Yes", "Yes")
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.your_account_has_been_created_message().__eq__(expected_text)
        time.sleep(2)

    def test_already_user_email_with_sub_register(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_the_user("test", "123456", email, "1231231331", "1234",
                                                               "1234",
                                                               "No", "Yes")
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.email_already_register_warning_message().__eq__(expected_warning_message)
        time.sleep(2)

    def test_invalid_data_with_sub_register(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_the_user("", "", "", "", "",
                                        "",
                                        "No", "No")
        assert register_page.verify_all_warning("Warning: You must agree to the Privacy Policy!", "First Name must be between 1 and 32 characters!", "Last Name must be between 1 and 32 characters!", "E-Mail Address does not appear to be valid!", "Telephone must be between 3 and 32 characters!", "Password must be between 4 and 20 characters!" )
