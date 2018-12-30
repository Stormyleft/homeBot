# -*- coding: utf-8 -*-
"""
Телеграм бот
Отправляет тестовое сообщение определенному пользователю
"""

# Импорт библиотек
import telebot
from telebot import apihelper

# Импорт файлов
import constants

# Настройки
token = constants.token_Nick420
apihelper.proxy = {'https': 'https://{}'.format(constants.proxy)}

# Токен
bot = telebot.TeleBot(token)

# Отправить сообщение "Updated"
bot.send_message(119245728, "test")

# End
