oppi_str = input('Syötä opiskelin tiedot (etunimi, sukunimi, kaupunki, opiskelupaikka, arvosanat) '
             'välilyönnin kanssa: ')
oppi_lista = oppi_str.split()
oppi = dict()
oppi['Etunimi'] = oppi_lista[0]
oppi['Sukunimi'] = oppi_lista[1]
oppi['Kaupunki'] = oppi_lista[2]
oppi['Opiskelupaikka'] = oppi_lista[3]
oppi['Arvosanat'] = []

for i_arvo in oppi_lista[4:]:
    oppi['Arvosanat'].append(int(i_arvo))

for i_tieto in oppi:
    (print(i_tieto, '-', oppi[i_tieto]))
