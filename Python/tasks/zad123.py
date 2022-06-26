##################################### Задачи 1 ##########################################
# 1. Да се състави програма, която намира всички числа в интервала [1,1000], които
# завършват на 7.

# li = [i for i in range(1,1001) if i % 7 == 0]
# print(li)


# 2. Да се състави програма, която изчислява сумата и произведението на всички
# числа от 1 до дадено число n.

# n = int(input("n = "))
# s = 0
# p = 1
# for i in range(1,n+1):
#     s += i
#     p *= i
# print("s = {} p = {}".format(s,p))


# 3. Да се състави програма, която отпечатва таблицата за умножение за дадено
# число.

# n = int(input("n = "))
# for i in range(1,11):
#     print("{} * {} = {}".format(n,i,n*i))


# 4. Да се състави програма, която извежда числата от -10 до -1.

# for i in range(-10,0):
#     print(i, end=" ")

# 5. Да се състави програма, която извежда всички прости числа в диапазона от 25
# до 50.

# def primes(start,finish):
#     prime = [num for num in range(start,finish+1) if  is_prime(num)]

#     print(prime)

# def is_prime(num):
#     result = True
#     for i in range(2, num//2):
#         if num % i == 0:
#             result = False

#     return result

# primes(25,50)

# 6. Да се състави програма, която извежда следния модел:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#     print(i*"*")
# for i in range(4,0,-1):
#     print(i*"*")


# 7. Да се състави програма, която обръща цифрите на дадено число:

# n = input("Write a number")
# list = int("".join(reversed(n)))
# print(list)


# 8. Да се състави програма, която въвежда от клавиатурата n числа и сумира
# поотделно всички четни и нечетни числа. Програмата да извежда общата
# сума и за двата случая.

# even_sum = odd_sum = 0
# n = int(input("n= "))
# for i in range(n):
#     num = int(input("x= "))
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
# print("Sum of even: {} \n Sum of odd: {}".format(even_sum,odd_sum))


# 9. Да се състави програма, която въвежда n числа от клавиатурата и намира
# средноаритметичната им стойност (1≤n≤1000).

# while True:
#     try:
#         n = int(input("n= "))
#         if n < 1 or n > 1000:
#             raise TypeError()
#         break
#     except TypeError:
#         print("Wrong value... (1 <= n <= 1000). Try again...")

# li = ()
# for i in range(n):
#     x = int(input("x="))
#     li += (x,)

# print(sum(li) / len(li))

# 10. Да се състави програма, която въвежда n (n≤10) на брой реални числа
# по-малки от 1000 и намира тяхното произведение.

# while True:
#     try:
#         n = int(input("n= "))
#         if n > 10:
#             raise TypeError()
#         break
#     except TypeError:
#         print("Wrong value... (n <= 10). Try again...")

# p = 1
# for i in range(n):
#     x = 1000
#     while x >= 1000:
#         x = int(input("x="))
#     p *= x
# print(p)

# 11. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са отрицателни.

# n = int(input("n= "))
# sum = 0
# for i in range(n):
#     x = int(input("x= "))
#     if x < 0:
#         sum += x
# print(sum)

# 12. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са по-големи от предварително
# зададено число k.

# n = int(input("n= "))
# k = int(input("k= "))
# sum = 0
# for i in range(n):
#     x = int(input("x= "))
#     if x > k :
#         sum += x
# print(sum)


# 13. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са по-малки от предварително
# зададено число u и по-големи от предварително зададено число v (u&gt;v).


# n = int(input("n= "))
# k = int(input("k= "))
# v = int(input("v= "))
# sum = 0
# for i in range(n):
#     x = int(input("x= "))
#     if x < k and x > v:
#         sum += x
# print(sum)



# 14. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичното само на онези от тях, които са по-големи от
# предварително зададено число k.


