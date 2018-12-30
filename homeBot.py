# -*- coding: utf-8 -*-
# Телеграм бот - умный дом
# Импорт библиотек
import telebot
from telebot import apihelper

# Импорт файлов
import constants

# Настройки
token = constants.token_Nick420
apihelper.proxy = {'https': 'https://{}'.format(constants.proxy)}

mymsg = "Howdy, how are you doing?"

# Функции
# Отправка клавиатуры меню
def menu_markup():
    menu_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    menu_markup.row('shit')
    return menu_markup

# Токен
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
#	bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.from_user.id, mymsg, reply_markup=menu_markup())

@bot.message_handler(func=lambda message: True,
                     content_types=['text'])
def default_command(message):
    if message.text == 'shit':
        bot.send_message(message.chat.id, "получен")


bot.polling(none_stop = 'True', interval = 0)			    					# Запуск цикла

"""
Все что после, не выполняется
"""
