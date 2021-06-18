while True:
    operation = input('Выберете операцию: [0 - Завершить], '
                      '[ + Сложить] [ - Вычесть], [ * Умножить], [ / Делить]: ')
    if operation == '0':
        break
    nums_1 = float(input('Введите первое число: '))
    nums_2 = float(input('Введите второе число: '))

    if operation == '+':
        result = nums_1 + nums_2
    elif operation == '-':
        result = nums_1 - nums_2
    elif operation == '*':
        result = nums_1 * nums_2
    elif operation == '/':
        if nums_2 == 0:
            print('Деление на ноль запрещено')
            continue
        result = nums_1 / nums_2
    else:
        print('Операция невозможна')
        continue

    print(f'{nums_1} {operation} {nums_2} = {result}')