# Задача №31.

# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# 0 1 1 2 3 5 8 13 21 34 55 89
# f(n) = f(n - 1) + f(n - 2)

# from datetime import datetime

# def f(n):
#     if n in (0, 1): # n == 0 or n == 1
#         return n
#     return f(n - 1) + f(n - 2)

# n = int(input("Введите номер: "))
# start_time = datetime.now()
# print(f(n))
# print(f'Время работы: {datetime.now() - start_time}')
# # O(2^n)
# # O(2^10) = 1024 операции

# a0 = 0
# a1 = 1
# start_time = datetime.now()
# for i in range(n):
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
# print(a0)
# print(f'Время работы: {datetime.now() - start_time}')
# # O(n) = 10 операций


# Задача №33.

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


marks = [int(i) for i in input("Введите оценки: ").split()]
print(*[min(marks) if i == max(marks) else i for i in marks])
# min(marks) - поиск минимального числа списка
# max(marks) - поиск максимального числа списка