kontakt_dict = {}
while True:

    print('Nyt puhelimen yhteystietoluettelo on -')
    if kontakt_dict:
        for i_nimi in kontakt_dict:
            print(i_nimi, kontakt_dict[i_nimi])
    else:
        print('<Tyhjä>')
    nimi = input('Syötä nimi: ')

    if nimi in kontakt_dict:
        print('Virhe. Nimi on jo yhteystietoluettelossa')
    else:
        puhel = int(input('Syötä puhelinumero: '))
        kontakt_dict[nimi] = puhel
