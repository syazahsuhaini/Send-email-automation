from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication  # for non text

from email_addr import *
#from email_text import *
from data_path import *

def message(month, year):

    msg = MIMEMultipart()

    # email headers
    msg['Subject'] = f'TIMESHEET: SYAZA HAZWANI BINTI SUHAINI {month.upper()} {year}'  
    msg['From'] = from_addr
    msg['To'] = to_addr

    text_content = (f'Dear Wilson/Kim/Rajesh,\n\n'
        f'Below I attached all the timesheets for {month.capitalize()} {year}.\n\n'
        f'Thank you.\n\nBest regards,\nSyaza\n019-3012070')

    # contents in the email
    # texts
    msg.attach(MIMEText(text_content)) 

    # attachments
    # get attachments from selected directory
    files = []

    for f in timesheet_dir.iterdir():
        if f.is_file() and not f.name.startswith('.') and f.name.startswith('SYAZA'):
            files.append(f)

    count_files = len(files)

    if count_files < 1:
        print('There is no files to send as attachments.')
    else:
        for attachment_content in files:
            with open(attachment_content, 'rb') as f:
                file = MIMEApplication(
                    f.read(),
                    name=attachment_content.name
                )
            msg.attach(file)

    return msg