######################## Лабораторно упражнение 11 ###################

# Създаване на модул и съхраняване под името mymodule.py:
# def greeting(name):
#     print("Hello, " + name)

# Извикване на модула:
# import mymodule
# mymodule.greeting("Jonathan")

# # Hello, Jonathan


# from modname import name1 [, name2 [... nameN]]

# from fibo import fib, fib2
# fib(500)

# # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# from modname import *

# from fibo import *
# fib(500)

# reload()

# reload(module_name)

# Създаване на модули с използване на променливи от тип масив, обекти речници и 
# Нека следващия код бъде съхранен под името mymodule.py:
# a = mymodule.person1["age"]
# print(a)

# Локализиране на модули ( променлива PYTHONPATH):
#     set PYTHONPATH = c:\python20\lib;

# Глобални и локални променливи

# Дефиниране на глобална променлива:

# # дефиниране
# var = 'Hello world'

# # достъпване на променливата
# def my_function():
#     print(var)

# # извикване на функция
# my_function()

# Обхват на локална и глобална променлива:
# var = 'global scope'
# var = 'local scope'
# my_funciton()
# print(var)

# #local scope
# #global scope

# Функция dir()

# import math

# content = dir(math)
# print content


# Пример 11:
# три.py файла в директория Phone с определи функции:
# 1. Pots.py:

# def Pots():
#     print "I'm Pots Phone"
# 2. Isdn.py, e аналогичен на Pots.py и изпълнява функцията Isdn() за извеждане на съобщение "I'm ISDN Phone"
# 3. G3.py, изпълняващ функцията G3(), извеждайки съобщението "I'm ISDN Phone"

# Създава се четвърти файл __init__.py в директорията Phone, чрез който да изпълним всички горепосочени функции.
# from Pots import Pots
# from Isdn import Isdn
# from G3 import G3

# Резултат: всички посочени класове са налични, когато се импортира пакета Phone:
# import Phone

# Phone.Pots()
# Phone.Isdn()
# Phone.G3()

# Резултат:
# I'm Pots Phone
# I'm 3G Phone
# I'm ISDN Phone