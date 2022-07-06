# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # a,b,c,d параметры
#     '''
#     Returns sum of all parameters
#     '''
#     return a + b + c + d
# result = sum_of_args
# print(result)
# print(type(result))
# print(result(5,10,15,20))

#------------------------------------------------------------------------------

# Позиционные и именованные аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
# printParams(1, c = 3, b = 5)


# def sum_of_args(a: int, b: int, c: int, d: int) -> int: # a,b,c,d параметры
#     '''
#     Returns sum of all parameters
#     '''
#     return a + b + c + d
# print(sum_of_args(1, 2, 3, 4)) # Позиционныые аргументы (arguments)
# print(sum_of_args(a = 5, b = 6, d = 7, c = 6)) # Именованные аргументы (keyword arguments)
# print(sum_of_args(5, 10, d = 15, c = 20)) 


# -----------------------------------------------------------------------------------------
# Оператор * 
# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)
# print(*a, end='*\n')

# ---------------------------------------------------------------------------------------
# *args **kwargs в функциях


# def print_scores(student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     # print(type(scores))
#     for x in scores:
#         print(f'Оценка:', x)      
# print_scores('John Snow', 100, 90, 80, 70, 88, 96)



# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         print(f'{pet}: {name}')
# print_pet_names('John Snow', dog='Rex', cat='Larry', fish=['Nemo', 'Dori', 'Alex'], 
# turple='Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('параметры a и b:', a, b)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])
#     print('Аргументы', args)
#     print('Именованные аргументы:', kwargs)
# get_some_data(1,2,3,4,5, lang='Python', name='John Snow', car='BMW M5')


# ----------------------------------------------------------------------------

# def conc_two_string(str1, str2):
#     import random
#     res = random.randint(1, 10)
#     return str1 + str2 + str(res)
# result = conc_two_string('hello', 'world')
# print(result)

#-------------------------------------------------


# def generate_password(name, fam):
#     import random 
#     random_num = random.randint(100000,999999)
#     return name + fam + '_' + str(random_num)

# def get_info():
#     name = input('Введите имя: ')
#     fam = input('Введите фамилию: ')
#     return generate_password(name, fam)

# result = get_info()
# print(result)

#---------------------------------------------------

# def generate_random_string(len_, lang):
#     import string as s
#     import random
#     random_str = ''.join(random.choice(s.ascii_lowercase + s.digits)for i in range(len_))
#     return random_str 

# print(generate_random_string(15, 'eng'))

#---------------------------------------------------







def add(num1, num2): return num1 + num2 

def subtract(num1, num2): return num1 - num2

def multiply(num1, num2): return num1 * num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'На 0 делить нельзя'


def main():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели некорректные данные')
        main()
    operator = input('Введите оператор(+, -, /, *): ')
    result = None


    if operator == '+': result = add(num1, num2)
    elif operator == '-': result = subtract(num1, num2)
    elif operator == '*': result = multiply(num1, num2)
    elif operator == '/': result = divide(num1, num2)
    else:
        print('Вы ввели некорректный оператор!!!')

    print(f'Результат: {result}')

    question = input('Хотите проолжить?(Yes/No):')
    if question. lower() == 'yes':
        main()
    else:
        print('Спасибо что используете наш калькулятор, пока)')

main()