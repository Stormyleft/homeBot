#!/usr/bin/python
"""
Эхо бот
Отвечает сообщением на сообщение
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

# Обертки
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


# Запуск цикла
if __name__ == '__main__':
	bot.polling(none_stop = 'True')

# End
