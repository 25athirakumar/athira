import smtplib
TO = 'kathira052000@gmail.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'
# Gmail Sign In
gmail_sender = 'athira.1802023@srec.ac.in'
gmail_passwd = 'srec1234'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = '\r\n'.join(['TO: %s' % TO,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ('email sent')
except:
    print ('error sending mail')

server.quit()