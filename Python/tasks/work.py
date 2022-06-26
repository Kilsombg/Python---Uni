# print("""
# Are you ignoring me?
# A) Yes.
# B) Yep.
# C) Absolutely.
# D) I can't stand you.
# E) You are very annoying.
# """)


########################### Упражнение 2 (задачи) ##############################
# Задача 1: 
# Да се състави програма от n цели числа и да ги сумира.

# n = int(input("Write n: "))
# a = []

# for i in range(n):
#     x = int(input("x= "))
#     a.append(x)

# print(sum(a))


########################### Упражнение 7 (задачи) ##############################
#Function

# Задача 1:
# Напишете програма, която намира лицето на геометрична фигура, като първо се въвежда вида на фигурата. 
# Първо квадртат, след това правоъгълник и правоъгълен триъгълник. За пресмятането на лицето на съответните
# фигуре да се запишат подходящи формули.

# Отговор на задачата в /Exercises/function.py

# def fig(f):
#     if f == 's':
#         square()
#     if f == 'r':
#         rect()
#     if f == 'r_t':
#         r_tr()

    
# def square():
#     a = float(input("Side of square is: "))
    
#     print(str(a*a))

# def rect():
#     a = float(input("First side of rectangle is: "))
#     b = float(input("Second side of rectangle is: "))

#     print(str(a*b))

# def r_tr():
#     a = float(input("First cathetus of right triangle is: "))
#     b = float(input("Second cathetus of right triangle is: "))

#     print(str(a*b/2))

# while True:
#     figure = input("Write the type of figure:\n")
#     if figure == "exit":
#         break
#     fig(figure)



########################### Упражнение 9 (задачи) ##############################
# Classes
# Задача 1:
# Съставете програма на Python с използването на клас за превръщане на число за преобръщането му
# от десетичен вид в римския му еквивалент

# class Number:
#     def __init__(self, value):
#         self.num = value
#         self.roman = {
#             'M'  : 1000,
#             'CM' :  900,
#             'D'  :  500,
#             'CD' :  400,
#             'C'  :  100,
#             'XC' :   90,
#             'L'  :   50,
#             'XL' :   40,
#             'X'  :   10, 
#             'IX' :    9,
#             'V'  :    5,
#             'IV' :    4,
#             'I'  :    1
#         }
    
#     def toRoman(self):
#         rom = ''
#         num = self.num
#         for k,v in self.roman.items():
#             while num // v > 0:
#                 rom += k
#                 num -= v

#         return rom

#     def toDec(self):
#         dec = 0
#         i = 0
#         rom = self.num
#         for k,v in self.roman.items():
#             while rom[i:i+len(k)] == k:
#                 dec += v
#                 i += len(k)

#         return dec

#     def reverse(self):
#         if type(self.num) == int:
#             return self.toRoman()
#         if type(self.num) == str:
#             return self.toDec()

# print(Number(1800).reverse())
# print(Number('MDCCC').reverse())


# Задача 2:
# Да се състави програма на Python с използването на клас за обръщането на низ дума по думa

# class Rev:
#     def rev_sen(self,sen):
#         s_list = sen.split()
#         sep_rev = ' '.join(reversed(s_list))

#         return sep_rev

# print(Rev().rev_sen(input()))

# Отговор на задачите в /Exercises/classes


########################### Упражнение 11 (задачи) ##############################
# Classes
# Задача 1:
# Създайте клас, който представя студентите от вашата група.
# Напишете метод, който по дадено име създава само студенти, които не са създадени от списъка от студенти.

# Задача 2:
# и напишете метод remove за триене на студент с оценка слаб

# Задача 3:
# и напишете метод за намиране на среден успех


# class Students:
#     def __init__(self):
#         self.group = {
#             'Anna' : 3.0,
#             'Bob' : 5.0,
#         }

#     def insert(self,name,mark):
#         if name not in self.group.keys():
#             self.group[name] = mark

