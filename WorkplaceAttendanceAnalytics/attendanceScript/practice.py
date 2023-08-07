# import time
#
# from selenium.webdriver.common.by import By
#
# from pageobject.login_page import LoginPage
# from utilities import get_driver
#
# base_url = "https://app.keka.com/Account/Login"
# email = "schandra@msystechnologies.com"
# password = "SjcKekaCgs@999"
# driver = get_driver.get_web_driver()
# captchaIMG_path = "D:\\PythonProject\\AttendenceEntry\\captchaIMG"
#
# captcha_element_xpath = "//img[@id='imgCaptcha']"
#
# lp = LoginPage(driver)
# lp.setup(base_url)
# lp.enter_email(email)
# lp.click_on_submit_button()
# lp.click_on_keka_password_button()
# lp.enter_password(password)
# time.sleep(5)
# lp.click_on_login_button()
# lp.click_on_email()
# lp.click_on_login_submit_button()
#
# captcha_element = driver.find_element(By.XPATH, captcha_element_xpath)
# captcha_element.screenshot(captchaIMG_path+"\\captcha_img6.png")
#
#
# time.sleep(15)
#
#
# import pytesseract
# from PIL import Image, ImageFilter
#
#
# # Open the image file
# image_path = "D:\\Documents\\Captcha\\capcha.jpeg"
# image = Image.open(image_path)
#
# smooth_image = image.filter(ImageFilter.SMOOTH)
# smooth_image.save(image_path)
# resize = image.resize((100, 100))
# resize.save("D:\\PYTHON AUTOMATION PROJECT\\pythonProject\\AttendenceEntry\\captchaIMG\\captcha_img1.png")
#
# # Use Tesseract OCR to extract text from the image
# text = pytesseract.image_to_string(image)
#
# # Print the extracted text
# print(text)
#
#
# ## mail ##
# #
# import imaplib
# import email
# import re
#
# def get_otp(body):
#     # Define the pattern to search for OTP
#     pattern = r'OTP: (\d{6})'
#
#     # Search for the pattern in the body
#     match = re.search(pattern, body)
#
#     # Check if a match is found
#     if match:
#         # Extract the OTP from the match
#         otp = match.group(1)
#
#         # Print or do something with the extracted OTP
#         print("Extracted OTP:")
#         print(otp)
#     else:
#         print("No OTP found.")
#
# def get_email_body(msg):
#     if msg.is_multipart():
#         # Iterate over the email parts
#         for part in msg.walk():
#             # Check if the part is the text/plain part
#             if part.get_content_type() == 'text/plain':
#                 body = part.get_payload(decode=True).decode()
#                 print("Email Body:")
#                 print(body)
#                 break
#     else:
#         # The message is not multipart, so it's a simple text message
#         body = msg.get_payload(decode=True).decode()
#         print("Email Body:")
#         print(body)
#     get_otp(body)
#
#
# # Connect to the email server
# mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#
#
# # Log in to the email account
# mail.login('schandra@msystechnologies.com', 'buvggujdibavldqz')
#
# # Select the mailbox/folder
# mail.select('INBOX')
#
# # Search for the email message
# result, data = mail.search(None, 'SUBJECT "Your One-Time Password (OTP) for Secure Login"')
# print(data)
#
# # Get the unique identifier (UID) of the email
# email_uid = data[0].split()[-1]
#
# # Fetch the email message
# result, message_data = mail.fetch(email_uid, '(RFC822)')
#
# # print(message_data[0])
# # print(len(message_data))
# # for i in message_data:
# #     print(i)
#
# # Process and display the email message
# for response_part in message_data:
#     if isinstance(response_part, tuple):
#         msg = email.message_from_bytes(response_part[1])
#         # sender = msg['From']
#         # subject = msg['Subject']
#         # date = msg['Date']
#         # print(msg)
#
#         body = get_email_body(msg)  # Implement this function to extract the email body
#         # attachments = get_email_attachments(msg)  # Implement this function to extract attachments
#
#         # Do something with the email details (e.g., print, save, etc.)
#
#
# response_part = message_data[0]
# msg = email.message_from_bytes(response_part[1])
# body = get_email_body(msg)
#
# # Close the connection
# mail.close()
# mail.logout()
#
#
# # extract text from image
#
# import pytesseract
# from PIL import Image, ImageEnhance
#
#
# # Preprocess the image
# def preprocess_image(image_path):
#     # Open the image using PIL
#     image = Image.open(image_path)
#
#     # Convert the image to grayscale
#     gray_image = image.convert("L")
#
#     # Enhance the image (optional)
#     enhanced_image = ImageEnhance.Contrast(gray_image).enhance(2.0)  # Adjust the enhancement factor as needed
#
#     return enhanced_image
#
#
# # Perform OCR on the preprocessed image
# def perform_ocr(image):
#     # Set the Tesseract path if it's not in your system PATH
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Users\schandra\AppData\Local\Programs\Tesseract-OCR"
#
#     # Perform OCR using Tesseract
#     extracted_text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')
#
#     return extracted_text
#
#
# # Specify the path to your image
# image_path = "D:\\PYTHON AUTOMATION PROJECT\\pythonProject\\AttendenceEntry\\captchaIMG\\captcha_img.png"
#
# # Preprocess the image
# preprocessed_image = preprocess_image(image_path)
#
# # Perform OCR on the preprocessed image
# extracted_text = perform_ocr(preprocessed_image)
#
# # Print the extracted text
# print(extracted_text)
#
#
#
# Image process for ocr
import time
import cv2
import numpy as np

folder_img = "D:\\PythonProject\\AttendenceEntry\\captchaIMG\\"
image_path = folder_img+"captcha_img2.png"
new_image_path = folder_img+"new_img.png"

image = cv2.imread(image_path)
# Define the new width and height for the resized image
new_width = 280
new_height = 100

# Rescale the image to the new size
resized_image = cv2.resize(image, (new_width, new_height))

def process_image(image):
    # binarization
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold(gray_image, 235, 345, cv2.THRESH_BINARY)

    # Noise removing
    kernel = np.ones((2, 1), np.uint8)
    image = cv2.dilate(im_bw, kernel, iterations=1)
    kernel = np.ones((1, 2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    cv2.imwrite(new_image_path, image)

process_image(resized_image)

time.sleep(5)


from utilities import get_text_from_image

print(get_text_from_image.extract_text(new_image_path).strip())

# keras ocr

# import keras_ocr
# import matplotlib.pyplot as plt
#
# pipeline = keras_ocr.pipeline.Pipeline()
#
# # image_path = r"D:\PythonProject\AttendenceEntry\captchaIMG\captcha_img1.png"
# images = [keras_ocr.tools.read(img) for img in [new_image_path]]
#
# prediction_groups = pipeline.recognize(images)
# print(prediction_groups)

