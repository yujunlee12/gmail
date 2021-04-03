import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp=smtplib.SMTP("smtp.gmail.com",587)
smtp.ehlo()
smtp.starttls()
smtp.login("yujunlee7862@gmail.com","dkgur3@@")

m="yujunlee7862@gmail.com"
y="yujunlee7862@gmail.com"
subject="hellow"
message="dd"
msg=MIMEText(message.encode('utf-8'),_subtype='plain',_charset='uft-8')
msg['subject']=Header(subject.encode('utf-8'),'utf-8')
msg['From']=m
msg['To']=y
smtp.sendmail(m, y, msg.as_string())
smtp.quit()
