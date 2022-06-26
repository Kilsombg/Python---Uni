######################### Лабораторно упражнение 6 #####################

# теория
# # създаване на речник

# d = dict()
# d1 = dict(name = 'ivan', last_name = 'petrov')
# d3 = dict([('name', 'polina'), ('l_name', 'koleva')])
# print(d3)
# print(d1)



# # запълване на речник елемент по елемент
# d = { }
# d['name'] = 'petyr'
# d['l_name'] = 'kolev'
# #d = {'name': 'ivan', 'last_name': 'ivanov'}
# print(d)

# # операции с речници
# d = {'name': 'ivan', 'last_name': 'ivanov'}
# d['name']
# #print(d['fname']) # KeyError: 'fname'

# # проверка за наличие на ключ чрез оператор in
# b = 'fname' in d
# print(b) # False

# # определяне броя на ключовете в речника
# len(d)
# print(len(d)) #2

# # добавяне на елементи в речника
# d['s_name'] = 'petrov'
# print(d) # {'name': 'ivan', 'last_name': 'ivanov', 's_name': 'petrov'}

# # премахване на елемент от речник - използва се оператор del
# del d['s_name']
# print(d) # {'name': 'ivan', 'last_name': 'ivanov'}

# # методи keys() и values()
# keys = list(d.keys())
# keys.sort()
# for key in keys:
#     print("{0} => {1}".format(key, d[key], end = ' ')) # last_name => ivanov name => ivan



# примери

# dic = {}
# print(dic)
# dic = dict()

# dic = {'ivan':'123-123', 'petyr':'111-222'}
# print(dic)

# dic['lili'] = '444-333'
# print(dic)

# dic['petyr'] = '656-566'
# print(dic)

# del dic['ivan']
# print(dic)
# # del dic['ivan']

# print(list(dic))
# print(sorted(dic))

# dic = dict([('ivan','123-123'),('petyr','656-566'), ('maria', '111-222')])
# print(dic)

# dic1 = dict(ivan='123-123', petyr='656-566')
# print(dic1)

# # dict comprehensions
# print({x:x*2 for x in (1,2,3)})
# print({x:x*2 for x in range(1,11)})

# for k,v in dic.items():
#     print(f'{k}=>{v}')

# li = list([44,1,2,3,4,-11,5,6,7,11,22,33])
# for i,v in enumerate(li):
#     print('{0}=>{1}'.format(i,v))

# for v in reversed(li):
#     print('{0}'.format(v), end = ' ')
# print()

# for i in sorted(set(li)):
#     print(i,end=' ')
# print()

# print(li)