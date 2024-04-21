from queue import LifoQueue
stack = LifoQueue()
teht = {1: 'сделать', 4: 'wash', 2: ['put', 'take']}
sort_teht = sorted(teht.items())
print(sort_teht)
stack.put(sort_teht)
print(stack.get())