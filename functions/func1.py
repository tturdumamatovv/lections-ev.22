# def <name_of_function>(<a, b> #параметры):
#     <body> # некий код, некая логика 
#     <return # возвращаем что-то>

# <name_of_function>(<5, 6> # аргументы)

# Параметры функции - переменные которые будет принимать наша функция, 
# для того чтобы мы смогли работать с данными которые передаются в жто функцию

# Аргументы - данные которые мы передаем для параметров при вызове функции

# return нужен для того чтобы функция что то возвращала, и для того чтобы мы 
# могли работать с результатом действий функции, return является необязательным оператором 
# (возвращает None - если не указать return)


# ls = []
# result = ls.append(1)
# print(ls)
# print('результат действия: ', result)

# result1 = ls.pop()
# print(ls)
# print('результат действия: ', result1)



# def sumTwoNums(num1, num2): # параметры 
#     result = num1 + num2 
#     # print(result)
#     return result 
# print(sumTwoNums(5, 5)) # аргументы


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# a = 10 
# b = int(input('Enter num: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))


# def isEven1(num: int) -> bool:
#     """
#     Наша функция проверяет является ли число,
#     типа int, четным ?
#     """ 
#     if num % 2 == 0:
#         return True
#     return False

# isEven()
# isEven1()

# Anna, Ded, Kabak, Kazak, Walaw, ono

# def get_polindrom(words: list[str]) -> list:
#     '''
#     Функция возвращает список из полиндрома
#     '''
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result 

# some_word = ['John', 'Ono', 'Kazak', 'peter', 'anna', 'Dovod', 
# 'apa', 'Juice', 'piko', 'tenet']
# print(get_polindrom(some_word))


# def func():
#     print('hello world')
# func()

# ==================================================================

# default params

# def print_welcome(name:str='User') -> str:
#     print(f'Welcome, {name}!')

# print_welcome()

'''
Напишите функцию которая будет возвращать ваш 
депозит через определенное время с процентом 10%,
возвращать финальное количество денег
Мин период вложения 3 года, 
мин ставка денег 30000
'''


# def get_percentage(money: float, period: int)-> float:

#     '''
#     Return final amount of money!
#     '''
#     if money < 30000:
#         raise Exception('Вы ввели некоректное количество денег, мин ставка 30000 сомов!')
#     if period < 3:
#         raise Exception('Вы ввели некоректный срок для депозита, мин период волжения 3 года!')
#     i = 0
#     while i < period:
#         money = money + (money*0.1)
#         # money * 1.1 
#         #  money + (money / 100 * 10)
#         i += 1 
#     return money 

# money = float(input('Введите сумму денег: '))
# year = int(input('Введите срок вашего депозита: '))
# print(get_percentage(money, year))



# 'Hello world! My name is John, last name is Snow. Nice to meet you!'

# def get_reverse(text: str) -> str:
#     '''
#     return reversed string*
#     '''
#     spisok = text.split(' ')
#     result = ' '.join(spisok[::-1])
#     print(result)
#     return result

# get_reverse('Hello world! My name is John, last name is Snow. Nice to meet you!')








