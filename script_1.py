# Задача_1
def premiya():
    a = float(input('Введите количество отработанных часов: '))
    b = float(input('Введите суммы оплаты труда за 1 час: '))
    c = float(input('Укажите размер премии - '))
    pay = a * b
    return pay + c
print(f'Размер заработной платы составил: {premiya() }')