# n = int(input("n= "))
# k = int(input("k= "))
# sum = 0
# count = 0
# for i in range(n):
#     x = int(input("x= "))
#     if x > k :
#         sum += x
#         count += 1
# print(sum / count)




# 15. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичното само на онези от тях, които са по-малки от
# предварително зададено число u и по-големи от предварително зададено
#число v (u&gt;v).


# n = int(input("n= "))
# k = int(input("k= "))
# v = int(input("v= "))
# sum = 0
# count = 0
# for i in range(n):
#     x = int(input("x= "))
#     if x < k and x > v :
#         sum += x
#         count += 1
# print(sum / count)



# 16. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичната стойност на всички четни числа и
# произведението на всички нечетни числа.

# n = int(input("n= "))
# s = 0
# p = 1
# for i in range(n):
#     x = int(input("x="))
#     if x % 2 == 0:
#         s += x
#     else:
#         p *= x

# print("s= ",s, " p= ",p)


# 17. Да се състави програма, която въвежда две цели числа и извежда
# произведението им само ако произведението е по-голямо от 1000. В
# противен случай да се изведе тяхната сума.

# a = int(input("a= "))
# b = int(input("b= "))

# p = a*b
# if p > 1000:
#     print(p)
# else:
#     print(a+b)


##################################### Задачи 2 ##########################################

# import random

# Задачи с функции

# 1. Напишете програма с функция, която създава вложен списък. Размерите на
# списъка се указват като аргументи на функцията. Списъкът се запълва със
# случайни букви.

# def li(k,m):
#     lim = [[random.randint(0,10) for i in range(m)] for j in range(k)]

#     return lim

# print(li(4,3))


# 2. Напишете програма с функция за запълване на вложен списък. Списъкът се
# запълва с естествени числа на принципа на „змията“: най-напред се запълва
# първият ред, след това последната колона (от горе надолу), последният ред (от
# дясно на ляво), първата колона (отдолу нагоре), вторият ред (от ляво на дясно) и
# т.н.

"""
    Пример: snake = [
                        [1,2,3]
                        [8,9,4]
                        [7,6,5]
                    ]
"""

# def snake(n):
#     li = [[0 for i in range(n)] for j in range(n)]
#     move = 0    # 0 - right, 1 - down, 2 - left, 3 - up, -1 - stop

#     i = j = 0
#     el = 0
#     while move != -1:
#         el += 1

#         if li[i][j] == 0:
#             li[i][j] = el
#         else: 
#             break

#         # moving
#         if move == 0: # right
#             if j == n-1 or li[i][j+1] != 0:
#                 i += 1
#                 move = 1
#                 continue
#             else:
#                 j += 1
#         if move == 1: # down
#             if i == n-1 or li[i+1][j] != 0:
#                 j -= 1
#                 move = 2
#                 continue
#             else:
#                 i += 1
#         if move == 2: # left
#             if j == 0 or li[i][j-1] != 0:
#                 i -= 1
#                 move = 3
#                 continue
#             else:
#                 j -= 1
#         if move == 3: # up
#             if li[i-1][j] != 0:
#                 j += 1
#                 move = 0
#             else:
#                 i -= 1

#     for x in range(n):
#         print("[", end="")
#         for y in li[x]:
#             print(str(y).center(3), end=" ")
#         print("]")

# snake(9)


# 3. Напишете програма, в която се създава вложен списък от случайни числа. В
# матрицата, която се реализира от дадения вложен списък се изтрива ред и
# колона. Номерът на реда и номерът на колоната, които трябва да бъдат изтрити,
# се въвеждат от потребителя.

# import random


# def list_pr(li,n):  
#     for x in range(n):
#         print("[", end="")
#         for y in li[x]:
#             print(str(y).center(3), end=" ")
#         print("]")

# def rand_list(n):
#     li = []

#     for i in range(n):
#         li.append([])
#         for j in range(n):
#             li[i].append(random.randint(0,10))
        
#     return li

# def remove():
#     li = rand_list(5)
#     list_pr(li,5)

