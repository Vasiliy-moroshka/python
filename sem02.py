#  Цикл (for)

# for element in 1, 45, -2, "Ivan", True, False:  # Последовательно сохраняет в переменную element следующее значение
#     print(element, end=' ') # Функция end обьединяет каждый последующий вывод через пробел

# Функция (range) Работает самостоятельно. Цикл for перебирает значения, а функция range генерирует значения по заданным параметрам
# range(initial=0, end(обязательное), step=+1)

# print(*range(5)) # 0 1 2 3 4
# print(*range(2, 8, 2)) # 2 4 6  
# print(*range(5, 0, -1)) # 5 4 3 2 1
# print(*range(2, 7)) # 2 3 4 5 6

# from numpy import arange

# print(arange(5, 0, -0.5)) # [5.  4.5 4.  3.5 3.  2.5 2.  1.5 1.  0.5]

# for i in range(5):
#     print(i)


# Задача №9. 
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input("Введите число: "))

# i = 2
# result = 1
# while i <= n:
#     result = result * i
#     i += 1
# print(result)


# Задача №11.
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

# f(n) = f(n - 1) + f(n - 2)
# 0 1 1 2 3 5 8 13 21 34 
# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# i = 1
# while a0 < n:
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
#     i += 1
#     if a0 > n:
#         i = -1
# print(i)

# n = int(input("Введите число: "))
# a_next = 0
# a0 = 0
# a1 = 1
# i = 2
# while a_next < n: # a_next = n or a_next > n
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
#     i = i + 1
# if a_next > n:
#     i = -1
# print(i)


