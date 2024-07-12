from selenium.webdriver.common.by import By
from selenium import webdriver

from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_button_xpath = "//span[@class='input-group-btn']//button"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_dropdown_option_link_text = "Login"
    register_dropdown_option_link_text = "Register"


    def search_valid_product_name(self, product_name):
        self.type_to_element(product_name, "search_box_field_name, product_name", self.search_box_field_name, )

    def click_search_button(self):
        self.click_the_element("search_button_xpath", self.search_button_xpath)
        return SearchPage(self.driver)

    def my_account_drop_down(self):
        self.click_the_element("my_account_drop_menu_xpath", self.my_account_drop_menu_xpath)


    def login_dropdown_option(self):
        self.click_the_element("login_dropdown_option_link_text", self.login_dropdown_option_link_text)
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.my_account_drop_down()
        return self.login_dropdown_option()

    def register_dropdown_option(self):
        self.click_the_element("register_dropdown_option_link_text", self.register_dropdown_option_link_text)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.my_account_drop_down()
        return self.register_dropdown_option()
    def search_for_product(self, productname):
        self.search_valid_product_name(productname)
        return self.click_search_button()
