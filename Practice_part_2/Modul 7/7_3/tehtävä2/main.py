import random

def create_random_list():
    return [random.choice(merkki) for _ in range(10)]


def create_dict(lista):
    uus_dict = dict()
    for i, nimi in enumerate(lista):
        uus_dict[i] = nimi
    return uus_dict


merkki = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

lista_merkki_1 = create_random_list()
lista_merkki_2 = create_random_list()
uus_dict_1 = create_dict(lista_merkki_1)
uus_dict_2 = create_dict(lista_merkki_2)
print(uus_dict_1)
print(uus_dict_2)





