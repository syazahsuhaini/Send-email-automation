# Send email automation
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

# Telegram bot integration for send email automation (Local)
This project also includes a Telegram bot interface that allows triggering the email
automation using Telegram commands.

The bot is **not hosted on a server**. It only works when the script is running on
my local machine. This feature was implemented mainly for learning purposes and
experimentation with bot automation.

## How to use the bot ?
1. Open a terminal and navigate to the project directory
2. Run the Telegram bot script locally:
    ```bash
    python telegram_bot.py
3. Open telegram and go to the bot then send:
    ```bash
    To start the bot : /start
    To send email    : /send <month> <year>

## Demo
Video demonstration: TBA

## Future improvement
- ~~Apply it as a Telegram bot~~
- Host the bot on a cloud server for 24/7 availability
- Add config.json file to store sensitive/important information properly
- Add scheduling by using Windows Task Scheduler or Python schedule library
- Telegram bot upgrade:
    - /status → shows last sent email
    - /help → explains commands
    - /preview → shows email content before sending