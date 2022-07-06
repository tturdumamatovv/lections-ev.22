# 1 Task 

# list1 = []
# for i in range(0,200,2):
#         # if i%2==0:
#     list1.append(i)
# print(list1)


# 2 Task 

# a = list(range(0,200))
# b = []
# for i in a:
#     if i % 2 == 0 and i % 3 == 0:
#         b.append(i)
# print(b)

'''
comprehensions
'''
# ls = [x for x in range(0,200) if x%2==0 and x%3==0]
# print(ls)


# 3 Task

# ls = []
# for i in range(0,100):
#     if i%2==0:
#         ls.append(i**2)
#     elif i%2!=0:
#         ls.append(i)
# print(ls)

'''
comprehensions
'''
# ls = [x**2 if x%2==0 else x**3 for x in range(0, 100) ]
# print(ls)


# --------------------------

# list comprehensions - генераторы списков

# newlist = [expression for item in iterable <if condition==True>]

# list - comprehension - это упрощенный подход к созданию списка, который 
# задействует цикл for, а также конструкции if-else для определения того, что в итоге
# окажется добавлено в наш список.

# ls = []
# for i in range(0,100,2):
#     ls.append(i)
# print(ls)

# new_list = [i for i in range(0,100,2)]
# print(new_list)

# ls = [i**2 for i in range(0,11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'lemon']
# # ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if 'a' in x]
# print(ls)

# ls = [x for x in fruits if x != 'apple']
# print(ls)

# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# ls = []
# for inner_list in list_:
#     for num in inner_list:
#         ls.append(num)
# print(ls)

# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# ls = [x for inner_list in list_ for x in inner_list ]
# print(ls)


# import datetime

# start = datetime.datetime.now()
# ls = [x for x in range(1, 10_000_00)]
# # for x in range(1,10_000_000):
# #     ls.append(x)
# finish = datetime.datetime.now()
# print(finish-start)


# ls = [x+10 if x==8 else x+1 for x in range(0,10)]
# print(ls)

