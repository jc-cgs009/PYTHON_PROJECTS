import time

from selenium.webdriver.common.by import By


class SearchEmployee:
    textbox_search_employee_xpath = "//input[@placeholder='Search employees or actions (Ex: Apply Leave, Attendance Approvals)']"
    dropdown_searched_employee_xpath = "//button/div/a[@placement='right']"

    def __init__(self, driver):
        self.driver = driver

    def search_employee(self, emp_id):
        self.driver.find_element(By.XPATH, self.textbox_search_employee_xpath).send_keys(emp_id)
        time.sleep(2)

    def clear_search_employee_text_box(self):
        self.driver.find_element(By.XPATH, self.textbox_search_employee_xpath).clear()
        time.sleep(2)

    def click_on_searched_employee(self):
        self.driver.find_element(By.XPATH, self.dropdown_searched_employee_xpath).click()
        time.sleep(2)

