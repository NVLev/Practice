players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

joukko1 = [
    pelaaja['name']
    for pelaaja in players_dict.values()
    if pelaaja['team'] == 'A' and pelaaja['status'] == 'Rest'
]
print(joukko1)
print([pelaaja['name']
       for pelaaja in players_dict.values()
       if pelaaja['team'] == 'B' and pelaaja['status'] == 'Training'
       ])
print([pelaaja['name']
       for pelaaja in players_dict.values()
       if pelaaja['team'] == 'C' and pelaaja['status'] == 'Travel'
       ])
