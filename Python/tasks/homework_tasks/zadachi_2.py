import random

# Задачи с функции

# 1. Напишете програма с функция, която създава вложен списък. Размерите на
# списъка се указват като аргументи на функцията. Списъкът се запълва със
# случайни букви.

# def rand_list(row, col):
#     list = []
#     for i in range(row):
#         list.append([])
#         for j in range(col):
#             list[i].append(random.randint(0,10))

#     return list

# list = rand_list(3,4)
# print(list)
###########################################

# 2. Напишете програма с функция за запълване на вложен списък. Списъкът се
# запълва с естествени числа на принципа на „змията“: най-напред се запълва
# първият ред, след това последната колона (от горе надолу), последният ред (от
# дясно на ляво), първата колона (отдолу нагоре), вторият ред (от ляво на дясно) и
# т.н.

# def snake(n):
#     list = []
#     for i in range(n):
#         for j in range(n):
#             list[i][j] = 0
#     print(list)
#     count = 0
#     snakef(1,n,list,count)

# def snakef(row,n, list,count):
#         for j in range(n): #от начало надясно
#             list[row][j] = count
#             count += 1
#         for i in range(n): # в края надолу
#             list[i][n-1] = count
#             count += 1
#         for j in range(n-1,-1,-1): # от долу дясно - наляво
#             list[n][j] = count
#             count += 1
#         for i in range(n,row,-1):# долу ляво - нагоре
#             list[i][0] = count
#             count += 1
#         if row > n // 2:
#             return
#         snakef(row+1,n-1,list,count)

# snake(5)
# print(list)



# 3. Напишете програма, в която се създава вложен списък от случайни числа. В
# матрицата, която се реализира от дадения вложен списък се изтрива ред и
# колона. Номерът на реда и номерът на колоната, които трябва да бъдат изтрити,
# се въвеждат от потребителя.


# 4. Напишете програма, в която се изпълнява сортиране по възходящ ред по метода
# на мехурчето. Методът е следният: последователно се сравняват стойностите на
# съседните елементи и ако стойността на елемента от ляво е по-голяма от
# стойността на елемента от дясно, елементите разменят местата си. За едно
# пълно обхождане на елементите в списъка елементът с най-голяма стойност ще
# се окаже последен в списъка. На второто обхождане предпоследният елемент
# ще се окаже елементът с втора по големина стойност и т.н.


# 5. Напишете програма с функция, която за списък, предаден като аргумент, връща
# списък от два елемента: стойността на най-големия елемент в списъка и индекса
# на този елемент в списъка (ако такива елементи има няколко, то индекса на
# първия от тях).