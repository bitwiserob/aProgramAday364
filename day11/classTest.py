from emailHelper import emailHandler
#create emailer object with a email and password
emailer = emailHandler('user email','user password')
#Select the sender email provider
#0 = gmail
#1 = outlook
#2 = yahoo
emailer.selectServer(0)
emailer.createSMTPobject()

#enter the email of a recipent
emailer.setRecipent('email')
#generate the email, args: subject line, email body
emailer.generateEmail('subject','body')
#sends the email
emailer.sendEmail()
#closes the connection to the email service
emailer.closeConnection()