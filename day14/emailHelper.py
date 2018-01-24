import email.message
import smtplib
class emailHander:
	def __init__(self,userEmail='',password=''):
		self.password = password
		self.userEmail = userEmail
		self.smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		self.msg = email.message.Message()
	def set_user_email(self,userEmail):
		self.userEmail = userEmail
	def set_user_password(self,password):
		self.password = password
	def get_user_password(self):
		return self.password
	def get_user_email(self):
		return self.userEmail
	def set_recipient(self, recipient):
		self.recipient = recipient
	def login(self):
		self.smtpObj.ehlo()
		x = self.smtpObj.login(self.userEmail,self.password)
		return x
	def generate_email(self,subject,content):
		self.msg.add_header('Content-Type','text/html')
		self.msg['Subject'] = subject
		self.msg['From'] = self.userEmail
		self.msg['To'] = self.recipient
		self.msg.set_payload(content)
	def send_mail(self):
		self.smtpObj.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())
	def quit(self):
		self.smtpObj.quit()