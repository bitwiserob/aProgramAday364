'''
Created on Jan 21, 2018

@author: Robert
'''
import smtplib

class emailHandler():
	def __init__(self,userEmail,password):
		self.emailServers = ['smtp.gmail.com','smtp-mail.outlook.com','smtp.mail.yahoo.com']
		self.userEmail = userEmail
		self.password = password
		self.serv = self.emailServers[0]
		self.smtpObj = ''
		self.recipientEmail = ''
		self.emailContent = ''

	def setPassword(self,password):
		self.password = password
	
	def setEmail(self,email):
		self.userEmail = email
	
	def selectServer(self,servNum):
		self.serv = self.emailServers[servNum]
	
	def createSMTPobject(self):
		self.smtpObj = smtplib.SMTP_SSL(self.serv,465)
		self.login()
	
	def login(self):
		self.smtpObj.ehlo()
		print(self.smtpObj.login(self.userEmail,self.password))
	
	def setRecipent(email):
		self.recipient = email
	
	def generateEmail(self,subject,content):
		self.emailContent = "Subject: {}.\n{}".format(subject, content)
	
	def sendEmail(self):
		self.smtpObj.sendmail(self.userEmail, self.recipientEmail, self.emailContent)
	
	def closeConnection():
		self.smtpObj.quit()

