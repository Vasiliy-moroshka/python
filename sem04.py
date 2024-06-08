# # dict(dictionary) - словарь
# # key: value

# data = {"Ivan" : 27, "Petr": 31, "Alina": 18, "Egor": 23, "Anna": 45, "Vladimir": 60, "Maria": 19}
# # print(data.keys())
# # print(data.values())
# # print(data.items())

# # #  Это всё разные типы данных! Возвращает не список!!!
# # print(type(data.keys()))   # Возврат всех ключей
# # print(type(data.values())) # Возврат всех значений
# # print(type(data.items()))  # Возврат коллекция данных, которая содержит кортеж
# # # Кортеж состоит из двух значений (ключ, значение)

# # for i in data.keys(): # == for i in data:
# #     print(i)

# # data["Ivan"] = 35
# # print(data)

# data = {"Ivan" : 27, "Petr": 31, "Alina": 18, "Egor": 23, "Anna": 45, "Ivan": 20, "Ivan": 7}
# print(data)
# # В словарях ошибки при повторениях ключей нет! Происходит перезапись значения!


# Задача №25.

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


data = input("Введите символы через пробел:" ).split()
print(data)

frequency_dict = {}
for element in data:
    if element not in frequency_dict:
        print(element, end=' ')
        frequency_dict[element] = 1
    else:
        print(f'{element}_{frequency_dict[element]}', end=' ')
        frequency_dict[element] += 1

