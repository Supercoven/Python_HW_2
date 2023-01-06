print('Введите числа N для определения границ списка: ')
print('Введите число N: ')
n = int(input())

list_num = []
mult_num = 0

for i in range(-n, n):
    list_num.append(randint(-n, n)) #пока просто пробовал напечатать список, VSC выдал что такой функции
    # randint или random нет на свете, тогда не знаю как случайными числами заполнить

print(list_num)