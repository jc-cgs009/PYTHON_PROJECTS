import imaplib
import email
import re


class GetOtpFromEmail:
    imap_server = 'imap.gmail.com'
    imap_host = 993
    email = 'schandra@msystechnologies.com'
    password = 'dorgscrahzpuchxk'

    def __init__(self):
        self.mail = imaplib.IMAP4_SSL(self.imap_server, self.imap_host)

    def __get_otp(self, body):
        # Define the pattern to search for OTP
        pattern = r'OTP: (\d{6})'

        # Search for the pattern in the body
        match = re.search(pattern, body)

        # Check if a match is found
        if match:
            # Extract the OTP from the match
            otp = match.group(1)
            return otp
        else:
            return False

    def __get_email_body(self, msg):
        if msg.is_multipart():
            # Iterate over the email parts
            for part in msg.walk():
                # Check if the part is the text/plain part
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            # The message is not multipart, so it's a simple text message
            body = msg.get_payload(decode=True).decode()

        return self.__get_otp(body)

    def log_in_to_email_account(self):
        self.mail.login(self.email, self.password)

    def get_latest_uid_of_the_searched_email(self):
        self.mail.select('INBOX')
        result, data = self.mail.search(None, 'SUBJECT "Your One-Time Password (OTP) for Secure Login"')
        email_uid = data[0].split()[-1]
        return email_uid

    def fetch_email_message(self, email_uid):
        result, message_data = self.mail.fetch(email_uid, '(RFC822)')
        if result == 'OK':
            return message_data
        else:
            return False

    def get_OTP(self, message_data):
        response_part = message_data[0]
        msg = email.message_from_bytes(response_part[1])
        self.mail.logout()
        return self.__get_email_body(msg)




