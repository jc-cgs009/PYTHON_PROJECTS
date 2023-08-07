from pageObject.loginPage import Login_Page
from utilities.readProperties import Read_Config
from utilities.customLogger import Log_Gen
from utilities import XLutils


class Test_002_LoginPage_DDT:
    path = './testData/login_data.xlsx'
    base_url = Read_Config.get_application_url()
    logger = Log_Gen.log_gen()

    def test_login_page_ddt(self, setup):
        self.logger.info("****************** Test_002_LoginPage_DDT*********************")
        self.logger.info("****************** Started login page ddt test *********************")
        self.driver = setup
        self.driver.get(self.base_url)
        lp = Login_Page(self.driver)
        rows = XLutils.get_row_count(self.path, 'loginData')

        for r in range(2, rows+1):
            user = XLutils.read_excel_data(self.path, 'loginData', r, 1)
            password = XLutils.read_excel_data(self.path, 'loginData', r, 2)
            exp_res = XLutils.read_excel_data(self.path, 'loginData', r , 3)

            lp.set_username(user)
            lp.set_password(password)
            lp.click_login_button()

            act_title = self.driver.title

            status = []
            if act_title == 'Dashboard / nopCommerce administration':
                if exp_res == 'pass':
                    lp.click_logout_link()
                    status.append('pass')
                    self.logger.info("*** passed ***")
                elif exp_res == 'fail':
                    status.append('fail')
                    self.logger.info("*** failed ***")
            else:
                if exp_res == 'pass':
                    status.append('fail')
                    self.logger.info('*** failed ***')
                elif exp_res == 'fail':
                    status.append('pass')
                    self.logger.info('*** passed ***')

        if 'fail' in status:
            self.driver.close()
            self.logger.error('*** Login page DDT test failed ***')
            assert False
        else:
            self.driver.close()
            self.logger.info('*** Login page DDT test passed ***')
            assert True

        self.logger.info('****************** completed login page ddt test *********************')




