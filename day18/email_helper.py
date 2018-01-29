import email.message
import smtplib


class EmailHandler:

    def __init__(self, user_email='', user_password=''):
        self.user_password = user_password
        self.user_email = user_email
        self.smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.msg = email.message.Message()

    def set_user_email(self, user_email):
        self.user_email = user_email

    def set_user_user_password(self, user_password):
        self.user_password = user_password

    def get_user_user_password(self):
        return self.user_password

    def get_user_email(self):
        return self.user_email

    def set_recipient(self, recipient):
        self.recipient = recipient

    def login(self):
        self.smtp_obj.ehlo()
        x = self.smtp_obj.login(self.user_email, self.user_password)
        return x

    def generate_email(self, subject, content):
        self.msg.add_header('Content-Type', 'text/html')
        self.msg['Subject'] = subject
        self.msg['From'] = self.user_email
        self.msg['To'] = self.recipient
        self.msg.set_payload(content)

    def send_mail(self):
        self.smtp_obj.sendmail(self.msg['From'], [self.msg['To']],
                              self.msg.as_string())

    def quit(self):
        self.smtp_obj.quit()
