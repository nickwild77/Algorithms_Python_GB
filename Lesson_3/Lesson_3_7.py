'''7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться.'''

import random

nums = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {nums}')

min_index_1 = 0
min_index_2 = 1

for i in nums:
    if nums[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = nums.index(i)
    elif nums[min_index_2] > i:
        min_index_2 = nums.index(i)

print(f'Два наименьших элемента: {nums[min_index_1]} и {nums[min_index_2]}')
