import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

def EmailAttOnline():
    email_user = 'your@email.com'
    email_password = 'password'
    recipients = ['recepient@gmail.com' ]

    subject = 'Relatório diário do MCC - TODOS OS MCCs ONLINE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] =  ", ".join(recipients)
    msg['Subject'] = subject

    data_atual = date.today()

    #body = "Olá!\nSegue o relatório diário, em PDF, abaixo:\n "

    html = """\
    <html>
      <head><p><strong><font color="green">TODOS OS MCC(s) ESTÃO ONLINE!</strong></font><br>
      <img scr="https://i.imgur.com/4CVBKal.jpg"></p></head>
      <body>
        <strong><p><font size="5" color="green">Está tudo certo no momento!</font><br>
           Segue o relatório diário, em PDF, abaixo: <br>
            <a href="http://vilatec.com.br/">Evolution Vilatec</a>
        </p></strong>
      </body>
    </html>
    """

    # fp = open('online.jpg', 'rb')
    # msgImage = MIMEImage(fp.read())
    # fp.close()
    #
    # msgImage.add_header('Content-ID', '<online>')



    #part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')



    filename='status.png'
    attachment  =open(filename,'rb')

    part3 = MIMEBase('application','octet-stream')
    part3.set_payload((attachment).read())
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition',"attachment; filename= "+filename)

    #msg.attach(part1)
    #msg.attach(msgImage)
    msg.attach(part2)
    msg.attach(part3)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,recipients,text)
    server.quit()


def EmailAttOffline():
    email_user = 'yourg@email.com'
    email_password = 'xxxxx'
    recipients = [
        'recepient@gmail.com']
    subject = 'Relatório diário do MCC - HÁ MCC(s) OFFLINE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    data_atual = date.today()

    # body = "Olá!\nSegue o relatório diário, em PDF, abaixo:\n "

    html = """\
    <html>
      <head><p><strong><font color="red">HÁ MCC(s) OFFLINE!</strong></font><br>
      <img scr="https://i.imgur.com/4CVBKal.jpg"></p></head>
      <body>
        <strong><p><font size="5" color="red">Por favor, verifique o relatório!</font><br>
           Segue o relatório diário, em PDF, abaixo: <br>
            <a href="http://vilatec.com.br/">Evolution Vilatec</a>
        </p></strong>
      </body>
    </html>
    """

    # part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')

    filename = 'status.png'
    attachment = open(filename, 'rb')

    part3 = MIMEBase('application', 'octet-stream')
    part3.set_payload((attachment).read())
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition', "attachment; filename= " + filename)

    # msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, recipients, text)
    server.quit()


def EmailFicouOn():
    email_user = 'your@email.com'
    email_password = 'password'
    recipients = [
        'recepient@gmail.com']
    subject = 'MCC ONLINE NOVAMENTE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    data_atual = date.today()

    # body = "Olá!\nSegue o relatório diário, em PDF, abaixo:\n "

    html = """\
        <html>
          <head><p><strong><font color="green">Algum MCC ficou ONLINE!!</strong></font><br>
          <img scr="https://i.imgur.com/4CVBKal.jpg"></p></head>
          <body>
            <strong><p><font size="5" color="green">Algum MCC retornou a funcionar normalmente!</font><br>
               Segue o relatório, em PNG, abaixo: <br>
                <a href="http://vilatec.com.br/">Evolution Vilatec</a>
            </p></strong>
          </body>
        </html>
        """

    # part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')

    filename = 'status.png'
    attachment = open(filename, 'rb')

    part3 = MIMEBase('application', 'octet-stream')
    part3.set_payload((attachment).read())
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition', "attachment; filename= " + filename)

    # msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, recipients, text)
    server.quit()

def EmailFicouOff():
    email_user = 'your@email.com'
    email_password = 'password'
    recipients = [
        'recepient@gmail.com']
    subject = 'MCC OFFLINE!'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    data_atual = date.today()

    # body = "Olá!\nSegue o relatório diário, em PDF, abaixo:\n "

    html = """\
        <html>
          <head><p><strong><font color="red">Algum MCC ficou OFFLINE!!</strong></font><br>
          <img scr="https://i.imgur.com/4CVBKal.jpg"></p></head>
          <body>
            <strong><p><font size="5" color="green">Por favor, verifique no relatório abaixo o que ocorreu!</font><br>
               Segue o relatório, em PNG, abaixo: <br>
                <a href="http://vilatec.com.br/">Evolution Vilatec</a>
            </p></strong>
          </body>
        </html>
        """

    # part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')

    filename = 'status.png'
    attachment = open(filename, 'rb')

    part3 = MIMEBase('application', 'octet-stream')
    part3.set_payload((attachment).read())
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition', "attachment; filename= " + filename)

    # msg.attach(part1)
    msg.attach(part2)
    msg.attach(part3)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, recipients, text)
    server.quit()
