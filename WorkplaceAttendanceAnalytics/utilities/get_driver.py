from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_web_driver():
    # service_obj = Service(executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    return driver