#     def rm(self):
#         self.group = {k:v for k,v in self.group.items() if v != 2}

#     def avg(self):
#         val = [v for v in self.group.values()]
#         print(sum(val) / len(val))
    
#     def pr(self):
#         print(self.group)

#     def update(self):
#         self.rm()
#         self.pr()
#         self.avg()

# group = Students()
# while True:
#     name  = input("Write name: ('done' for stop inserting)\n")
#     if name == "done":
#         print("Input Success!")
#         break
#     mark  = float(input("Write mark: "))

#     group.insert(name,mark)

# group.update()



# class Students:
#     def __init__(self):
#         self.names = ['St1', 'St2', 'St3', 'St4']
#         self.marks = [1, 4, 2, 5]

#     def insert(self,name,mark):
#         if name not in self.names:
#             self.marks += [mark]
#             self.names += [name]

#     def rm(self):
#         for i in range(len(self.marks)-1, -1,-1):
#             if self.marks[i] == 2:
#                 del self.names[i]
#                 del self.marks[i]
                

#     def avg(self):
#         print("\n" + str(sum(self.marks) / len(self.marks)))
    
#     def pr(self):
#         for i in range(len(self.marks)):
#             print(self.names[i], str(self.marks[i]), end="   ")

#     def update(self):
#         self.rm()
#         self.pr()
#         self.avg()

# group = Students()
# while True:
#     name  = input("Write name: ('done' for stop inserting)\n")
#     if name == "done":
#         print("Input Success!")
#         break
#     mark  = float(input("Write mark: "))

#     group.insert(name,mark)

# group.update()


# Отговор на задачите в /Exercises/classes

########################### Упражнение 13 (задачи) ##############################
# Недовършена задача

# Задача 3:
#  Създайте клас, който представя студентите във вашата група:
# Напишете метод, който записва данни във файл, чете файла и създава списък на студентите.
# Напишете метод, който да добавя студенти, които не са записани в списъка студенти
# Напишете метод remove, който да трие студент със слаб успех
# Напишете метод за намиране на среден успех на група
# ??? Напишете метод за намиране на минимален и максимален успех
# Напишете метод copy, който да копира студенти с начална буква 'А'в нов списък, който метода връща
# Напишете метод, който връща данните за студентите с един и същ успех
# ??? Напишете метод, който да връща данни за студентите с четен номер и с максимален успех
#-------------------------------------------------------------------------------------------
# ??? Напишете метод move, който мести студенти с отличен успех...
# ??? метод, който връща данните за студентите с четен номер и минимален успех
# метод, който представя имената на студентите само с големи букви 

# class Students:

#     def __init__(self):
#         self.group = {
#             'Fred' : [4, 101],
#             'George' : [2, 102],
#             'Sebastian' : [5, 103],
#             'Leah' : [6, 104],
#             'Sandra' : [3, 105]
#         }

#     def ins(self):
#         with open("data.txt", 'w') as data:
#             data.write(str(self.__dict__))

#     def add(self,name,mark,id):
#         if name not in self.group.keys():
#             self.group[name] = (mark,id)

#     def rm(self):
#         self.group = {k:v for k,v in self.group.items() if v[0] != 2}

#     def avg(self):
#         marks = [val[0] for val in self.group.values()]
#         print(sum(marks) / len(marks))


# group = Students()
# group.ins()



# Задача 4:
# Да се създаде функция приход от списък със стоки, с цена-количество. 
# Да се извърши търсене по код и ако кода фигурира да се създаде намаление с 10%. 
# Ако го няма да се генерира друг код с поредица от 4 нули и съобщение: "Зареди продукта." 
# Да се изчисли средно-аритметичната и цена на списъкиа със стоки.




















# Задачи от лабораторните
# отговорите са в папката /Laboratories във файловете със съответните имена

# За точност на задачите не гарантирам, първо пробвай дали работи и след
# това разгледай кода


