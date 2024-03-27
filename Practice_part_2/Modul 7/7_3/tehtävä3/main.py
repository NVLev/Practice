def data_tarkastus(x):
    if isinstance(x, str):
        return 'str'
    elif isinstance(x, list):
        return list
    elif isinstance(x, dict):
        return dict
    elif isinstance(x, tuple):
        return tuple

def final(lista):
    final = []
    for i, nimi in enumerate(lista):
        if i % 2 == 0:
            final.append(nimi)
    return final

data = input('data')
tarkastus = data_tarkastus(data)
if tarkastus == 'str' or tarkastus == 'tuple':
    data_lista = list(data)
elif tarkastus == 'list':
    data_lista = list(data.join())
elif tarkastus == 'dict':
    data_lista = list(data.values())
#elif tarkastus == tuple:


final_data = final(data_lista)

print(final_data)
