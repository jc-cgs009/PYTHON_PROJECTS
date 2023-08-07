from selenium.webdriver.common.by import By


class GetEmployeeDetails:
    job_title_xpath = "//div[@class='data-bar single-line-bar']/div[1]/p"
    department_name_xpath = "//div[@class='data-bar single-line-bar']/div[2]/p"
    reporting_manager_xpath = "//div[@class='data-bar single-line-bar']/div[4]/p"
    emp_name_class_name = "mr-20.ng-star-inserted"
    location_xpath = "//div[@class='mr-40 d-flex align-items-center ng-star-inserted'][1]/span[2]"

    def __init__(self, driver):
        self.driver = driver

    def get_job_title(self):
        return self.driver.find_element(By.XPATH, self.job_title_xpath).text

    def get_department_name(self):
        return self.driver.find_element(By.XPATH, self.department_name_xpath).text

    def get_reporting_manager_name(self):
        return self.driver.find_element(By.XPATH, self.reporting_manager_xpath).text

    def get_employee_name(self):
        return self.driver.find_element(By.CLASS_NAME, self.emp_name_class_name).text

    def get_location_name(self):
        return self.driver.find_element(By.XPATH, self.location_xpath).text

