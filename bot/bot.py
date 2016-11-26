# -*- coding: utf-8 -*-
from db import *
import telebot
import config

bot = telebot.TeleBot(config.token)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    start_text = 'hello\nsay /cmd'
    bot.send_message(message.chat.id, start_text)

@bot.message_handler(commands=['wrk', 'list', 'cmd'])
def handle_list(message):
    text = '/freelansim -- Работа с Фрилансим'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['freelansim', 'f'])
def handle_freelansim(message):
    cur = session.execute("SELECT * FROM job LIMIT 3")
    jobs = cur.fetchall()
    for job in jobs:
        output = str(job.id)+' '+job[4]+'\n   '+job[2]+'\n   '+job[3]
        bot.send_message(message.chat.id, output)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
