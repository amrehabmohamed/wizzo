from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WIZZO is Online!")

def main():
    updater = Updater('6698711490:AAG3dNO24IO5dComduagtUEBluSl7LzwyQw', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
