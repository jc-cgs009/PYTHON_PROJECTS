import time

from selenium.webdriver.common.by import By


class Add_Customer:
    link_main_customer_xpath = "//a[@href='#']/p[contains(text(),'Customers')]"
    link_sub_customer_xpath = "//a[@href='/Admin/Customer/List']/p[contains(text(),'Customers')]"
    link_add_new_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_first_name_id = "FirstName"
    txt_last_name_id = "LastName"
    rd_gender_male_id = "Gender_Male"
    rd_gender_female_id = "Gender_Female"
    txt_dob_id = "DateOfBirth"
    txt_customer_role_xpath = "(//div[@role='listbox'])[2]"
    li_register_xpath = "//li[contains(text(), 'Registered')]"
    li_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    li_guests_xpath = "//li[contains(text(), 'Guests')]"
    li_forum_moderators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    li_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_main_customer_link(self):
        self.driver.find_element(By.XPATH, self.link_main_customer_xpath).click()

    def click_on_sub_customer_link(self):
        self.driver.find_element(By.XPATH, self.link_sub_customer_xpath).click()

    def click_on_add_new_link(self):
        self.driver.find_element(By.XPATH, self.link_add_new_xpath).click()

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).clear()
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.txt_password_id).clear()
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(password)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.txt_first_name_id).clear()
        self.driver.find_element(By.ID, self.txt_first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.txt_last_name_id).clear()
        self.driver.find_element(By.ID, self.txt_last_name_id).send_keys(last_name)

    def select_gender(self, gender='male'):
        if gender == 'male':
            self.driver.find_element(By.ID, self.rd_gender_male_id).click()
        elif gender == 'female':
            self.driver.find_element(By.ID, self.rd_gender_female_id).click()

    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.txt_dob_id).send_keys(dob)

    def select_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.txt_customer_role_xpath).click()
        time.sleep(3)
        if role == 'guest':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.li_register_xpath).find_element(By.XPATH, "//span[@title='delete']").click()
            self.list_item = self.driver.find_element(By.XPATH, self.li_guests_xpath)
        elif role == 'vendors':
            self.list_item = self.driver.find_element(By.XPATH, self.li_vendors_xpath)
        elif role == 'administrators':
            self.list_item = self.driver.find_element(By.XPATH, self.li_administrators_xpath)
        elif role == 'forum moderators':
            self.list_item = self.driver.find_element(By.XPATH, self.li_forum_moderators_xpath)
        elif role == 'register':
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.li_guests_xpath).find_element(By.XPATH, "//span[@title='delete']").click()
            self.list_item = self.driver.find_element(By.XPATH, self.li_register_xpath)

        self.driver.execute_script("arguments[0].click();", self.list_item)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()