#     # k - ред
#     k = int(input("k= "))
#     li.pop(k)

#     # m - колона
#     m = int(input("m= "))
#     for i in range(4):
#         li[i].pop(m)
#     list_pr(li,4)


# remove()


# 4. Напишете програма, в която се изпълнява сортиране по възходящ ред по метода
# на мехурчето. Методът е следният: последователно се сравняват стойностите на
# съседните елементи и ако стойността на елемента от ляво е по-голяма от
# стойността на елемента от дясно, елементите разменят местата си. За едно
# пълно обхождане на елементите в списъка елементът с най-голяма стойност ще
# се окаже последен в списъка. На второто обхождане предпоследният елемент
# ще се окаже елементът с втора по големина стойност и т.н.

# li = [6,4,5,3,7,5,2,3,8,5,4,3,2,1,9]
# def bubble(li):
#     for j in range(len(li)):
#         for i in range(len(li) - 1):
#             if li[i] > li[i+1]:
#                 li[i], li[i+1] = li[i+1], li[i]
#     return li
# li = bubble(li)
# print(li)


# 5. Напишете програма с функция, която за списък, предаден като аргумент, връща
# списък от два елемента: стойността на най-големия елемент в списъка и индекса
# на този елемент в списъка (ако такива елементи има няколко, то индекса на
# първия от тях).

# def max_num(li):
#     max = li[0]
#     index = 0
#     for i in range(1,len(li)):
#         if li[i] > max:
#             max = li[i]
#             index = i
#     return [max,index]
# li = [4,5,3,65,23,45,6,2,1,3,45]
# max = max_num(li)
# print(max)



##################################### Задачи 3 ##########################################



# 1. Напишете програма, в която се създава функция с два аргумента, явяващи се
# числови списъци. Резултатът се явява число, равно на сумата от двойките
# произведения на елементите на списъците. Ако в един от списъците елементите
# са по-малко от другия, то недостигащите елементи се получават посредством
# циклично повторение на съдържанието на списъка.

# def sum_list(li1,li2):
#     if len(li1) >= len(li2):
#         s_li, b_li = li2, li1
#     else:
#         s_li, b_li = li1, li2

#     sum = 0
#     for i in range(len(b_li)):
#         j = i % len(s_li)
#         sum += s_li[j] + b_li[i]

#     return sum


# li1 = [1,2,3,4,5,6,7,8,9,10]
# li2 = [10,11,12,13,14,15]

# li1 = [1,2,3]
# li2 = [1,2,3,4,5]

# print(sum_list(li1,li2))



# 2. Съставете програма с функция, която получава като аргумент числов списък и
# връща като резултат друг списък, в който са включени само четните числа от
# списъка аргумент.

# def e_li(li):
#     li = [x for x in li if x % 2 == 0]
#     return li

# li = [1,2,3,4,5,6,7,8,9]

# print(li)
# print(e_li(li))


# 3. Напишете програма с функция с произволен брой числови аргументи, която
# връща като резултат списък от три елемента: средноаритметичната,
# максималната и минималната стойност на аргументите.

# def amami(*li):
#     return [sum(li) / len(li), max(li), min(li)]

# res = amami(1,5,8,54,3,4)
# print(res)


# 4. Да се състави програма с функция с един текстов аргумент и произволен брой
# целочислени аргументи. Резултатът се явява текст, сформиран от буквите на
# първия текстов аргумент. Целочислените аргументи определят индексите на
# буквите, които трябва да влязат в текста резултат.

# def func(s, *xs):
#     return ''.join([s[j] for j in [i for i in xs]])

# st = "This is the text!"

# res = func(st, 3,4,5,6,7,2,3)
# print(res)


# 5. Да се състави програма с функция, която получава като аргументи референция
# към функция и две цели числа. Функцията връща като резултат най-голямата
# стойност на предадената като първи аргумент функция в целочислените точки
# на диапазона, границите на които се определят от втория и третия аргумент.

