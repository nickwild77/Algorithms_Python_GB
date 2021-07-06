"""1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python и разрядность
вашей ОС."""


import sys
import random
import platform

matrix = []

for i in range(15):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(15)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d}' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d}' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы:', min_list[0])


def show_size_of():
    """Возвращает размер переменных в байтах"""
    sum_size = 0
    sum_size += sys.getsizeof(matrix)
    sum_size += sys.getsizeof(min_list)
    sum_size += sys.getsizeof(i)
    sum_size += sys.getsizeof(string)
    sum_size += sys.getsizeof(j)

    print(f'Переменные занимают: {sum_size} байт')


def show_platform_and_architecture():
    """Возвращает платформу и разрядность. В моем случае
    macOS-10.16-x86_64-i386-64bit"""
    return print(platform.platform())


show_size_of()
show_platform_and_architecture()
