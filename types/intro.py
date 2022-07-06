# # Типы данных в питоне:
# 1. NoneType -> Ничего пустота
# 2. Boolean -> Правда или Ложь
# 3. Числовые типы данных:
#             a. integer(int()) ->  Целое число(1, 2)
#             b. float() -> Числа с плавающей точкой(-1.2, 100.200, 2.7)
#             с. complex() -> комплекстные числа(3+5i/j)
# 4. Списковые типы данных:
#         a. list(списоск)(массив) -> [1,2,3,True, None, "Hello"]
#         b. tuple(кортеж) -> (1,2,3,False)
#         c. range(1,3) -> range(1,2)
# 5. str() -> Строки: "Hello world", 'Salam 312'
# 6. set() -> Множества 
# 7. dict -> Словарь содержит данные в виде ключа: значения -> {1: 'one', 2: 'two'...}

# *************************************************************************************
# Mutable(изменяемые типы данных)
#     1. list()
#     2. set()
#     3. dict()
# Immutable(неизменяемые типы данных)
#     1. NoneType
#     2. boolean
#     3. int(), float(), complex()
#     4. str()
#     5. range()
#     6. tuple()
# **************************************************************************************
'''Стандартный вывод данных'''
"""
в питоне для вывода данных в терминал 
используется функция print()
"""
# print('Hello world')

"""
Стандартный ввод данных через терминал используется функция input()
"""
# a = input('Введите число:')
# print(a)

# # type() выводит тип данных
# print(type(a))

# b = int(input('Введите число номер2: '))
# print(b)
# print(type(b))

# print(a, b, 'Salam')

''' 
divmod(a, b) она выводит два числа первое число это 
результат целочисленного деления //"a" на "b" 
второе число это остаток от делления
''' 
# print(divmod(13, 5))
# print(12 // 5)
# print(13 % 5

#abs() - Выводит абсолютное значение числа
# print(abs(-5))
# print(abs(5))

# import math 

# a = 25 
# print(math.sqrt(a))
