import smtplib
import feedparser
import sys
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=us")
feed_title = feed['feed']['title']
feed_entries = feed.entries
artCout = 0
gmailPassword = sys.argv[1]
gmailAddress = sys.argv[0]
emailString = ''
for i in feed_entries:
    if artCout <= 11:
        emailString += i['title'] + '\n'
        emailString += i['published'] + '\n'
        emailString += i['link'] + '\n'
        emailString += '\n'
        artCout += 1
    else:
        break


def login(email, password):
    smtpObj.ehlo()
    print(smtpObj.login(email, password))
def sendEmail(senderEmail, recipient,content):
    sendmailStatus = smtpObj.sendmail(senderEmail, recipient, content)
    print(sendmailStatus)
login(gmailAddress, gmailPassword)
sendEmail(gmailAddress, gmailAddress, emailString)
smtpObj.quit()