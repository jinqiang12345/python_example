import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['jinqiang@ygsoft.com']

message = MIMEText('python test mail', 'plain', 'utf-8')
message['From'] = Header("runoob", 'utf-8')
message['To'] = Header("test", 'utf-8')

subject = 'Python SMTP mail test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("success")
except smtplib.SMTPException:
    print("Error")