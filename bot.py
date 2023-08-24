from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WIZZO is Online!")
    log_message(update.message.text)

def handle_message(update, context):
    # Log the received message
    log_message(update.message.text)
    
    # Hardcoded replies
    message_text = update.message.text.lower()

    if "hello" in message_text or "hi" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hey there! WIZZO at your service. Ready to make things fly?")
    elif "how are you" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Always soaring high and ready to assist. What can WIZZO do for you today?")
    elif "who are you" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm WIZZO, your trusty wingman. Here to help you soar to new heights!")
    elif "thanks" in message_text or "thank you" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Anytime, partner! Remember, the sky's the limit with WIZZO by your side.")
    elif "help" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Of course! Just let me know what you need, and I'll help you take off.")
    elif "bye" in message_text or "goodbye" in message_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Safe travels! Remember, whenever you need to soar, WIZZO's here to help.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Not sure about that one, but I'm always here to help you fly high. Ask away!")

def log_message(message):
    with open("message_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def main():
    updater = Updater('6698711490:AAG3dNO24IO5dComduagtUEBluSl7LzwyQw', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
