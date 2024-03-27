# сли в списке встретился словарь, то оставляем его.
#
# Если в списке встретилась строка, то из неё нужно сделать словарь и положить его в итоговый список, например “abc” → {“abc”: “abc”}.
#
# С числами нужно сделать то же самое, что и со строками.
#
# Всё остальное выкидываем из нашего списка.

def create_dict(tieto):
    if isinstance(tieto, dict):
        return tieto


    elif isinstance(tieto, (int, float, str)):
        template = dict()
        template[tieto] = tieto
        return template
    else:
        return None

def data_preparation(vanha_lista):
    uusi_lista = []
    for i_element in vanha_lista:
        uusi_element = create_dict(i_element)
        uusi_lista.append(uusi_element)

    return uusi_lista


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
data = data_preparation(data)

print(data)


