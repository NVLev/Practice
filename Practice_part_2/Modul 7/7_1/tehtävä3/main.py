import random

def change(nums):
    nums = list(nums)

    index = random.randint(0, 5)

    value = random.randint(100, 1000)

    nums[index] = value

    return nums, value


my_nums = (1, 2, 3, 4, 5)

new_nums, rand_val = change(my_nums)
new_nums = tuple(new_nums)

print(new_nums, rand_val)

new_nums, uus_rand_val = change(new_nums)
new_nums = tuple(new_nums)
rand_val += uus_rand_val



print(new_nums, rand_val)