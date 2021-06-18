even_nums = 0
odd_nums = 0

num = int(input('Введите натуральное число: '))

while True:
    if num % 10 % 2:
        odd_nums += 1
    else:
        even_nums += 1

    num //= 10

    if not num:
        break

print(f'четных {even_nums} нечетных {odd_nums}')