############################# Лабораторни 1 (задачи) ##############################
# Задача 1:
# Да се състави програма на Python, която извежда съобщението: "Hello, Python!"

# print("Hello, Python!")

# Задача 2:
# Да се състави програма, която да изпълнява аритметичните операции +,-,*,/ 
# на две чила а и b от цял тип. Като за всяка аритметична операция се изведе
# резултат като а и b се въведнат от клавиатурата

# a = 3
# b = 4

# print("{} + {} = {}".format(a,b,a+b))
# print("{} - {} = {}".format(a,b,a-b))
# print("{} * {} = {}".format(a,b,a*b))
# print("{} / {} = {}".format(a,b,a/b))

############################# Лабораторни 2 (задачи) ##############################
# Задача 1:
# Да се направи програма, която приема три стойности a,b и h и пресмята лицето
# на трапец S=(a+b)*h/2, принтирайте резултата като закръглите до 2-рия знак 
# след десетичната запетая ",". 
# Забележка: print("%.2f" %name)

# a = int(input("a="))
# b = int(input("b="))
# h = int(input("h="))

# print(round((a+b)*h/2,3))


# Задача 2:
# Чете от клавиатурата r и пресмята и отпечатва лицето и периметъра на окръжност
# с радиус r. Изведете резултата като закръглите до 3-тия знак след десетичната запетая.
# (S = pi*r^2, C = 2pi*r)

# import math
# r = int(input("r= "))

# print("S= ", round(math.pi*r**2,3))
# print("C= ", round(2*math.pi*r,3))


# Задача 3:
# Изчислява дневната надница при n-часов работен ден като заплащането за час е числото к
# въвеждано от клавиатурата. Да се изчисли работната надница за 1 месец при 20 дневен работен месец.

# n = int(input("n= "))
# k = int(input("k= "))

# dn_nad = n*k
# print("Дневна надница: ",dn_nad)

# mes_nad = dn_nad * 20
# print("Месечна надница: ", mes_nad)


############################# Лабораторни 3 (задачи) ##############################
# Задача 1:
# Да се направи програма, в която се въвеждат n цели числа и намира max.
# Първо се въвежда n, след това се въвеждат n на брой числа.

# n = int(input())
# li = []
# for i in range(n):
#     x = int(input("x= "))
#     li.append(x)
# print(max(li))

# Задача 2:
# Да се състави програма, която чете число n и проверява дали е > 50,
# ако е така print("bigger than 50") else ("smaller")

# n = int(input("n= "))
# print("Bigger than 50." if n > 50 else "Smaller than 50.")

# Задача 3:
# Принтирайте от 1 до 10 числата с while

# x = 1
# while x < 10:
#     print(x, end=" ")
#     x += 1

# Задача 4:
# Принтирайте от 1 до 10 като пропусне 5 (continue)

# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     print(x, end=" ")

############################# Лабораторни 4 (задачи) ##############################

# Задача 2:
# въвежда число n и печата триъгълник от '*'.
# Пример:
# n = 3
# ------------
# *
# **
# ***
# ------------

# n = int(input("n= "))
# for i in range(1,n+1):
#     print(i*"*")


# Задача 4:
# Да се напише програма, която проверява дали дадено число е просто число.

# def  isPrime(num):
#     res = True
    
#     for i in range(2,num//2):
#         if num % i == 0:
#             res = False
#             break
#     print(res)

# isPrime(55)

############################# Лабораторни 6 (задачи) ##############################

# Задача 1:
# Напишете програма, в която потребителя въвежда цяло число, а програмата формира 2 кортежа, 
# състоящи се цифрите от това число. Единия с цифрите състоящи се в прав ред, втори, в които са в обратен ред

# n = input("n= ")
# t = tuple(map(int,n))
# t_rev = tuple(reversed(n))
# t_rev = tuple(map(int,t_rev))
# print(t)
# print(t_rev)


# Задача 2:
# Напишете програма, в която се създава числов списък. Той се запълва със случайни числа, 
# след това от всяка двойка елементи от този списък се вмъква нов равен на сумата от стойностите
#  на предходните два елемента.

