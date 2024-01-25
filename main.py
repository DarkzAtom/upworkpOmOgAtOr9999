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


@bot.message_handler(commands=['start', 'scrape'])
def message_sender(message):
    while True:
        resultscrape = scrapesite()
        if resultscrape is not None and 'Name' in resultscrape:
            item = resultscrape
            bot.send_message(message.chat.id, f"""Название: {item['Name']}
    Оплата: {item['Payment']}
    Сложность: {item['Difficulty']}
    Кол-во предложений: {item['Proposals']}
    Тип проекта: {item['Project Type']}
    Ссылка: {item['Url']}
    Описание: {item['Description']}
            """)
        else:
            pass
        time.sleep(15)




if __name__ == "__main__":
    bot.infinity_polling()