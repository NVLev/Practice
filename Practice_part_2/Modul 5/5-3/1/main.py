sano1 = input('Ensimmäinen sano: ')
sano2 = input('Kahden sano: ')
sano3 = input('Kolmen sano: ')
teksti = input('syötä teksti: ')
laskuri = 0
sano_lista = teksti.split()
for sano in sano_lista:
    if sano == sano1 or sano == sano2 or sano == sano3:
        laskuri += 1
print(laskuri)
