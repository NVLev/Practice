rivi = input('Syötä rivi')
merkki_lista= list('.,;:!?')
merkki = [
    i
    for i in rivi
    if i in merkki_lista
]
print(set(merkki))