# def f(x):
#     return 2*x*x - 4*x + 3

# def max_x(f,a,b):
#     y = []
#     for i in range(a,b+1):
#         y.append(f(i))
#     return max(y)

# res = max_x(f,3,7)
# print(res)


# 6. Напишете програма, в която по метода на рекурсията символите от текста,
# предаден като аргумент на функцията, се изобразяват „през един“: т.е. изписва
# се първият, третият, петият и т.н. символ.

# def mod_str(text):
#     if text == "":
#         return ""
#     return text[0] + mod_str(text[2:])

# txt = "abcdefghi"
# print(mod_str(txt))


# 7. Да се състави програма с използване на функция генератор, създаваща
# итерируем обект с имената на месеците.

# def get_months(month):
#     for m in month:
#         yield m

# months = ['January', 'February', 'March', 'April', 'May', 'June',
#           'July', 'August', 'September', 'Oktober', 'November', 'December']
# for m in get_months(months):
#     print(m)


# 8. Да се състави програма с функция генератор, създаваща итерируем обект със
# степени на двойката. Броят на елементите се определя от аргументите на
# функцията генератор.

# def pows(n):
#     for x in range(n):
#         yield 2**x

# for r in pows(4):
#     print(r, end=" ")


# 9. Съставете клас на Python с името Student с две свойства: student_id и
# student_name. Добавете ново свойство student_class. Създайте функция за
# извеждане на цялото свойство и техните стойности в класа Student.

# class Student:
#     def student_id(self,id):
#         self.id = id

#     def student_name(self,name):
#         self.name = name

#     def student_class(self,c):
#         self.cl = c

# def pr(st):
#     print(st.__dict__)

# John = Student()
# John.student_id(101)
# John.student_name("John")
# pr(John)


# 10. Съставете програма на Python с използването на клас за преобразуване на цяло
# десетично число в римския му еквивалент и обратно.

# class Transfer:
#     def __init__(self, num) -> None:
#         self.num = num
#         self.rome = {
#             'M' :   1000,
#             'CM':   900,
#             'D' :   500,
#             'CD':   400,
#             'C' :   100,
#             'XC':   90,
#             'L' :   50,
#             'XL':   40,
#             'X' :   10,
#             'IX':   9,
#             'V' :   5,
#             'IV':   4,
#             'I' :   1
#         }

#     def to_roman(self):
#         roman = ''
#         dec = self.num
#         for k,v in self.rome.items():
#             while dec // v != 0:
#                 roman += k
#                 dec -= v
#         return roman
    
#     def to_dec(self):
#         roman = self.num
#         dec = 0
#         for k,v in self.rome.items():
#             while roman[0:len(k)] == k:
#                 dec += v
#                 roman = roman[len(k):]
#         return dec

# print(Transfer(1800).to_roman())
# print(Transfer("MDCCCXIX").to_dec())



# 11. Да се състави програма на Python с използването на клас за обръщането на низ
# дума по дума.

# class Reverse:
#     def rev_str(self,s):
#         return ' '.join(reversed(s.split()))
# print(Reverse().rev_str("This stirng is reversed."))


# 12. Да се състави програма с използването на клас с два метода get_String и
# print_String. Методът get_String приема символен низ от потребителя, а
# print_String извежда символния низ с главни букви.


# class Str:
#     def get_String(self,text):
#         self.txt = text
    
#     def print_String(self):
#         print(self.txt.upper())

# s = Str()
# s.get_String("this will be uppercased.")
# s.print_String()


# 41.	Напишете клас на Python, за да получите всички възможни уникални подмножества от набор от различни цели числа.
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

# class comb:
#     def comb_li(self,li,cur=[]):
#         while li:
#             return self.comb_li(li[1:],cur) + self.comb_li(li[1:],cur + [li[0]])
#         return [cur]
# print(comb().comb_li([4,5,6]))



