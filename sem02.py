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