import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest

from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage
from testcase.BaseTest import BaseTest


class TestSearch(BaseTest):

    @allure.severity(allure.severity_level.MINOR)
    def test_search_product(self):
        home_page = HomePage(self.driver)
        search_page =home_page.search_for_product("Hp")
        assert search_page.display_status_of_product()

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_search_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("Honda")
        expected_result = "There is no product that matches the search criteria."
        assert search_page.retrieving_no_product_search_message().__eq__(expected_result)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_without_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_product("")
        expected_result = "There is no product that matches the search criteria."
        assert search_page.retrieving_no_product_search_message().__eq__(expected_result)
