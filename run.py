import smtplib
import housieticket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "17131a1249@gvpce.ac.in"
you = "ksgsarma5@gmail.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

html = housieticket.get_ticket(2)
part2 = MIMEText(html, 'html')

msg.attach(part2)

s = smtplib.SMTP('smtp.gmail.com: 587')
 
s.starttls()
 
s.login(msg['From'], "****************")
 
s.sendmail(me, you, msg.as_string())
print("Mails Sent")
s.quit()

































