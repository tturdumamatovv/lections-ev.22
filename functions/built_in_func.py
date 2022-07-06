# Встроенные функции 
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max()
# etc. 152 


# map()
# filter()
# lambda
# enumerate()


# Анонимные функции - lambda(такие же функции только без названия)
# Lambda функции могут принимать сколько угодно аргументов, но всегда возвращают 
# только одно выражение

# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_arg = lambda a, b: a + b
# print(sum_arg(1, 2))


# x = lambda a, b, c: a + b + c 
# print(x(5,6,7))


# def myFunc(n):
#     return lambda a : a * n

# my_doubler = myFunc(2)
# my_tripler = myFunc(3)

# print(my_doubler(11))
# print(my_doubler(22))
# print(my_tripler(11))
# print(my_tripler(22))


# ls = ['def', 'Ivan', 'john', '', ' ']
# new_list = sorted(ls, key=len)
# print(new_list)


#-----------------------------------------------------------------------------


# map(function, Iterable) -> применяет функцию к каждому элементу последовательности и возвращает 
# mapobject(итератор) с результатами


# Например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)
# result2 = list(map(len, list_of_words))
# print(result2)


# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)


# names = ['John', 'Jamie', 'Sansa', 'Tirion', 'Aibek']
# result = list(map(lambda x: f'Hello mr/mrs {x}',names))
# print(result)


# nums = [1,2,3,4,5]
# num2 = [100,200,300,400,500]
# # 100, 400, 900, 1600, 2500
# result = list(map(lambda x,y: x*y, nums, num2))
# print(result)


# dict_ = {1: 2, 3: 4, 5: 6}
#         #{1: '2', 3: '4', 5: '6'}
# result = dict(map(lambda items: (items[0], str(items[1])), dict_.items()))
# print(result)


#______________________________________________________________________________


# filter(function, Iterable) - Применяет ко всем элементам iterable функцию которую мы передаем и возвращает
# filterobject(итератор) с теми объектами, для которых функция вернула True.


# list_of_str = ['one', 'two', 'list', '', '100', '1', '50', 'John99']
# result = filter(str.isdigit, list_of_str)
# print(result)
# for x in result:
#     print(x)


# ls = [10, 11, 102, 213, 314, 515]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)


# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22', 'ono']
# result = list(filter(lambda x: len(x) >= 4, list_of_words))
# print(result)

#__________________________________________________________________________



# enumerate(Iterable) 

# ls = ['str1', 'str2', 'str3']
# i = 0 
# for x in ls:
#     print(f'element: {x}, index: {i}')
#     i += 1

# for i, x in enumerate(ls):
#     print(f'element: {x}, index: {i}')


# new_list = list(enumerate(ls))
# print(new_list)


#-----------------------------------

# zip(iterables) - она соединяет каждый элемент итерируемых элементов между собой в тип данных tuple и возвращать это

# list1 = [1,2,3]
# list2 = [100,200,300]
# result = list(zip(list1, list2))
# print(result)



# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200, 300]
# result = list(zip(a, b, c))
# print(result)


# zip для создания словарей 

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['london_r1', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']

# dict_r1 = dict(zip(d_keys, d_values))
# print(dict_r1)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']

# data = {
#     'r1': ['london_r1', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['london_r2', '21 New Blobe Walk', 'Cisco', '4451', '15.4', '10.255.0.2'],
#     'sw1': ['london sw1', '21 New Globe Walk', 'Cisco', '3850', '3.6.XE', '10.255.0.101']
# }

# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)


# ----------------------------------------------------------------------------------------

# all и any 
# all -> возвращает True, если все элементы объекта истинна(или объект пустой)

# ls = [2, 1, 'stroka', True]
# print(all(ls))
# ls2 = [False, 1, 'stroka', True]
# print(all(ls2))


# ip = '10.255.0.0.1'
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any -> возвращает True, если хотя бы один элемент истинный 

# ls = [0, 1, '', False]
# print(any(ls))

# ls2 = [0, 0, '', False]
# print(any(ls2))

# def ignore_command(command):
#     '''
#     Функция проверяет есть ли в команде слово их списка ignore. 
#     True - если есть, иначе False
#     '''
#     ignore = ['rm -rf', 'alias', 'reset']

#     for word in ignore:
#         if word in command:
#             return True
#     return False
# # print(ignore_command('sudo rm -rf user'))
# command = 'sudo nano configurations'
# if ignore_command(command):
#     raise Exception('Invalid command')
# print('All Okay')


# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo nano configurations'

# if any([word in command for word in ignore]):
#     raise Exception('Invalid command')
# print('All Okay')



# from random import choices 
# from string import ascii_letters, digits
# from itertools import repeat

# q_pass = int(input('Введите количество паролей: '))
# print({
#     f(choices(ascii_letters, k=10), choices(digits, k=5))
#     for f in repeat(lambda x, y: ''.join(set((x+y))), q_pass)
# })