# import random
# import math
# random.seed()

# li = []
# for i in range(16):
#     li.append(random.randint(0,10))
# print(li)
# for i in range(2,math.floor(len(li)*1.5),3):
#     num = li[i-1] + li[i-2]
#     li.insert(i,num)
# print(li)


# Задача 3:
# Напишете програма , в която потребителя въвежда текст и на негова база се създава речник. 
# За ключове на речника служат символите от текста, а стойността на елементите се определя от 
# броя на съответните символи в текста.
# Примерен вход :  SSWTWWTAAA

#             Речникът ще се състои от 4 елемента :

#              А:3     S:2       T:2     W:3

# sent = input()
# s = sorted(set(sent))
# d = {}

# for ch in s:
#     d[ch] = sent.count(ch)

# print(d)


# Задача 4:
# Напишете програма, в която потребителя въвежда чяло число. 
# От него се създава списък състоящ се от числата от 1 до това число . 
# Въз основа на този списък се създава речник, в който елементите на списъка
# служат за ключове на елементите на речника , а стойностите на тези елементи в речника
# са елементите на списъка но в обратен ред.

# Пример : ако сме въвели числото 4 , създава се списъка  [1,2,3,4 ]
#  и на негова основа се създава речник с 4 елемента :   {1:4, 2:3,  3:2,  4:1}

# x = int(input("x= "))
# li = [i for i in range(1,x+1)]

# dic = {k:v for k,v in zip(li,reversed(li))}
# print(dic)


############################# Лабораторни 7 (задачи) ##############################
# Function

# Задача 1:
# Напишете програма, която намира лицето на геометрична фигура като първо се въвежда вида на фигурата:
#  1 - квадрат, 2 - правоъгълник, 3 - правоъгълен триъгълник. 
# За пресмятането на лицето на фигурите да се напишат подходящи функции

# def square():
#     a = int(input("a= "))
    
#     print(a*a)

# def rec():
#     a = int(input("a= "))
#     b = int(input("b= "))

#     print(a*b)

# def ri_tr():
#     a = int(input("a= "))
#     b = int(input("b= "))

#     print(a*b/2)    

# def figure(fig):
#     if fig == "s":
#         square()
#     if fig == "r":
#         rec() 
#     if fig == "r_t":
#         ri_tr()

# fig = input("Write type of figure: ")
# figure(fig)


# Задача 2:
# Напишете потребителска функция , проверяваща дали число е палиндром. 
# Функцията получава като аргумент число, връща като резултат 1, ако числото е палиндром
#  и 0 ако числото не е палиндром.

# def isPoli(num):
#     rev = int(''.join(reversed(str(num))))
#     print(1 if num == rev else 0)

# isPoli(34543)


# Задача 3:
#  Програма, която реализира калкулатор за цели числа. Действията които изпълнява са :
#             Събиране +
#             Изваждане –
#             Умножение *
#             Деление /
# Потребителя въвежда вида на операцията.
# После въвежда две числа и резултата се извежда на екрана . Реализирайте отделни функции за отделните операции.

# def s(a,b):
#     print(a+b)

# def m(a,b):
#     print(a-b)

# def p(a,b):
#     print(a*b)

# def d(a,b):
#     print(a/b)

# def op(t):
#     a = int(input("a= "))
#     b = int(input("b= "))

#     if t == 's' or t == '+':
#         s(a,b)
#     if t == 'm' or t == "-":
#         m(a,b)
#     if t == 'p' or t == "*":
#         p(a,b)
#     if t == 'd' or t == "/":
#         d(a,b)

# type = input("Type of operation: ")
# op(type)


# Задача 4:
# На функция се подават два аргумента: списък с числа  и число. Променете всички елементи от списъка със 
# стойност по-голяма от даденото число на 0(нула).

# def no_big(li,number):
#     li = [x if x <= number else 0 for x in li]

