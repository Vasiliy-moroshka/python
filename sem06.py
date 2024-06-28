# Задача №39.

# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

import random

def list_creation(a):
    list = []
    for i in range(0, a):
        list.append(random.randint(1, 10))
    # print(list_1)
    return list

def comparision(list_1, list_2):
    list = []
    for num in list_1:
        if num not in list_2:
            list.append(num)
    return list

n = int(input("Введите кол-во чисел списка N: "))
m = int(input("Введите кол-во чисел списка M: "))

list_1 = list_creation(n)
list_2 = list_creation(m)
list_3 = comparision(list_1, list_2)
print(list_1)
print(list_2)
print(list_3)
