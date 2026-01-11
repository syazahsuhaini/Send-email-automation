# telegram interface

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

from email_text import *
from email_send import *
from secret import *

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # bot will reply with this text when you typed /start
    await update.message.reply_text(f'Hello! I\'m your email automation bot.\n'
                                    f'I can help you send send emails and attach your documents.\n\n'
                                    f'You can control me by sending these commands:\n\n'
                                    f'/send <month> <year> - send email with attachments\n'
                                    f'/help - for assistance on using this bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is help.')

async def send_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # context.args is list of arguments after the command
    if len(context.args) != 2:
        await update.message.reply_text('Usage: /send <month> <year>')

    # get the first and second arguments
    month = context.args[0]
    year = context.args[1]

    # validate the argument
    if not isinstance(month, str):
         await update.message.reply_text('Error: month must be string.')
         return
    elif not year.isdigit():
        await update.message.reply_text('Error: year must be number.')
        return

    text_content = text_template(month, year)
    error_flag = send_process(month, year, text_content)

    if error_flag == 'N':
        await update.message.reply_text('Email sent successfully!')
    else:
        await update.message.reply_text('Failed to send email due to lack of attachment.')

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    # register command
    # the /start in telegram, start function
    app.add_handler(CommandHandler('start', start_command))

    # Register the help command
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(CommandHandler('send', send_email))

    # this is printed on terminal
    print("Bot is running...")
    # run the bot
    app.run_polling()

if __name__ == "__main__":
    main()