import allure
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest

from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities import Readexcel
from testcase.BaseTest import BaseTest


@allure.severity(allure.severity_level.CRITICAL)
class Test_login(BaseTest):

    @pytest.mark.parametrize("username,password", Readexcel.readExcel("LoginPage"))
    def test_valid_login(self, username, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_the_user(username, password)
        assert account_page.edit_your_account_info_text()

    def test_invalid_login(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_the_user("", "")
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.empty_login_warning_message().__eq__(expected_text)