#     print(li)

# li = [1,2,3,4,5,6,7,8,9,10]
# k = int(input("k= "))

# no_big(li,k)

# Отговора на задачите е в /Laboratories/function.py



############################# Лабораторни 8 (задачи) ##############################
# Classes

#Задача 1: 
# Да се напише код на Python, който дефинира клас Person с полета
# име (name),  фамилия (family), възраст (age), националност (nationality). 
# Да се дефинира конструктор, който инициализира полетата на класа. 
# Да се добави метод print, който отпечатва имената и националността на съответното лице. 
# Да се създадат обекти-инстанции на класа. За тях  да се извика методът print.


# class Person:

#     def __init__(self,name,family,age,nationality):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.nationality = nationality

#     def  pr(self):
#         print("{} {} is {} years old. He/She is from {}."
#             .format(self.name,self.family,self.age,self.nationality))
        
# John = Person("John", "Perseccati", 32, "Italy")
# Maru = Person("Maru", "Tue", 28, "Spain")

# John.pr()
# Maru.pr()

# Задача 2:
# Да се добави към кода от Задача 1 клас Student, наследник на класа Person с две нови полета
# – университет (university) и година на обучение (yearofstudy). Да се предифинира за него методът print,
#  така, че да отпечатва и тези две полета. Да се създадат инстанции на новия клас и за тях да се извика
#  методът print.

# class Student(Person):
#     def __init__(self, name, family, age, nationality, universiy, yearofstudy):
#         super().__init__(name, family, age, nationality)
#         self.university = universiy
#         self.yearofstudy = yearofstudy

#     def pr(self):
#         print("({}, {})".format(self.university,self.yearofstudy), end=". ")
#         return super().pr() 

# Peter = Student("Peter","Dyke",45,"Bosna","EVU",2008)
# Peter.pr()

# Да се добави: class Lecturer, наследник на Person
#  с две нови полета university, experience - брой години, преподавателски стаж 
# да  се направи print, така че да отпечатва тези две полета


# class Lecturer(Person):
#     def __init__(self, name, family, age, nationality, universiy, experience):
#         super().__init__(name, family, age, nationality)
#         self.university = universiy
#         self.experience = experience 

#     def pr(self):
#         print("({}, {})".format(self.university,self.experience), end=". ")
#         return super().pr() 

# Lora = Student("Lora","Stamatos",45,"Bulgaria","WROU",17)
# Lora.pr()



# Отговора на задачите е в /Laboratories/classes.py

############################# Лабораторни 10 (задачи) ##############################
# Errors
 # Отговори няма

# Задача 1:
# Напишете код на метод, който приема като параметър име на текстов файл, 
# прочита съдържанието на файла и го връща като стринг. 
# Какво е правилно да направи методът с възникващите изключения?

# def reading(fname):
#     with open(fname,"r") as f:
#         text = f.read()

#     return text

# path = "text.txt"
# print(reading(path))


# Задача 2:
#  Да се открият и прегледат всички стандартни изключения на Python

# Exception context, Base classes, Concrete exceptions, 

# Задача 3:
# Прегледайте от документацията на Python информацията за основните изключения
# BaseException, Exception, ArithmeticError, BufferError, LookupError


# exception Exception

#     All built-in, non-system-exiting exceptions are derived from this class.
#      All user-defined exceptions should also be derived from this class.

# exception ArithmeticError

#     The base class for those built-in exceptions that are raised for various arithmetic errors:
#      OverflowError, ZeroDivisionError, FloatingPointError.

# exception BufferError

#     Raised when a buffer related operation cannot be performed.

# exception LookupError

#     The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid:
#      IndexError, KeyError. This can be raised directly by codecs.lookup().


# Задача 2:
# Напишете програма, която прочита от конзолата цяло положително число
#  и отпечатва на конзолата корен квадратен от това число. Ако числото е отрицателно или невалидно,
#  да се изпише “Invalid Number”. Във всички случаи накрая да се изпише “Good Bye”.

