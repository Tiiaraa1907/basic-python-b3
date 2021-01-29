import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "dewi.mutiara606@gmail.com"
toaddr = ["tiiaraa19@gmail.com","falconsmanba@gmail.com"]
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "FINAL PROJECT"
 
body = "If you receive this message, this program is succeess"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "tiara19072003")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/