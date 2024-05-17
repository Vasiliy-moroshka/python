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

