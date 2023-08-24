from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Function to handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WIZZO is Online!")
    log_message(update.message.text)

# Function to handle all other messages
def handle_message(update, context):
    # Log the received message
    log_message(update.message.text)
    
    # Predefined replies
    replies = {
        "hello": "Hello from TheWizzoBot!",
        "how are you": "I'm just a bot, but I'm working fine!"
    }
    
    # Send the coded reply if available, otherwise send "Not available"
    response = replies.get(update.message.text.lower(), "Not available")
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Function to log received messages
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
