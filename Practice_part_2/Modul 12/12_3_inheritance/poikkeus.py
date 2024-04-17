class Poikkeus(Exception):
    pass


class Omapoikkeus(Poikkeus):
    pass


def luoda(file):
    with open(file, 'w') as num:
        num.write('4 2\n3 6\n9 3')
    return file


def luoda_lista(file):
    with open(file, 'r') as tiedosto:
        for rivi in tiedosto:
            try:
                clear_line = rivi.rstrip()
                first, second = clear_line.split()
                if int(first) < int(second):
                    raise Poikkeus("нельзя делить большее на меньшее")

            except (ValueError, Poikkeus) as exc:
                print(exc, type(exc), first, second)

        return clear_line

# def jakaa(lista):
#     jakaa_lista = []
#     for i, j in enumerate(lista):
#         if i % 2 == 1:
#             jakaa_1 = j / j[i + 1]
#             jakaa_lista.append(jakaa_1)
#     return jakaa_lista


luoda('numero.txt')
uusi_lista = luoda_lista('numero.txt')
print(uusi_lista)
