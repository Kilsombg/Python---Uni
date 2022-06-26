################### Лабораторно упражнение 7 ###################

# # Функция за дължина на аргумент: len()
# a = ('foo', 'bar', 'baz', "qux")
# len(a) # 4

# # Фунцкия any(): "True", "False";
# any([False, False, False]) # False
# print(any([False, True, False])) # True

# # def <function_name>([<parameters>]):
#     #<statement(s)>

# #<function_name>([<arguments>])

# def f(qty, item, price):
#     print(f'{qty} {item} cost $ {price:.2f}')
# f(6, 'bananas', 1.74)

# #f(6, 'bananas', 1.74, 'kumquats')

# f(qty=6, item = 'bananas', price = 1.74)

# f(4, 'apples', 2.24) # 4 apples cost $2.24
# #f(4) # 4 apples cost $1.74
# #f() # 6 bananas cost $1.74

# #f(item='kumquats', qty=9) # 9 kumquats cost $1.74
# f(price = 2.29) # 6 bananas cost $2.29





# Задача 1:
# Напишете програма, която намира лицето на геометрична фигура като първо се въвежда вида на фигурата:
#  1 - квадрат, 2 - правоъгълник, 3 - правоъгълен триъгълник. 
# За пресмятането на лицето на фигурите да се напишат подходящи функции

# # square
# def square():
#     a = int(input("a = "))
#     return a*a

# # rect
# def rect():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return a * b

# # right triangle
# def right_triangle():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return (a*b) / 2

# while type != "":
#     type = input("What is the type of the figure (1 - square, 2 - rect, 3 - right triangle): \n")

#     if type == "1":
#         print(square())
#     elif type == "2":
#         print(rect())
#     elif type == "3":
#         print(right_triangle())



# Задача 2:
# Напишете потребителска функция , проверяваща дали число е палиндром. 
# Функцията получава като аргумент число, връща като резултат 1, ако числото е палиндром
#  и 0 ако числото не е палиндром.

# def is_palindrome(number):
#     temp = number
#     reverse_num = 0

#     while number > 0 :
#         digit = number % 10
#         reverse_num = (reverse_num * 10) + digit
#         number=number // 10

#     if temp == reverse_num:
#         return 1
#     return 0

# number = int(input("Enter a number: "))
# print(is_palindrome(number))



# Задача 3:
#  Програма, която реализира калкулатор за цели числа. Действията които изпълнява са :
#             Събиране +
#             Изваждане –
#             Умножение *
#             Деление /
# Потребителя въвежда вида на операцията.
# После въвежда две числа и резултата се извежда на екрана . Реализирайте отделни функции за отделните операции.

# def sum(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a * b

# def div(a,b):
#     return a / b

# type = input("Type of action: ")
# a = int(input("a = "))
# b = int(input("b = "))

# res = None
# if type == "+":
#     res = sum(a,b)
# elif type == "-":
#     res = sub(a,b)
# elif type == "*":
#     res = mul(a,b)
# elif type == "/":
#     res = div(a,b)

# print(res)



# Задача 4:
#  На функция се подават два аргумента: списък с числа  и число. Променете всички елементи от списъка със 
# стойност по-голяма от даденото число на 0(нула).


# def bigger(list, max):
#     for i in range(len(list)):
#         if list[i] > max:
#             list[i] = 0

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# max = int(input("max = "))
# bigger(list, max)

# print(list)