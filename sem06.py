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



# Задача №43.

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:          Вывод:
# 1 2 3 2 3        2

# import random

# def list_creation(a):
#     list = []
#     for i in range(0, a):
#         list.append(random.randint(1, 10))
#     # print(list_1)
#     return list

# def count_pairs(list):
#     count = 0
#     for i in range(len(list)):
#         for j in range(i + 1, len(list)):
#             if list[i] == list[j]:
#                 count += 1
#     return count

# n = int(input("Введите кол-во элементов списка N :"))
# list_1 = list_creation(n)
# print(list_1)
# print(count_pairs(list_1))


# Задача №45

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10**5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:                      Вывод:
# 300                        220 284

# k = 500

# def get_sum(n):

#     sum = 1
#     for element in range(2, n):
#         if n % element == 0:
#             sum += element
#     return sum

# def fill_arrays(k):

#     res = []
#     for n in range(1, k + 1):
#         if n not in res:
#             m = get_sum(n)
#             # n = get_sum(m)
#             if n == get_sum(m) and m != n:
#                 res.append(n)
#                 res.append(m)
#     return res

# print(fill_arrays(k))


# Задача №46

# def func(n):

#     res = [el for el in range(n)]
#     return res

# print(func(10))

# def func2(n):

#     for el in range(n):
#         yield el

# for el in func2(10):
#     print(el, end=' ')

