rivi = input('Syötä rivi: ')
laskuri_pien = 0
laskuri_iso = 0
for i_merkki in rivi:
    if i_merkki.isupper():
        laskuri_pien += 1
    elif i_merkki.islower():
        laskuri_iso += 1
if laskuri_iso > laskuri_pien:
    print(rivi.lower())
else:
    print(rivi.upper())
