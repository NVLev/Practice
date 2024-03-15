ip_address = "{0}.{1}.{2}.{3}"
count = 0
numbers = []
while count < 4:
    new_number = int(input("Syötä numero: "))
    if 0 <= new_number <= 255:
        numbers.append(new_number)
        count += 1
    else:
        print('Virhe!')

print(ip_address.format(*numbers))
