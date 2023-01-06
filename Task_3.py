# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

print('Введите количество чисел для заполнения списка: ')
num = int(input())


sum_num = 0
list_num = []

for i in range(1, num + 1):
    res = round((1 + 1/ i) ** i)
    list_num.append(res)
    sum_num += res

print(f'Сумма чисел в списке: {sum_num}')