import telebot
from telebot import types
import time
import threading

from scrapeinsite import scrapesite

bot = telebot.TeleBot('6470470662:AAFZNbPryFh6iseDwTtKZXwo1Awh54v3gJQ')





    # "Name": name,
    # "Payment": payment,
    # "Difficulty": difficulty,
    # "Proposals": proposals,
    # "Project Type": project_type,
    # "Description": opis



def message_sender(message):
    while True:
        item = scrapesite()
        bot.send_message(message.chat.id, f"""Название: {item['Name']}
Оплата: {item['Payment']}
Сложность: {item['Difficulty']}
Кол-во предложений: {item['Proposals']}
Тип проекта: {item['Project Type']}
Ссылка: {item['Url']}
Описание: {item['Description']}
        """)
        time.sleep(60)


@bot.message_handler(commands=['start', 'scrape'])
def start(message):
    x = threading.Thread(target=message_sender, args=(message,))
    x.start()


if __name__ == "__main__":
    bot.infinity_polling()