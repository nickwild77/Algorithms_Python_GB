def rev(x):
    x_ = x // 10

    if x_ == 0:
        return x

    return f'{x % 10}{rev(x_)}'


zero = ''

num = input('Введите число: ')

if num.startswith('0'):
    zero = '0'
print(f'{rev(int(num))}{zero}')
