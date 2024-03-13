tarkastus = 'аеоиыуэАОИЫУЭ'
text = input('Syötä teksti: ')
vowels = [i_vow for i_vow in text if i_vow in tarkastus]
print(vowels)
print(len(vowels))