from pageObject.loginPage import Login_Page
from utilities.readProperties import Read_Config
from utilities.customLogger import Log_Gen


class Test_001_Login_Page:
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    base_url = Read_Config.get_application_url()
    logger = Log_Gen.log_gen()

    def test_homepage_title(self, setup):
        self.logger.info("****************** Test_001_Login_Page *********************")
        self.logger.info("****************** Started home page title test *********************")
        self.driver = setup
        self.driver.get(self.base_url)
        home_page_title = self.driver.title
        if home_page_title == "Your store. Login":
            self.driver.close()
            self.logger.info("****************** Home page title test passed *********************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/"+"test_homepage_title.png")
            self.driver.close()
            self.logger.error("******************Error : Home page title test failed *********************")
            assert False

    def test_login_page(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.logger.info("****************** Started login page title test *********************")
        lp = Login_Page(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        dashboard_title = self.driver.title
        if dashboard_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("****************** Login page title test passed *********************")
            assert True
        else:
            self.driver.save_screenshot("./screenshots/"+"test_login_page.png")
            self.driver.close()
            self.logger.error("****************** Error: Login page title test failed *********************")
            assert False




