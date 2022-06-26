############################# Лаботаторно Упражнение 6 #########################

# теория

# # множества
# s = set([1, 2, 3, 1]) #list
# print("s = ", s)
# s2 = set("hello") #string

# # операции с множества
# # обхождане на множество
# s2 = set("hello")
# for i in s2:
#     print(i, end=' ') # l h e o
# print()

# #- функция len()
# print(len(s2)) # 4

# #- обединение на множества:
# s = set([1, 2, 3])
# s1 = set([4, 2, 6])
# s3 = s | s1
# print(s3) # {1, 2, 3, 4, 6}

# #- разлика на множества:
# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s2 = s - s1
# print(s2) # {1, 3}
# s3 = s1 - s
# print(s3) # {6 }

# #- пресичане на множества
# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s4 = s & s1
# print(s4) # {2, 4}

# # - оператор ^
# # изключващо или
# # bit A   bit B   XOR
# # 0        0       0
# # 0        1       1
# # 1        0       1
# # 1        1       0

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s5 = s ^ s1
# print(s5) # {1, 3, 6}

# 3 in s # True

# # методи на множествата
# # add(<елемент>)
# # remove(<елемент>)
# # discard(<елемент>)
# # pop()
# # clear()


# примери

# s1 = set([2, 4, 6])
# s1.add(8) # {8, 2, 4, 6}
# s1.remove(2) # {8, 4, 6}
# print(s1)
# # s1.remove(2) # KeyError:2


# s = set()
# print(s)
# s = {1,2,3,4,5,6,7,8,9}
# print(s)

# print(3 in s) 
# print(3 not in s)




# # set comprehension
# print({x for x in 'abracadabra'})
# print({x for x in 'abracadabra' if x not in 'abc'})