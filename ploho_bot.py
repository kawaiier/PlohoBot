import os
from dotenv import load_dotenv, find_dotenv
from telebot import types, TeleBot

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")
DESTINATION_CHANNEL = os.getenv("CHANNEL")
GATEWAY_ACCOUNT_TAG = os.getenv("GATEWAY_ACCOUNT_TAG")


bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        "Привет! Пойдешь сегодня в Плохо?\n"
        f"Присылай мне текст для публикации в {GATEWAY_ACCOUNT_TAG}",
    )


@bot.message_handler(commands=["help"])
def send_help(message: types.Message) -> None:
    bot.send_message(
        message.chat.id, f"Присылай мне текст для публикации в {GATEWAY_ACCOUNT_TAG}"
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message: types.Message) -> None:
    bot.send_message(DESTINATION_CHANNEL, message.text)


@bot.message_handler(content_types=["photo"])
def echo_photo(message: types.Message) -> None:
    bot.send_photo(DESTINATION_CHANNEL, message.photo[0].file_id)


def main() -> None:
    bot.infinity_polling()


if __name__ == "__main__":
    main()
