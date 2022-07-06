# types = (str, int, float, list, tuple)

# for value in types:
#     print(value, True if '__iter__' in dir(value) else False)




# name_lists = ['Ermek', "Aidana", 'Tima', 'Bermet', 'Zhanylai']

# for name in name_lists:
#     if name.lower() == 'aidana':
#         continue
#     print(f'Hi {name}!')

# sred = len(name_lists) //2 
# name_lists.insert(sred, 'Ramazan')
# for name in name_lists:
#     if name == 'Ramazan':
#         break
#     print(f'Hi {name}!')



# a = bool(23)
# while a:
#     if input('Enter message: ') in 'war drags black'.split():
#         print('You are BLOCKED!!!')
#         break




# 1) input(Email)  2) Show Emails  
# CRUD - Create Read Update Delete
# DB_EMAILS = []

# while True:
#     print(' 1) Input Email    2) Show db_emails   3)Delete email in DB    4) stop WHILE!!!   5) Rename email') 
#     choices = int(input('Enter choice: '))
#     if choices == 1:
#         email = input('Enter email: ')
#         if email.endswith('@gmail.com'):
#             if email in DB_EMAILS:
#                 print('gmail уже существует!!!')
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         print('invalid email, only GMAIL.COM!!!')
#     elif choices == 2:
#         print(DB_EMAILS)
#     elif choices == 3:
#         email = input('Enter email: ')
#         if email in DB_EMAILS:
#             # index = DB_EMAILS.index(email)
#             # DB_EMAILS.pop(index)
#             DB_EMAILS.remove(email)
#         else:
#             print(f'{email}не существует!!!')
#     elif choices == 4:
#         break
#     elif choices == 5:
#         old_email = input('Enter old_email: ')
#         if old_email in DB_EMAILS:
#             new_email = input('Enter new_email: ')
#             if new_email.endswith('@gmail.com'):
#                 DB_EMAILS.remove(old_email)
#                 DB_EMAILS.append(new_email)
#     else:
#         print('Error !!!')



# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# for i in range(5):
#     if i == 3:
#         break
#     print(i)


# 1 
# name_of_friends = ['Aibek', 'Agahan', 'Beka', 'Artur', 'Dastan']
# for i in name_of_friends:
#     print(i)

# 2
# labels = ['Honda', 'BMW', 'Toyota']
# for i in labels:
#     print('I like brand',i)

# 3
# name_of_list = ['Helloworld!']

# string = name_of_list[0]
# length = len(string)

# if length % 2 == 0:
#     result = list(string[length // 2:] + string[:length // 2])
# else:
#     result = list(string[length // 2 + 1:] + string[:length // 2 + 1])

# print(result)


# 4 
# list_ = ['world', 'hello']
# list_.reverse()
# new_list = list_
# print(new_list)


# 5 
# suitcase = []
# suitcase.append('Cap')
# suitcase.append('Heels')
# suitcase.append('Stockings')
# suitcase.append('Panties')
# suitcase.append('Laptop')
# suitcase.pop()
# suitcase.insert(0, 'EarPods')
# print(suitcase)



# 6 
# nums = [1,1,2,3,5,8,13,21,34,55,89]
# res = []
# for i in nums:
#     if i < 5 :
#         res.append(i)
# print(res)


# 7
# a = input().split(",")
# tuple_ = tuple(a)
# list_ = list(a)
# print(list_)
# print(tuple_)


# 8 
# list_ = [1,2,3,4,5]
# new_list = []
# for i in list_:
#     new_list.append(str(i))
# print(new_list)


# 9 
# list_ = [1,2,3,4,5,6,7,8,9]
# new_list = []
# for i in list_:
#     if i%2==0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')
# print(new_list)


# 10
# list_ = []
# for i in range(20):
#     list_.append(i)
# print(list_)



# 11 
# list_ = []
# for i in range(101):
#     if i%2==0:
#         list_.append(i)
# print(list_)




# 12 
# list1 = [4,5,6,3,7,9,1]
# list2 = [4,6,579,86,0,54]
# list1.extend(list2)
# print(sum(list1))