"""
    1. Клас, който представя студентите във вашата група.
    2. Напишете метод, който записва данни във файла, чете файла и създава списък на студентите.
    3. Напишете метод, който по дадено име добавя само студенти, които не са записани в списъка от студенти.
    4. Напишете метод remove за триене със слаб успех.
    5. Напишете метод за намиране на среден успех на група.
    6. Напишете метод за намиране на минимален и максимален успех на групата.
    7. Напишете метод copy, който да копира студенти с начална буква 'А' в нов списък, който метода връща.
    8. Напишете метод, който връща данните за студентите с един и същи успех.
    9. Напишете метод, който връща данни за студентите с четен фак. номер и максимален успех.
    10. Напишете метод move, който мести студенти с отличен успех в нов списък.
    11. Напишете метод, който връща данните за студенти с един и същи успех.
    12. Напишете метод, който връща данни за студент с четен фак. номер и минимален успех.
    13. Напишете метод, който връща данни за студентите само с големи букви
"""

# class Student:
#     def __init__(self):
#         #1
#         self.group = {
#                 "Bob" : 3,
#                 "Anna": 4,
#                 "Reac": 5
#         }

#     #2
#     def insert(self):
#         with open('data.txt', "w+") as data:
#             data.write(str(self.group))
#             data.seek(0)
#             txt = data.read()
#             return txt
    
#     #3
#     def add(self, name, mark):
#         if name not in self.group.keys():
#             self.group[name] = mark

#     #4
#     def rm(self):
#         self.group = {k:v for k,v in self.group.items() if v != 2}

#     #5
#     def avg(self):
#         return sum(self.group.values()) / len(self.group.values())

#     #6
#     def max_min(self):
#         marks = list(self.group.values())
#         max = min = marks[0]
#         for i in range(1,len(marks)):
#             if max < marks[i]:
#                 max = marks[i]
#             if min > marks[i]:
#                 min = marks[i]
#         print("max= ", max)
#         print("min= ", min)

#     #7
#     def new_li(self):
#         new_li = {}
#         for k,v in self.group.items():
#             if k[0] == 'A':
#                 new_li[k] = v
#         return new_li

#     #8
#     def same_mark(self):
#         s = set(self.group.values())
#         for m in s:
#             for k,v in self.group.items():
#                 if v == m:
#                     print("{} : {}".format(k,v), end="   ")
#             print()

#     #9


# # print(Student().insert())
# group = Student()
# group.add("fd", 2)    
# group.add("ds", 2)
# group.add("as", 3)
# group.rm()
# print(group.insert())
# print(group.avg())
# group.max_min()
# group.same_mark()




# class Student:    
#     def __init__(self,fnum,name,mark):
#         self.fnum = fnum
#         self.name = name
#         self.mark = mark
    
#     def __str__(self):  # metod za printirane
#         return'['+str(self.fnum)+','+self.name+'.'+str(self.mark)+']'

 
# class StudentGroup:
#     def __init__(self):
#         self.group = []

#     def append(self,student):
#         self.group.append(student)

#     def __str__(self):
#         #return str([str(student) for student in self.group])
#         result = ''
#         for student in self.group:
#             result += str(student)+''
#         return result

# def min_mark(self):
#     min = self.group[0]
#     for student in self.group:
#         if (min.mark > student.mark):
#             min = student
#     return min

# def max_mark(self):
#     max = self.group[0]
#     for student in self.group:
#         if (max.mark < student.mark):
#             max = student
#     return max

# def average_mark(self):
#     sum = 0
#     for student in self.group:
#         sum += student.mark
#     return round(sum/len(self.group))

# def sort(self):
#     for i in range(len(self.group)):
#         min = i
#         for j in range(i+1,len(self.group)):
#             if self.group[min].mark > self.group[j].mark:
#                 min = j

#         temp = self.group[i]
#         self.group[i] = self.group[min]
#         self.group[min] = temp