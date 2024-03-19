def get_value(x):
    return x[1]

incomes = {

'apple': 5600.20,

'orange': 3500.45,

'banana': 5000.00,

'bergamot': 3700.56,

'durian': 5987.23,

'grapefruit': 300.40,

'peach': 10000.50,

'pear': 1020.00,

'persimmon': 310.00,
}
print(incomes)
print('Vuoden kokonaistulot on', sum(incomes.values()))


pien = None
pien_nimi = ''
for name, value in incomes.items():
    if pien is None or pien > value:
        pien = value
        pien_nimi = name


print(f'Pienin tulos on {pien_nimi}:ssa.  Se on {pien} rublia')

min_name, min_value = min(incomes.items(), key=get_value)
# При помощи функции и параметра key мы говорим пайтону как именно надо сравнивать между собой элементы
# Т.к. элементы записаны в таком виде - ('apple': 5600.20), а сравнивать мы хотим по значениям
# - то нам проосто надо брать для сравнения
# элементы под индексом 1 (если бы сравнивали по ключам, то индекс надо было бы заменить на 0)
print(min_name, min_value)
