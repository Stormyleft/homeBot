"""
Функции
"""

import ast              # ast.literal_eval()

# from func import str_to_dict, print_dict				# перевод сообщения
# 	print_dict(str_to_dict(str(message)))

def log_wr(message):
    p = r"/Документы/Разработка/TranserfingBot/log.txt"
    f = open(p, 'r')
    s = str(message)
    if f == '':
        f.close()
        f = open(p, 'w', encoding='utf-8')
        n = '[' + s + ']'
    else:
        r = f.read()
        f.close()
        f = open(p, 'a', encoding='utf-8')
        n = r[:-1] + ', ' + s + ']'
    f.write(n)
    f.close()

# Строка в Солварь
def str_to_dict(param):
    return ast.literal_eval(param)


def print_dict(dictionary):
    """
    Функция отображает содержимое словаря
    в удобном для чтения виде (кроме None)
    """
        for i in dictionary:                               # i - Key
            j = dictionary.get(i)                          # j - value
            if j != None:                               # Пропуск пустых значений
                if type(j) == dict:                 # Проверка j на Dict
                    first = True                           # Начало счетчика
                    for x in j:
                        y = j.get(x)
                        if y != None:                   # Пропуск пустых значени
                            if first:
                                print(i, ':', x, ':', y)
                                first = False
                            else:
                                print(' ' * len(i), ' ', x, ':', y)
                else:
                    print(i, ':', j)


def good_dict(dictionary):
    """
    Функция возвращает содержимое словаря в удобном для чтения виде.
    В формате String (кроме None).
    """
    string = ''
    for i in dictionary:                                # i - Key
        j = dictionary.get(i)                           # j - value
        if j != None:                                   # Пропуск пустых значений
            string = string + str(i) + ' : '
            if type(j) == dict:                         # Если Value словарь
                first = True                              # Начало счетчика
                for x in j:                                 # x - Key
                    y = j.get(x)                            # y - value
                    if y != None:                           # Пропуск пустых значени
                        if first:
                            string = string + str(x) + ' : ' + str(y) + '\n'
                            first = False
                        else:
                            string = string + (' ' * len(i)) + '   ' + str(x) + ' : ' + str(y) + '\n'
            else:
                string = string + str(j) + '\n'
    return string


"""
a = {'content_type': 'text', 'message_id': 361, 'from_user': {'id': 119245728, 'first_name': 'Nicholas', 'username': 'Stormyleft', 'last_name': 'Bojgua', 'language_code': 'ru-IE'}, 'date': 1506638417, 'chat': {'type': 'private', 'last_name': 'Bojgua', 'first_name': 'Nicholas', 'username': 'Stormyleft', 'id': 119245728, 'title': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None}, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'text': 'hi', 'entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None}
b = {}
print_dictionary(a)
"""
