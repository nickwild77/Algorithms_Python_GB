'''4. Определить, какое число в массиве встречается чаще всего.'''

import random

nums = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {nums}')

max_index = 0
for i in nums:
    if nums.count(max_index) < nums.count(i):
        max_index = nums.index(i)

print(f'Число {nums[max_index]}, встречается {nums.count(max_index)} раза')
