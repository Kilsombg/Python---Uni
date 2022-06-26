########################### Лабораторно упражнение 5 ############################

# import random

# s = [1,3,5,7]
# print(s[1],4) # 3 4

# s[1] = 1
# print(s)

# s = [1,2,3,4,5,6]
# print(s[::-1]) # извеждане на елементите в обратен ред
# print(s[:-1]) # принтиране без последния елемент
# print(s[1:]) # принтиране без първия елемент
# print(s[0:2]) # принтиране на първите два елемента
# print(s[-1:]) # принтиране на последния елемент

# s = [1,2,3,4,5,6]
# s1 = [9,8]
# s2=s+s1
# print(s2)

# s = [1,2,3,4,5,6]
# for i in s:
#     print(i)

# s=[1,2,3,4,5,6]
# for i in s:
#     print(i, end="")

# s = [1,2,3,4,5,6]
# for i in range(len(s)):
#     print(s[i],end="")

# s = [[1,2,3,4,5],['a','b','c'],[10,20]]
# print(s[0][3])
# print(s[2][0])

# s=[2,4,6,8]
# print(4 in s)
# print(9 in s)

# s = [2,4,6,8,2]
# print(s.count(2)) #2 колко пъти съдържа 2 в листа
# #print(s.index(3)) #ValueError:3 is not in list
# print(min(s)) #2
# print(max(s)) #8

# s = [2,4,6,8,2]
# s.append(22)
# print(s)

# s+=[[44,88]]
# print(s)

# #insert (<индекс>, <обект>)
# s.insert(0,90) # index 0 is "=" 90
# print(s)

# s.pop(0)
# print(s)

# s.remove(2)
# print(s)

# del s[4]

# # shuffle
# print("Shuffle")
# import random
# s = [2,4,6,8,2]
# random.shuffle(s)
# print(s)
# print(random.choice(s))
# s.reverse()
# print(s)

# #sort()
# #sort(<key=None>,<reverse False>) #reverse True
# #key = str.lower
# print("Sort")
# s = [45,10,55,5,35]
# s.sort()
# print(s)

# s.sort(reverse =True)
# print(s)
# s.sort(reverse = False)
# print(s)

# s1 = ["s","T","a","E","f"]
# s1.sort(key = str.lower)
# print(s1)
# s1.sort()
# print(s1)


# a = 0
# run = True
# def count(a,run):
#     a += 1
#     print("a = ", a)
#     if a >= 5:
#         run = False
#         return True
#     else:
#         return False
        
# while run:
#     if count(a,run) == True:
#         print("finished")
#     else:
#         print("No")





############################### Лабораторно 6 ###########################3

# li = list()
# print(li)
# li =   []
# print(li)
# li = [1,2,3,4,5]
# print(li)
li = list([1,2])
# print(li)

# li.append(11)
# print(li)
# li[len(li):] = [22]
# print(li)
# li += [44]
# print(li)
# li.extend([33])
# li.insert(0,77) # 0 is the index, 77 is the value
# print(li)

# li.remove(1)
# print(li)
# #li.remove(0) # търси се value не индекс
# print(li.pop())
# print(li)
# print(li.pop(0)) # 0 е индекс
# print(li)
# li.clear()
# print(li)
# del li[:]

# li = list([44,33,1,2,-1,3,4,-4,5,6,7,11,22,33])
# #print(li.index(0))
# print(li.index(1))
# print(li)
# print(li.index(2,0,8))
# print(li.count(0))

# print(li)
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)

# li.reverse()
# print(li)

# li1 = li.copy()
# print(li1)
# li1.append(-33)
# print(li)
# print(li1)
# li2 = li[:]
# print(li2)

# def create(m,n):
#     li = []
#     for x in range(m,n+1):
#         li.append(x)
#     return li

# print(create(1,10))
# print(list(map(lambda x: x, range(1,11))))


# def doubled(x):
#     return 2*x

# # list comprehensions
# print([doubled(x) for x in range(1,11)])
# print([x**2 for x in range(1,11)])
# print([(x,y) for x in [1,2,3] for y in [3,2,5]])
# print([(x,y) for x in [1,2,3] for y in [3,2,5] if x != y])

# li = []
# for x in [1,2,3]:
#     for y in [3,2,5]:
#         if x!=y:
#             li.append((x,y))
# print(li)

# print([(x, x**3) for x in range(1,11)])

# li = list([44,1,2,3,4,-11,5,6,7,11,22,33])
# print([x for x in li if x >= 0])
# print([abs(x) for x in li])

# import math
# print(math.pi)
# print(str([round(math.pi,i) for i in range(1,6)]))


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print([[row[i] for row in matrix] for i in range(3)])

# trans = []
# for i in range(3):
#     trans_row = []
#     for row in matrix:
#         trans_row.append(row[i])

# print(trans)