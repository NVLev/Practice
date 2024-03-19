def histogram(string):
    merkki_kir = dict()
    for merkki in string:
        if merkki in merkki_kir:
            merkki_kir[merkki] += 1
        else:
            merkki_kir[merkki] = 1
    return merkki_kir


teksti = input('Syötä tekstti: ').lower()
hist = histogram(teksti)
for i_merkki in sorted(hist.keys()):
    print(i_merkki, ':', hist[i_merkki])

print('Suurin käyttötiheys on', max(hist.values()))