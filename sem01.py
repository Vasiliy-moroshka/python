# Виды трансляции программного кода:
# 1. Компиляция (C#, C++, ...)
# 2. Интерпретация (Python, JavaScript, ...)

# C#:
# int n = 5; -> []

# Python:
# n = 5 -> class <'int'> -> []

# Оффтоп - всегда при вводе в терминал, мы вводим строку!

# name = input("Введите имя: ")  # type = str(string)
# print(name)

# name = input("Введите имя: ")
# age = input("Введите возраст: ")
# print(name, age)
# print(f"Привет, {name}! Тебе {age} лет.") # форматированный вывод / интерполяция строк

# name = "Sidor"
# print(type(name)) # <class 'str'>

# number = 123
# print(type(number)) # <class 'int'>

# float_number = 232.233
# print(type(float_number)) # <class 'float'>

# n = input("Введите число: ")
# print(type(n)) 

# Встроенные функции (int, float, str)
# print(int("234") + 6)
# print(int(3.99))
# print(int("234"))
# # print(int("23 4")) ValueError: invalid literal for int() with base 10: '23 4'
# print(float(56)) # 56.0
# print(str(455.56) * 2) # 455.56455.56 

# n = int(input("Введите 1-ое число: "))
# m = int(input("Введите 2-ое число: "))
# print(type(n))
# print(f'{n} + {m} = {n + m}')
# print(f'{n} - {m} = {n - m}')
# print(f'{n} * {m} = {n * m}')
# print(f'{n} : {m} = {n // m}(ост. {n % m})')
# print(f'{n} : {m} = {n / m}')
# print(f'{n}^{m} = {n ** m}')

# print(7 > 5)
# print(10 < 0)
# condition -> True or False

# Алгебка логики (Булевская логика) True(1) False(0)

# конъюнкция(логическое умножение) - and
# дизъюнкция(логическое сложение) - or
# отрицание(обратное значение) - not 

# print(7 > 5 and 10 < 0)
# #       1    *    0 = 0(False)
# print(1 > 2 or 5 > -1)
# #       0   +    1 = 1(True)
# print(3 > 2 or 5 > 2)
# #      1    +    1 = 1(True)
# print((3 > 2 or 5 > 3) and 2 < 0)
# #       1    +    1     *    0 = 0(False)



# Задача №1. Решение в группах

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input("Сколько за день проезжает машина: "))
m = int(input("Общее расстояние: "))
# # 750 : 700 = 1(ост. 50) + 1
# # 2100 : 700 = 3 (ост. 0) + 0
print((m + n - 1) // n)
# print(-12 % 5) # 15 - 12 = 3
# print(-14 % 6) # 18 - 14
# print(-7 % 3) # 9 - 7
