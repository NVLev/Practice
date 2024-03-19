num = int(input('Syötä numero: '))
tulos = dict()

for i in range(1, num + 1):
    tulos[i] = i ** 2
print(tulos)