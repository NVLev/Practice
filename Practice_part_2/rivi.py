import string

x = string.ascii_lowercase


uus_rivi = 'Mama myla ramu.'
sanakirja = dict()
for merkki in uus_rivi.lower():
    if merkki in x:
        if merkki in sanakirja:
            sanakirja[merkki] += 1
        else:
            sanakirja[merkki] = 1

summa = sum(sanakirja.values())
print(sanakirja)
print(summa)

for i, j in sanakirja.items():
    sanakirja[i] = round(j / summa, 3)

print(sanakirja)
tulos = sorted(sanakirja.items(), key=lambda item: (-item[1], item[0]))
# for i_avain, i_arvo in sanakirja.items():
#     print(i_avain, i_arvo, end='\n')
print(tulos)