# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, 
# а некоторые – гербом. Ваша задача - определить минимальное количество 
# монеток, которые нужно перевернуть, чтобы все монетки лежали 
# одной и той же стороной вверх.

# Входные данные:

# На вход программе подается список coins, 
# где coins[i] равно 0, если i-я монетка лежит 
# гербом вверх, и равно 1, если i-я монетка лежит 
# решкой вверх. Размер списка не превышает 1000 элементов.
# Выходные данные:

# Программа должна вывести одно целое число - минимальное 
# количество монеток, которые нужно перевернуть.

# Пример использования На входе: coins = [0, 1, 0, 1, 1, 0]
# На выходе: 3

# coins = [0, 1, 0, 1, 1, 0]

# heads = 0
# tails = 0

# for coin in coins:
#     if coin == 0:
#         heads += 1
#     else:
#         tails += 1

# if heads > tails:
#     print(tails)
# else:
#     print(heads)