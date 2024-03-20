user_input = set(input("Введите строку: "))
symbols = set(".,;:!?")
print("Количество знаков пунктуации:", len(user_input.intersection(symbols)))