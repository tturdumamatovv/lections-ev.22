# Обработка исключений 
# Операторы : try...except

# Ошибки - > связанные с кодом : 
# IndentationError
# TabError
# SyntaxError

# # Исключения -> Invalid values 
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException # прородитель всех ошибок

# try ... except

# try: 
#     <body try>
# except:
#     <body except>

# num1 = int(input('Введите число: '))
# print(num1)
# print('очень важная строчка кода')

# try:
#     num1 = int(input('Введите число: '))
#     print(num1)
# except:
#     print('Вы ввели некорректные данные исправьте это!!!')
# print('Очень важная строчка кода')

# 1. import sys
# list_ = [1,2,3,4,5]
# index = int(input('Введите индекс: '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     import sys
#     print(f'Oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e 

# list_ = [1,2,3,4,5]
# index = int(input('Введите индекс: '))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e: 
#     print(f'Oop, we catched {e.__class__} error!')


# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Введите индекс: '))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print('IndexError!!!')
# except ValueError:
#     print('ValueError!!!')


# else в try ... except 
# finally в try ... except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body> # Сработает если в операторе try не случилась ошибка
# finally:
#     <body> # сработает при любом исходе

# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter_2: '))
#     result = num1/num2
# except ZeroDivisionError:
#     print('на 0 делить нельзя!')
# except ValueError:
#     print('Invalid symbols!')
# else:
#     print(result)
# finally:
#     print('Код закончился')
