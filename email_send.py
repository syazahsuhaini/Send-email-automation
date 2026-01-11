import smtplib

from email_addr import *
from email_content import *

def send_process(month, year, text_content):

    # initialize connection to gmail
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(from_addr, password)

    try:
        msg, error_flag = message(month, year, text_content)

        if error_flag == 'N':
            # Provide some data to the sendmail function
            smtp.sendmail(from_addr=from_addr,
                        to_addrs=to_addr+cc_addr, msg=msg.as_string())
            print('Email sent successfully!')
        else:
            print('Failed to send email due to lack of attachment.')
    except Exception as e:
        print('Failed to send email:', e)


    smtp.quit() 

    return error_flag