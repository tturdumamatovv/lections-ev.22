# import random 

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']
# p = 0
# m = 0 
# k = 0 
# l = 0 
# d = 0
# for i in range(0, 100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p += 1
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() == 'kuurdak':
#         k += 1
#     elif choice.lower() == 'lagman':
#         l += 1 
#     elif choice.lower() == 'dymdama':
#         d += 1
# # print(f'Plov: {p},\nManty: {m},\nKuurdak: {k},\nLagman: {l}')

# dict_ = {'Plov': p, 'Manty': m, 'Kuurdak': k, 'Lagman': l, 'Dymdama': d}
# # print(dict_)
# res = sorted(dict_.items(), key=lambda x: x[1])
# winner = res[-1]
# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]}')



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


# 3 Task

# ls = []
# for i in range(0,100):
#     if i%2==0:
#         ls.append(i**2)
#     elif i%2!=0:
#         ls.append(i)
# print(ls)
    

# def countingValleys(steps, path):
#     dolina = 0 
#     sea_level = 0 
#     for x in path:
#         if x == 'U':
#             sea_level += 1
#             if sea_level == 0:
#                 dolina += 1 
#         elif x == 'D':
#             sea_level -= 1
#     return dolina 

# print(countingValleys(12, 'DDUUDDUDUUUD'))



m1,m2,m3= map(int,input().split())
if 94 > m1 or 94 > m2 or 94 > m3 or 727 < m1 or 727 < m2 or 727 < m3 :
    print("Error")
elif m1 > m2 and m1 >  m3:
    print(m1)
elif m2 > m1 and m2 > m3:
    print(m2)
elif m3 > m1 and m3 > m2:
    print(m3)
else:
    print(m1)

m1,m2,m3 = map(int,input().split())
if 94 > m1 or 94 > m2 or 94 > m3 or 727 < m1 or 727 < m2 or 727 < m3 :
    print("ERROR")
elif m1 > m2 and m1 > m3 :
    print(m1)
elif m2 > m1 and m2 > m3 :
    print(m2)
elif m3 > m1 and m3 > m2 :
    print(m3)
else:
    print(m1)