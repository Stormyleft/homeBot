"""
Функции
"""

# Функция показывает все возможные методы у объекта
def all_meth(thing):
    print(type(thing))
    i = 0
    while i < len(dir(thing)):
        print(dir(thing)[i])
        i = i + 1