# import math

# try:
#     x = int(input("x= "))
#     print(math.sqrt(x))
# except:
#     print("Invalid numbeer")
# finally:
#     print("Good Bye!")


# Задача 3:
# Да се състави програма на Python, която дефинира клас Travel с полета: ID, Destination, Flight, Price.
#  Да се добави метод „Reduce“, чрез който всички стойности от полето Price по-големи от 200
#  да бъдат заменени със стойност по-ниска с 10%. Да се добави и методът Print,
#  чрез който да се отпечатят ID, Destination, Flight, Price.

# class Travel:
    
#     def __init__(self, id, destination, flight, price) -> None:
#         self.id = id
#         self.destination = destination
#         self.flight = flight
#         self.price = price
        
#     def Reduce(self):
#         self.price = [x if x < 200 else round(x * 0.9,2) for x in self.price]

#     def Print(self):
#         print("ID".center(6), "Flight".center(10), "Destination".center(15), "Price".center(9))
#         for id, flight, destination, price in zip(self.id, self.flight, self.destination, self.price):
#             print(id.center(6), flight.center(10), destination.center(15), str(price).center(9))


# id = ["101", "102", "103", "104", "105", "106"]
# destination = ["Tokyo", "Prague", "Paris", "Melobourne", "Madrid", "Barcelona"]
# flight = ["TO4563", "SR2334", "VF7655", "SZ3897", "JU8676", "TR5325"]
# price = [250.0, 175.0, 340.0, 243.0, 200.0, 190.0]

# airport1 = Travel(id, destination, flight, price)
# airport1.Reduce()
# airport1.Print()
        

# Задача 4:
# Напишете програма на Python, за да получите следващия ден от дадена дата (въведена от потребителя).
# Пример:
# Input a year: 1974
# Input a month [1-12]: 2
# Input a day [1-31]: 15
# The next date is [yyyy-mm-dd] 1974-2-16.

# def next_date():
#     y = int(input("Input a year: "))
#     m = int(input("Input a month [1-12]: "))
#     d = int(input("Input a day [1-31]: "))

#     m30 = [4, 6, 9, 11] # 30 days month
#     m31 = [1, 3, 5, 7, 8, 10, 12] # 31 days month

#     if m == 2 and d == 28:
#         if y % 4 == 0: # Leap year
#             d += 1
#         if y % 4 != 0: # not leap year
#             m += 1
#             d = 1
#     elif m == 2 and d == 29:
#         m += 1
#         d = 1
#     elif m in m30 and d == 30:
#         m += 1
#         d = 1
#     elif m in m31 and d == 31:
#         if m == 12:
#             y += 1
#             m = 1
#             d = 1
#         else:
#             m += 1
#             d = 1
#     else:
#         d += 1
    
#     print("The next date is [yyyy-mm-dd] {}-{}-{}".format(y,m,d))

# while True:
#     next_date()

############################# Лабораторни 11 (задачи) ##############################
# Modules
# Задачи за модули са в папки Calculator и FigureAreas
# /Laboratories/Calculator
# /Laboratories/FigureAreas



############################# Лабораторни 12 (задачи) ##############################
# Files
# Отговори на тези задачи няма

# Задача 1:
# Да се създаде програма, която да чете предварително направен файл и да извежда съдържанието му ред по ред с помоща
#  на for цикъл

# with open("text.txt",'r') as f:
#     for line in f:
#         print(line)


# Задача 2:
# Да се създаде двоичен файл с document.bin, създадения файл да се отвори и реализира запис в подходящ режим на стринга
#  "This is good", който да се декодира в ASCII код. 
# За записа да се използва метода file.write(), а за затваряне на файла метода file.close().

# file = open("document.bin","wb+")
# text = "This is good"
# encoded = text.encode("ASCII")
# file.write(encoded)
# file.seek(0)

