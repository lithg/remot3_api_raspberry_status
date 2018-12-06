import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

def EmailAttOnline():
    email_user = 'gclithg@gmail.com'
    email_password = 'Guixwq6206!'
    recipients = ['xxxx@xxx.com', 'example@email.com'] # list

    subject = 'TODOS OS MCCs ONLINE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] =  ", ".join(recipients)
    msg['Subject'] = subject

    data_atual = date.today()

    body = 'Gerado em: '
    msg.attach(MIMEText(body,'plain'))

    filename='status.png'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,recipients,text)
    server.quit()


def EmailAttOffline():
    email_user = 'gclithg@gmail.com'
    email_password = 'Guixwq6206!'
    recipients = ['xxxx@xxx.com', 'example@email.com'] # list

    subject = 'MCC(s) OFFLINE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] =  ", ".join(recipients)
    msg['Subject'] = subject
    data_atual = date.today()

    body = 'Há MCCs Offline'
    msg.attach(MIMEText(body,'plain'))

    filename='status.png'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,recipients,text)
    server.quit()
