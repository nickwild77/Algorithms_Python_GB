'''6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.'''

import random

nums = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {nums}')

min_index = 0
max_index = 0
step = 1
summ = 0

for i in nums:
    if nums[min_index] > i:
        min_index = nums.index(i)
    elif nums[max_index] < i:
        max_index = nums.index(i)

if max_index - min_index < 0:
    step = -1

for i in nums[min_index + step:max_index:step]:
    summ += i

print(
        f'Сумма элементов между минимальным ({nums[min_index]})',
        f'и максимальным ({nums[max_index]}) элементами: {summ}'
        )
