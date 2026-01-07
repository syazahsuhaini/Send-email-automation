# importing requireed modules
from email.mime.text import MIMEText
#from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication  # for non text
from email.mime.multipart import MIMEMultipart
import smtplib

from data_path import *

# initialize connection to our
# email server, we will use gmail here
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

# Login with your email and password
#smtp.login('nuudii10@gmail.com', '4dXC.F9_m!Ac3iL')
#smtp.login('syazasuhaini@gmail.com', ':jAS4Ue-6UVBqtD')
smtp.login('syazasuhaini@gmail.com', 'bpjy intr lnmz ukri')


# send our email message 'msg'
def message(subject, text, attachment):

    # build message contents
    msg = MIMEMultipart()

    # Email headers (what recipient sees)
    msg['Subject'] = subject  
    msg['From'] = 'syazasuhaini@gmail.com'
    msg['To'] = "nuudii10@gmail.com"


    # add the content you want to send
    # Add text contents
    msg.attach(MIMEText(text))  

    # Check if we have anything
    # given in the attachment parameter
    if attachment is not None:

        # get the attachment from the directory
        files = []

        for f in timesheet_dir.iterdir():
            if f.is_file() and not f.name.startswith('.'):
                files.append(f)
        
        for one_attachment in files:
            with open(one_attachment, 'rb') as f:
              
                # Read in the attachment
                # using MIMEApplication
                file = MIMEApplication(
                    f.read(),
                    name=one_attachment.name
                )
            
            # At last, Add the attachment to our message object
            msg.attach(file)

    return msg

# Call the message function
msg = message("Test",
              "Hi there!",
              timesheet_dir)

# Make a list of emails, where you wanna send mail
to = ["nuudii10@gmail.com"]

try:
    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr="",
                to_addrs=to, msg=msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Failed to send email:", e)

 # Finally, don't forget to close the connection
smtp.quit() 