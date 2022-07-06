'''
Tuple -  это структура данных
неизменяемый
индексируемый
упорядочный 
'''

# string1 = str('hello AttackPython')
# string = 'hello world'
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {}
# dict1 = {'key': 'value'}

# tuple1 = (1,2,3)
# print(type(tuple1)) # -> tuple class

# tuple1 = 1,2
# print(tuple1[0])
# print(type(tuple1))

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))

# emails1 = ['Python@gmail.com', 'Tima@mail.ru']
# emails = ('Python@gmail.com', 'Tima@mail.ru')
# разница рамера 'tuple' и 'list'
# print(emails.__sizeof__(), emails1.__sizeof__(), sep= ' | ')

# emails = ('Python@gmail.com', 'Tima@mail.ru', 3, 5, ['potato', 'arbuz', 'apple'])
# print(type(emails[-1]))
# last_object = emails[-1]  # list
# last_object.append('Tomato')
# print(emails)
# print(len(emails))

# print(dir(tuple))

# Метод count и index в tuple
# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance  += tuple_sequance_first 
# # print(tuple_sequance)
# print(tuple_sequance.count(2))
# print(tuple_sequance.index(3))

# for value in tuple_sequance:
#     print(value)

# names = ('Tima', 'Zhanylai', 'Aidana', 'Bermet', 'ermek')
# print(names[0] + ' hello!')
# print(names[1] + ' hello!')
# print(names[2] + ' hello!')
# print(names[3] + ' hello!')
# print(names[4] + ' hello!')

# names_enter = ['Bermet', 'Ermek']

# for name in names:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
#         # print('it is len: ', len(name))
#     else:
#         print(f'{name} go home!!!')

# first_step_names = []
# names = input('Enter names: ').split(' ')
# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)
# print(first_step_names)
    

# print('start for')
# for i in range(10):
#     print(i)
# print('stop for')

# i = 0 
# while 3 > 2:
#     print(f' {i} i work')
#     i += 1 


# i = 0 
# num = 3 
# while num > i:
#     print('i work')
#     i += 1  
