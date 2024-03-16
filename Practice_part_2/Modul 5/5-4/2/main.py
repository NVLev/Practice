polku = input('Tiedostopolku: ')
levy = input('Levy: ')
muoto  = input('Tiedostomuoto: ')
if not polku.endswith(muoto):
    print('Virhe! Muoto on varassa!')
elif not polku.startswith(levy):
    print('Virhe! Levy on varassa!')
else:
    print('Tiedostopolku:', polku)
