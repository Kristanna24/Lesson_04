# Задача_2
my_list = []
list = [int(i) for i in input('Введите список чисел, через пробел: ').split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (my_list.append(list[i]))

print(f'Исходный список:  {list}')
print(f'Список, элементы которого больше предыдущего: {my_list}')

# Задача_3
my_list = [n for n in range(20, 240) if n % 20 == 0 or n % 21 == 0]
print('Список чисел кратных 20 или 21 в диапазоне от 20 до 240: ', my_list)

# Задача_4
my_list_1 = [2, 9, 11, 24, 2, 11]
print('Введите элементы списка: ', my_list_1)
my_list_2 = [i for i in my_list_1 if my_list_1.count(i) == 1]
print('Элементы списка, не имеющие повторений: ', my_list_2)

# Задача_5
from functools import reduce

new_list = [i for i in range(100, 1001, 2)]
print(f'Список четных чисел в диапазоне от 100 до 1000: {new_list}')
print('Произведение всех элементов списка: ', reduce(lambda x, y: x * y, new_list))

# Задача_7

from math import factorial

def fact(n):
    for i in range(n):
        print(i+1, end='! = ')
        yield factorial(i+1)

x = int(input('Введите число, для вычисления факториала: '))
for el in fact(x):
    print(el)