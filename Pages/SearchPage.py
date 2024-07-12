from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    product_search_page_link_text = "HP LP3065"
    No_product_message_xpath = "//input[@id='button-search']/following-sibling::p"

    def display_status_of_product(self):
        return self.check_display_status_of_element("product_search_page_link_text", self.product_search_page_link_text)

    def retrieving_no_product_search_message(self):
        return self.get_element_text("No_product_message_xpath", self.No_product_message_xpath)

