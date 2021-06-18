n = int(input("Введите количество суммируемых элементов: "))
count = 1
summ = 0

for i in range(n):
    summ += count
    count /= -2
print(summ)
