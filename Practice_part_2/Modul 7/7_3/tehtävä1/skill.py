import random


def get_indexes(where_to_search, what_to_search):
    return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]


text = input("Введите текст: ")
print("Ответ:", " ".join(get_indexes(text, "~")))
