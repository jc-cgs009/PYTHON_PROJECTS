import time

from pageobject.login_page import LoginPage
from pageobject.search_employee import SearchEmployee
from pageobject.get_employee_details import GetEmployeeDetails

from utilities import get_driver
from utilities import get_todays_date
# from utilities import get_text_from_image
from utilities.excel_utils import ExcelWork
from utilities import read_emp_data
from utilities import check_file_existence
from utilities.get_otp_from_email import GetOtpFromEmail
from utilities.get_year_month_day import get_year_month_day

from database.database_operations import DatabaseOperations


class EnterAttendance:
    base_url = "https://app.keka.com/Account/Login"
    email = "schandra@msystechnologies.com"
    password = "SjcKekaCgs@999"
    emp_id_text_file_path = "D:\\PythonProject\\AttendenceEntry\\employeeData\\empid.txt"
    # captcha_img_file_path = "D:\\PythonProject\\AttendenceEntry\\captchaIMG\\captcha_img.png"
    # date = str(get_todays_date.get_today_date())
    date = "2023-08-04"
    excel_file_name = "attendance_on_"+date+".xlsx"
    excel_file_path = "D:\\PythonProject\\AttendenceEntry\\excel_report\\"+excel_file_name
    database_name = 'msys'
    table_name = 'employee_data'
    table_columns = ('Date', 'Emp_id', 'Emp_name', 'Department', 'Designation', 'Location',
                     'Reporting_manager', 'Year', 'Month', 'Day')
    year, month, day = get_year_month_day(date)
    driver = get_driver.get_web_driver()

    def __init__(self):
        self.name = None
        self.department = None
        self.location = None
        self.reporting_manager = None
        self.job_title = None

    def login_to_Keka_portal(self):
        # create login page object
        lp = LoginPage(self.driver)

        # Login in to keka portal
        lp.setup(self.base_url)
        lp.enter_email(self.email)
        lp.click_on_submit_button()
        lp.click_on_keka_password_button()
        lp.enter_password(self.password)

        # get text from captcha image
        # lp.take_screen_short_of_captcha(self.captcha_img_file_path)
        # text = get_text_from_image.extract_text(self.captcha_img_file_path)
        # lp.enter_captcha(text)

        lp.click_on_login_button()
        lp.click_on_email()

        # get OTP from email #
        go = GetOtpFromEmail()
        go.log_in_to_email_account()
        email_uid = go.get_latest_uid_of_the_searched_email()
        message_data = go.fetch_email_message(email_uid)
        if message_data:
            otp = go.get_OTP(message_data)
            if not otp:
                print("Error : get OTP!")
                return
        else:
            print("Error : fetch email message!")
            return

        lp.enter_verification_code(otp)
        lp.click_on_login_submit_button()

        return lp

    def get_employee_id(self):
        return read_emp_data.get_emp_data(self.emp_id_text_file_path)

    def create_or_load_excel_workbook(self):
        # create excel object
        xl = ExcelWork(self.date)
        # check Excel file exist or not
        result = check_file_existence.file_exist_or_not(self.excel_file_path)
        if result:
            # load the existing work book
            xl.load_work_book(self.excel_file_path)
            c = (xl.get_row_count()) - 1
        else:
            # create excel workbook
            xl.create_work_book(self.excel_file_path)
            c = 0
        return c, xl

    def create_database(self):
        # creating database operations object
        db = DatabaseOperations()
        return db

    def update_data_to_excel(self, xl, c, emp_details):
        # update emp details in excel sheet
        xl.write_data(emp_details, self.excel_file_path)
        c += 1
        return c

    def update_data_to_database(self, db, value):
        # update emp details in database
        db.insert_into_table(self.database_name, self.table_name, self.table_columns, value)

    def search_get_and_update_employee_data(self, employee_id, c, xl, db):
        # Create Search Employee Object
        se = SearchEmployee(self.driver)

        # Create Get Employee Details Object
        ged = GetEmployeeDetails(self.driver)

        not_found = []
        for i, emp_id in enumerate(employee_id, start=1):
            # Search Employee's
            try:
                se.search_employee(emp_id)
                se.click_on_searched_employee()
            except:
                se.clear_search_employee_text_box()
                not_found.append((emp_id, i))
            else:
                # get employee data
                self.name = ged.get_employee_name()
                self.department = ged.get_department_name()
                self.location = ged.get_location_name()
                self.reporting_manager = ged.get_reporting_manager_name()
                self.job_title = ged.get_job_title()

                emp_details = [c + 1, self.date, self.name, emp_id, self.department, self.location,
                               self.reporting_manager]
                value = (self.date, emp_id, self.name, self.department, self.job_title, self.location,
                         self.reporting_manager, self.year, self.month, self.day)

                # update emp details in excel sheet
                c = self.update_data_to_excel(xl, c, emp_details)

                # update emp details in database
                self.update_data_to_database(db, value)

        return f"Emp Id's (not found) : {not_found}"

    def logout_from_keka_portal(self, lp):
        lp.log_out()

    def enter_attendance(self):
        lp = self.login_to_Keka_portal()
        employee_id = self.get_employee_id()
        c, xl = self.create_or_load_excel_workbook()
        db = self.create_database()
        not_found_emp = self.search_get_and_update_employee_data(employee_id, c, xl, db)
        self.logout_from_keka_portal(lp)
        return not_found_emp






