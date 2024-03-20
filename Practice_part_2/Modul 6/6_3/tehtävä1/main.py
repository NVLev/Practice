tilaus = {'omena': 2,

          'banana': 3,

          'päärynä': 1,

          'vesimeloni': 10,

          'suklaa': 5}

incomes = {

    'omena': 5600.20,

    'appelsiini': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'päärynä': 1020.00,

    'persimmon': 310.00,
}
summa = 0
for nimi, value in tilaus.items():
    summa += incomes.get(nimi, 0) * value
    print(f'{nimi}n hinta  -', end=' ')
    print(incomes.get(nimi, 0))
print(summa)

