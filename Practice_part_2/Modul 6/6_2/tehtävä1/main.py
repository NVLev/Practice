small_storage = {

'гвозди': 5000,

'шурупы': 3040,

'саморезы': 2000
}

big_storage = {

'доски': 1000,

'балки': 150,

'рейки': 600
}
big_storage.update(small_storage)
print(big_storage)
item = input('Syötä item: ')


if big_storage.get(item, None):
    print(big_storage[item])

else:
    print('Virhe')