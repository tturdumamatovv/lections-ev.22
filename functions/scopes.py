# Области видимости и пространство имен

# Built-in (Встроенная) - print, len, man, int etc.
# Global (Глобальная) 
# Enclosed (Не локальная, nonelocal)
# local (Локальная область видимости)



# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element = 'q'
# print_list([1,2,3,4,5])
# print(element)


# a = 10 # global
# print # built-in
# def hello(): #golbal
#     a = 'hello world' # local
#     print(a, 'Local inside at func')

# hello()
# print(a, 'global')


# x = 'global'
# print(x, '1') # 1 global

# def enclosed():
#     x = 'elclosed'
#     def local():
#         x = 'local'
#         print(x, '3') # local
#     print(x, '2') # enclosed
#     local()
#     print(x, '4') # enclosed

# enclosed()
# print(x, '5') # global


# num = 10 
# def func(): 
#     def inner_func():
#         print(num)
#     inner_func()
# func()


# var = 100 #global variable
# def increment():
#     var = var + 1 #Try to update a global variable(using increment -> var += 1)

# increment()
# print(var)



# global -> Позволяет менять значение глобальной переменной в локальной области видимости.
# nonlocal -> Позволяет менять значение не локальной 
# переменной находясь в локальной области видимости.

# var = 100

# def increment():
#     global var 
#     var += 1 

# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)






# def counter():
#     num = 0 
#     def incrementer():
#         nonlocal num
#         num += 1 
#         return num
#     return incrementer

# c = counter()
# print(c) # <function counter.<locals>.incrementer at 0x7f5e36749790>
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3

# c = counter()
# print(c()) # 1 


# # print(len(dir(__builtins__)))
# print(abs(-15)) # стандартный вызов встроенной функции
# abs = 15 # Переопределяю встроенное имя abs в глобальный области
# del abs
# print(abs(-15))

# ===================================================================

# Дан список внутри которого список из трех
# чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5]] -> 6, 11 -> 11


# list_ = [[1,2,3], [3,3,5]]
# a = list_[0]
# b = list_[1]
# c = sum(a)
# d = sum(b)
# if c > d:
#     print(c)
# else:
#     print(d)


# list_ = [[1,2,3], [3,3,5], [5,6,5], [12,3,34]]
# sums = []
# for x in list_:
#     sums.append(sum(x))
# print(sums)
# print(max(sums))


# res = max([sum(x) for x in list_])
# print(res)

# __________________________________________________________

# alice = [13, 15, 38]
# john = [5, 15, 50]
# res = {'Alice': 1, 'John': 1}

# [33,66,10]
# [33,66,10] # 0 0

# [54,20,10]
# [54,35,15] # 1 2 


# alice = [13,15,38]
# john = [5,15,50]

# def compareScores(a, j):
#     score_a = 0
#     score_j = 0 
#     for i in range(0, len(a)):
#         if a[i] > j[0]:
#             score_a += 1
#         elif a[i] < j[0]:
#             score_j += 1
#         else:
#             pass
#     return {'Alice': score_a, 'John': score_j}

# print(compareScores(alice, john))
# print(compareScores([54, 20, 10],[10,35,15]))


# str_ = 'pythoniiist'
# dict_ = {key:str_.count(key) for key in str_}
# print(dict_)


