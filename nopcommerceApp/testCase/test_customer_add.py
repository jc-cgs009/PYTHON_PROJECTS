import random
import string

from selenium.webdriver.common.by import By

from pageObject.loginPage import Login_Page
from pageObject.addCustomer import Add_Customer
from utilities.readProperties import Read_Config
from utilities.customLogger import Log_Gen


class Test_003_Customer_Add:
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    base_url = Read_Config.get_application_url()
    logger = Log_Gen.log_gen()

    def test_customer_add(self, setup):
        self.logger.info('********** Test_003_Customer_Add **********')
        self.logger.info('*************** login started *********')
        self.driver = setup
        self.driver.get(self.base_url)
        lp = Login_Page(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        self.logger.info('************* login successfully *****************')

        self.logger.info('************** started customer add test ******************')
        ac = Add_Customer(self.driver)
        ac.click_on_main_customer_link()
        ac.click_on_sub_customer_link()
        ac.click_on_add_new_link()
        self.email = random_data_generator()+'@gmail.com'
        ac.enter_email(self.email)
        ac.enter_password("test123")
        ac.enter_first_name("python")
        ac.enter_last_name("selenium")
        ac.select_gender("female")
        ac.enter_dob("01/01/2004")
        ac.select_customer_role("guest")
        # ac.select_customer_role("vendors")
        # ac.select_customer_role("register")
        ac.click_on_save()
        msg = self.driver.find_element(By.TAG_NAME, 'body').text
        if 'The new customer has been added successfully.' in msg:
            self.logger.info('*********** Add Customer passed***********')
            assert True
        else:
            self.logger.info('**************** Add Customer failed ************')
            assert False

        self.driver.close()
        self.logger.info('************** completed customer add test ******************')


def random_data_generator(size=8, char=string.ascii_lowercase):
    return ''.join(random.choice(char) for i in range(size))

