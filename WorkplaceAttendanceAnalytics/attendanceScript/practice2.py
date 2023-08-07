def enter_attendance(self):
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

    # get employee ID's
    employee_ID = read_emp_data.get_emp_data(self.emp_id_text_file_path)

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

    # creating database operations object
    db = DatabaseOperations()

    # Create Search Employee Object
    se = SearchEmployee(self.driver)

    # Create Get Employee Details Object
    ged = GetEmployeeDetails(self.driver)

    not_found = []
    for i, emp_id in enumerate(employee_ID, start=1):
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
                     self.reporting_manager)

            # update emp details in excel sheet
            xl.write_data(emp_details, self.excel_file_path)
            c += 1

            # update emp details in database
            db.insert_into_table(self.database_name, self.table_name, self.table_columns, value)

    lp.log_out()

    return f"Emp Id's (not found) : {not_found}"


