import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from openpyxl import Workbook

service = Service(executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.implicitly_wait(20)

driver.get("https://app.keka.com/Account/Login")

driver.find_element(By.ID, "email").send_keys("******************")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.find_element(By.XPATH, "//div/p[text()='Keka Password']").click()

driver.find_element(By.ID, "password").send_keys("**************")

time.sleep(15)

driver.find_element(By.XPATH, "//button[text()='Login']").click()

driver.find_element(By.XPATH, "(//p[@class='verify-btn-content'])[1]").click()

time.sleep(15)

driver.find_element(By.XPATH, "//li/a/span[text()='Org']").click()

driver.find_element(By.XPATH, "//span[text()='Department']").click()


driver.find_element(By.XPATH, "//label[@for='departmentNameSelectAll']").click()

driver.find_element(By.ID, "locationName").click()

driver.find_element(By.XPATH, "//span[@title='MSys Bangalore']").click()

page_height_1 = driver.execute_script("return document.body.scrollHeight;")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    page_height_2 = driver.execute_script("return document.body.scrollHeight;")
    if page_height_2 == page_height_1:
        break
    else:
        page_height_1 = page_height_2

wb = Workbook()
wb['Sheet'].title = 'Emp Data'
ws = wb.active
ws.append(['NAME', 'EMP ID', 'DEPARTMENT', 'LOCATION', 'REPORTING MANAGER'])

employee_name_elements = driver.find_elements(By.XPATH, "//div[@class='employee-details']/div/h4")

employee_names = []
for emp_name_element in employee_name_elements:
    employee_names.append(emp_name_element.text)

for emp_name in employee_names:
    driver.find_element(By.XPATH, "//input[@placeholder='Search employees or actions (Ex: Apply Leave, Attendance Approvals)']").send_keys(emp_name)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button/div/a[@placement='right']").click()
    time.sleep(2)

    department_name = driver.find_element(By.XPATH, "//div[@class='data-bar single-line-bar']/div[2]/p").text

    emp_num = driver.find_element(By.XPATH, "//div[@class='data-bar single-line-bar']/div[5]/p").text

    reporting_manager = driver.find_element(By.XPATH, "//div[@class='data-bar single-line-bar']/div[4]/p").text

    emp_details = [emp_name, emp_num, department_name, 'Bangalore', reporting_manager]

    # print(emp_details)
    ws.append(emp_details)


wb.save("./Bng_emp_data.xlsx")


time.sleep(5)

driver.close()
