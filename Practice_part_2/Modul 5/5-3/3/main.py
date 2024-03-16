while True:
    onn_malli = input('Syötä malli: ')
    if '{name}' in onn_malli and '{age}' in onn_malli:
        break
    else:
        print('Virhe!')

nimi_lista = input('Ihmisten nimejen lista, pilkulla erotettu')
ik_str = input('Ikä listä: ')
ik_lista = [i_num for i_num in ik_str.split(',')]

for i_ihm in range(len(nimi_lista)):
    print(onn_malli.format(name=nimi_lista[i_ihm], age=ik_lista[i_ihm]))
