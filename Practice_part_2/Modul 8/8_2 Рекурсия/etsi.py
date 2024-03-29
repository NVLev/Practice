# Задача 3. Поиск элемента
# Когда мы работаем с большой многоуровневой структурой, нам нередко необходимо пройтись по ней и найти нужный элемент. Для этого в программировании используются специальные алгоритмы поиска.
#
# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение
# этого ключа на экран. В качестве примера можно использовать такой словарь:
#
site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}
# Пример 1:
# Искомый ключ: h2
# Значение: Здесь будет мой заголовок
# Пример 2:
# Искомый ключ: abc
# Такого ключа в структуре сайта нет.

def etsi_avain(rakenne, avain):
    if avain in rakenne:
        return rakenne[avain]
    for sub_rakenne in rakenne.values():
        if isinstance(sub_rakenne, dict):
            tulos = etsi_avain(sub_rakenne, avain)
            if tulos:
                break
    else:
        tulos = None
    return tulos

uusi_avain = input('Mitä avaimen etsitään? ')
arvo = etsi_avain(site, uusi_avain)
if arvo:
    print(arvo)
else:
    print('Nolla')
