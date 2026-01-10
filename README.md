# Send-email-automation
A small automation tool using Python that will send a pre-written email
with attachments (e.g. monthly documents) via Gmail, without manually opening Gmail or composing
the email each time.

## What this does ?
This script automates the repetitive task of:
- Writing a standard email message
- Attaching multiple files from a folder
- Sending the email via Gmail SMTP

It is especially useful for sending recurring emails such as:
- Monthly documents
- Documents that follow a fixed format

The email content changes according to the month and year passed as command-line arguments.

## Current Features
- Sends email using Gmail SMTP
- Uses a predefined email template
- Automatically attaches **all files** from a specified directory
- Accepts `month` and `year` as command-line arguments
- Works without opening Gmail or manually attaching files

## How to run the script ?
1. Open a terminal and navigate to the project directory
2. For sending email, run:
    ```bash
    python app.py --write {month} {year}

## Demo
Video demonstration: TBA

## Future improvement
- Apply it as a Telegram bot