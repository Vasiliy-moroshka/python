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

# import random

# def list_creation(a):
#     list = []
#     for i in range(0, a):
#         list.append(random.randint(1, 10))
#     # print(list_1)
#     return list

# def comparision(list_1, list_2):
#     list = []
#     for num in list_1:
#         if num not in list_2:
#             list.append(num)
#     return list

# n = int(input("Введите кол-во чисел списка N: "))
# m = int(input("Введите кол-во чисел списка M: "))

# list_1 = list_creation(n)
# list_2 = list_creation(m)
# list_3 = comparision(list_1, list_2)
# print(list_1)
# print(list_2)
# print(list_3)


# Задача №41.

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:           Ввод:
# 5                 5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:         Вывод:
#   0               2

# import random

# def list_creation(a):
#     list = []
#     for i in range(0, a):
#         list.append(random.randint(1, 10))
#     # print(list_1)
#     return list

# def count_elements(list):
#     count = 0
#     for i in range(len(list)):
#         if list[i] > list[i - 1] + list[(i + 1) % len(list)]:
#             count += 1
#     return count

# n = int(input("Введите кол-во чисел в массиве N: "))
# list_1 = list_creation(n)
# print(list_1)
# print(count_elements(list_1))
