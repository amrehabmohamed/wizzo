import requests
import telegram.bot
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

def get_response(message):
    url = "https://api.huggingface.co/models/distilbert-base-uncased-squad2"
    params = {
        "question": message,
    }
    response = requests.get(url, params=params)
    return response.json()["answer"]

def main():
    bot = telegram.bot.Bot(token="YOUR_BOT_TOKEN")

    while True:
        update = bot.getUpdates()[-1]
        message = update.message.text

        response = get_response(message)

        bot.sendMessage(chat_id=update.message.chat_id, text=response)

if __name__ == "__main__":
    main()
