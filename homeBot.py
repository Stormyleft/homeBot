#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============
# Телеграм бот - умный дом
# ==============

# Импорт встроенных библиотек
import requests
import time

# Импорт библиотек
import telebot
from telebot import apihelper

# Импорт файлов
import constants
import data

# Настройки
token = constants.token_Nick420
apihelper.proxy = {'https': 'https://{}'.format(constants.proxy)}

# Функции
# Отправка клавиатуры меню
def switch_markup():
    menu_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    menu_markup.row('On', 'Off')
    menu_markup.row('Гараж')
    return menu_markup

# Токен
bot = telebot.TeleBot(token)

# Обертки
# Ответы на комманды
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, data.msg1, reply_markup=switch_markup())

# Ответ на текстовые сообщения
@bot.message_handler(func=lambda message: True,
                     content_types=['text'])
def default_command(message):
    if message.text == 'On' and message.from_user.id == constants.my_id:
        requests.get(data.url + data.on)
        bot.send_message(constants.my_id, "Is on!")
    elif message.text == 'Off' and message.from_user.id == constants.my_id:
        requests.get(data.url + data.off)
        bot.send_message(constants.my_id, "Is off!")
    elif message.text == 'Гараж':
        requests.get(data.url + data.g1)
        time.sleep(1)
        requests.get(data.url + data.g2)
        bot.send_message(constants.my_id, "Гараж в действии!")


# Запуск главного цикла
if __name__ == '__main__':
    bot.polling(none_stop = 'True')

"""
Все что после, не выполняется
"""
