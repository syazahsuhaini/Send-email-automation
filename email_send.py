import smtplib

from email_addr import *
from email_content import *

def send_process(month, year):

    # initialize connection to gmail
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(from_addr, password)

    try:
        msg = message(month, year)
        # Provide some data to the sendmail function!
        smtp.sendmail(from_addr=from_addr,
                    to_addrs=to_addr, msg=msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)


    smtp.quit() 

    return