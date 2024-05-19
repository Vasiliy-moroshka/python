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


# Задача №15.
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


# n = int(input("Введите количество арбузов: "))
# m = int(input("Введите массу 1-го арбуза: "))
# min_massa  = m
# max_massa = m
# for i in range(n - 1):
#     m = int(input(f"Введите массу {i + 2}-го арбуза: "))
#     if m < min_massa:
#         min_massa = m
#     elif max_massa < m:
#         max_massa = m
# print(min_massa, max_massa)


# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = int(input("Введите количество дней: "))
# count_max = 0
# count = 0

# for i in range(n):
#     temp = int(input(f"Введите температуру {i + 1}-го дня: "))
#     if temp > 0:
#         count += 1
#     else:
#         if count_max < count:
#             count_max = count
#         count = 0
# print(count_max)