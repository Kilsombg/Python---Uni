####################### Лабораторно упражнение 6 #######################

# # операции при кортежите 

# k = (7, 5, 3, 6, 1)
# print(k[0]) # достъп до елемент по индекс
# print(k[2:3]) # сечение
# print(7 in k) # проверка за наличие на елемент
# print(k * 3) # повторение 
# tup = k + (2, 4) # конкатенация
# print(tup)

# # поддържани методи при кортежите

# tup = (7, 5, 3, 6, 1)
# print(tup.index(1)) # 4
# print(tup.count(5)) # 1

# # обхождане на елементите на кортеж
# for i in tup:
#     print(i, end=' ')
# print()


# t = ()
# print(t, len(t))
# t = 'hi',
# print(t, len(t))

# t1 = 'hi'
# print(t1, len(t1))
# t = 'hello','python','my','friend'  # packing
# print(t,len(t))
# a,b,c,d = t # unpacking
# print(a,b,c,d)