# binary_data = file.read()
# file.close()
# print("binary: ", binary_data)
# print("encoded: ", encoded)
# text  = binary_data.decode("ASCII")
# print("deocded: ", text)

# for byte in binary_data:
#     print(byte)


# Задача 3:
#  Създайте клас, който представя студентите във вашата група:
# Напишете метод, който записва дданни във файл, чете файла и създава списък на студентите.
# Напишете метод, който да добавя студенти, които не са записани в списъка студенти
# Напишете метод remove, който да трие студент със слаб успех
# Напишете метод за намиране на среден успех на група
# Напишете метод за намиране на минимален и максимален успех
# Напишете метод copy, който да копира студенти с начална буква 'А'в нов списък, който метода връща
# Напишете метод, който връща данните за студентите с един и същ успех
# Напишете метод, който да връща данни за студентите с четен номер и с максимален успех
#-------------------------------------------------------------------------------------------
# Напишете метод move, който мести студенти с отличен успех...
# Напишете метод, който връща данни за студентите с един и същи успех
# метод, който връща данните за студентите с четен номер и минимален успех
# метод, който представя имената на студентите само с големи букви 

# class Students:

#     def __init__(self) -> None:
#         self.list = {
#             "pete" : 3,
#             'Prey' : 6,
#             "Lary" : 2,
#             "Ron" : 4,
#         } 

#     def writing(self):
#         with open("students.txt", "w") as f:
#             for k,v in self.list.items():
#                 f.write(k + " - " + str(v) + "  ")
    
#     def reading(self):
#         with open("students.txt", "r") as f:
#             text = f.read()
#         return text

#     def add(self,name,mark):
#         if name not in self.list.keys():
#             self.list[name] = mark

#     def rm(self):
#         self.list = {k:v for k,v in self.list.items() if v != 2}

#     def avg(self):
#         marks = [x for x in self.list.values()]
#         print(sum(marks) / len(marks))

#     def maxMark(self):
#         marks = [x for x in self.list.values()]
#         print(max(marks))

#     def maxMark(self):
#         marks = [x for x in self.list.values()]
#         print(min(marks))

#     def list_A(self):
#         li = [k for k in self.list.keys() if k[0] == 'A']
#         return li


# group = Students()
# group.writing()
# print(group.reading())
# group.avg()
# group.maxMark()


# Задача 4:
# Да се създаде функция приход от списък със стоки, с цена-количество. 
# Да се извърши търсене по код и ако кода фигурира да се създаде намаление с 10%. 
# Ако го няма да се генерира друг код с поредица от 4 нули и съобщение: "Зареди продукта." 
# Да се изчисли средно-аритметичната и цена на списъкиа със стоки.

# def income(list,CODE):
#     valid_code = ["ASUS", "REK123", "BTX450", "FREECODE"]
#     discount = 0

#     if CODE in valid_code:
#         discount = 0.1
    
#     # income
#     ic = 0
#     for k,v in list.items():
#         ic += k*v
#     ic = ic - discount*ic

#     print(ic)

# list = {1:2, 2:3, 4:4}
# Code = input("Write code here: ")
# income(list,Code)


############################# Лабораторни 13 (задачи) ##############################
# JSON

# Задача 1: 
# Да се създаде програма, която чете  двуичен файл document.bin,
#  като се използва режим за четене на двуичен файл, да се използва метода за четене read и print
#  за извеждане на първите четири букви от "This is good!"

# with open("document.bin", "rb") as f:
#     binary_text = f.read(4)
#     decoded = binary_text.decode()
#     print(decoded)


# Задача 2:
# Да се създаде програма на python, която да преобразува python обект в json данни
# .dumps()

# import json

# fruit = ['apple', 'banana', 'strawberry', 'bluberry']

# print(json.dumps(fruit))

########## -V2- ##########

# class Basket:
#     def __init__(self) -> None:
#         self.name = "John"
#         self.age = 13
#         self.sport = "Voleyball"

# John = Basket()
# print(json.dumps(John.__dict__))