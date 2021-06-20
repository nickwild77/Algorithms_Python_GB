'''5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random

nums = [random.randint(-99, 99) for _ in range(100)]
print(f'Массив: {nums}')

min_index = 0

for i in nums:
    if nums[min_index] > i:
        min_index = nums.index(i)

if nums[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент массива: {nums[min_index]}.',
            f'Находится на позиции {min_index} массива.')

