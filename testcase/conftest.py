import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failure", attachment_type=AttachmentType.PNG)

#
@pytest.fixture(scope="function", params=["chrome"])
def setup_and_teardown(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    request.cls.driver = driver
    yield
    driver.quit()

# @pytest.fixture(scope="function")
# def setup_and_teardown(request):
#     global driver
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     else:
#         print("Enter the valid browser")
#     driver.maximize_window()
#     driver.get("https://tutorialsninja.com/demo")
#     request.cls.driver = driver
#     yield
#     driver.quit()