from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        service_obj = Service("D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ######## pytest HTML report #########
# # It is hook for adding environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'Customer'
#     config._metadata['Tester'] = 'Suhas'
#
#
#
# # It is hook for delete/ modify environment info to HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)




