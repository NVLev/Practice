rivi = input('Syötä rivi: ')
rivi_set = set(rivi)
merkki = [i_merkki
          for i_merkki in rivi_set
          if '0' <= i_merkki <= '9'
          ]
print('Erilainen numerot rivissä ovat:', end=' ')
for i in merkki:
    print(i, end='')