def kysy(kysymys, viesti ='Virhe', yrit =2):
        while yrit:
            vastaus = input(kysymys).lower()
            if vastaus.lower() == 'jo':
                return 1
            elif vastaus.lower() == 'ei':
                return 0
            else:
                print(viesti)
            yrit -= 1

            print('Yrittien määrä on', yrit)






kysy('Oletko varma? Jo, ei ')
kysy('tiedosto? ')
kysy('Voi ei!  Miksi ei?')
