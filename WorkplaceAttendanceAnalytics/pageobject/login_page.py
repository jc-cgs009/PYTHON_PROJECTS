import time

from selenium.webdriver.common.by import By


class LoginPage:
    textbox_email_id = "email"
    button_submit_xpath = "//button[@type='submit']"
    button_keka_password_xpath = "//div/p[text()='Keka Password']"
    textbox_password_id = "password"
    captcha_element_xpath = "//img[@id='imgCaptcha']"
    textbox_captcha_id = "captcha"
    button_login_xpath = "//button[text()='Login']"
    button_mobile_xpath = "(//p[@class='verify-btn-content'])[1]"
    button_email_xpath = "(//p[@class='verify-btn-content'])[2]"
    textbox_code_id = "code"
    button_login2_xpath = "//button[@type='submit']"
    down_arrow_button_xpath = "(//span[@class='ki-chevron-down ki'])"
    logout_button_xpath = "//a[@routerlink='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def setup(self, base_url):
        self.driver.get(base_url)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def click_on_submit_button(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def click_on_keka_password_button(self):
        self.driver.find_element(By.XPATH, self.button_keka_password_xpath).click()
        time.sleep(10)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    # def take_screen_short_of_captcha(self, file_path):
    #     captcha_element = self.driver.find_element(By.XPATH, self.captcha_element_xpath)
    #     captcha_element.screenshot(file_path)
    #
    # def enter_captcha(self, text):
    #     self.driver.find_element(By.ID, self.textbox_captcha_id).send_keys(text)
    #
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        time.sleep(5)

    # def click_on_mobile(self):
    #     self.driver.find_element(By.XPATH, self.button_mobile_xpath).click()
    #     time.sleep(15)

    def click_on_email(self):
        self.driver.find_element(By.XPATH, self.button_email_xpath).click()
        time.sleep(5)

    def enter_verification_code(self, otp):
        self.driver.find_element(By.ID, self.textbox_code_id).send_keys(otp)

    def click_on_login_submit_button(self):
        self.driver.find_element(By.XPATH, self.button_login2_xpath).click()
        time.sleep(10)

    def log_out(self):
        self.driver.find_element(By.XPATH, self.down_arrow_button_xpath).click()
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()




