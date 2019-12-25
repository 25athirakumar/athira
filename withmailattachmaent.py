import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587                                 
from_address = "athira.1802023@srec.ac.in"             
from_password = "srec1234"    
to_address = "kathira052000@gmail.com"                 
subject = "test"              
mail_body = "hello attached file"
 
msg = MIMEMultipart()
msg['Subject'] =  subject
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
file = r"C:\Users\HP\Desktop\python1\for110.py"  
part = MIMEBase('application', "octet-stream")
part.set_payload(open(file, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
msg.attach(part)
 
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())

try:
    server.sendmail(from_address, to_address, msg.as_string())
    print ('email sent')
except:
    print ('error sending mail')

server.quit()

