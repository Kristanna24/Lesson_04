# Задача_6
from itertools import count
print('Итератор, генерирующий целые числа, начиная с указанного')
n = int(input('Введите цифру от 0 до 9: '))
for el in count(n):
    if el > 20:
        break
    else:
        print(el)

from itertools import cycle
print('Итератор, повторяющий элементы некоторого списка, определенного заранее')
list_1 = [5, 7, 9, 2, 4, 6, 8, 1, 3]
for x, y in enumerate(cycle(list_1)):
    print(y, end=' ')
    if x > 50:
        print()
        break