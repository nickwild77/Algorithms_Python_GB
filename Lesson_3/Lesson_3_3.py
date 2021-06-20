'''3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы.'''

import random

nums = [random.randint(0, 99) for _ in range(10)]
print(f'Массив до изменения: {nums}')

max = nums[0]
min = nums[0]

for i in nums:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = nums.index(min)
max_index = nums.index(max)
nums[min_index], nums[max_index] = nums[max_index], nums[min_index]
print(f'Массив пасле изменения элементов {min_index} и {max_index}: {nums}')
