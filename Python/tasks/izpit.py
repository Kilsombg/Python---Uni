"""
Зад 1.
    Напишете проограма, в която потребителят въвежда n-брой цели числа от
    клавиатурата. Да се създадат два списъка - в единия да се запишат всички нечетни числа,
    кратни на 3, а в другия - всички четни числа, кратни на 2. За списъка, съставен от неетни
    числа, да се намери минималната и максималната сотйност на елементите, съставящи
    списъка. За списъка, съставен от четни числа, да се намери сумата и средно аритметичната
    стойност за елементите от списъка.
"""

# n = int(input("n= "))

# ch = []
# nch = []

# for i in range(n):
#     x = int(input("x= "))

#     if x % 3 == 0 and x % 2 != 0:
#          nch.append(x)
    
#     if x % 2 == 0:
#         ch.append(x)

# mi = min(nch)
# ma = max(nch)
# print("mi = ", mi)
# print("ma = ", ma)

# print()

# sum = sum(ch)
# print("avg = ", sum / len(ch))




"""
Зад 2.
    Да се състави програма на Python, която дефинира клас, GSM mobile devices", с
    полета: налично количество, единична цена, година на производство, производител, модел
    на мобилни устройства. Да се състави:
    - метод, който сортира моделите мобилни устройства по налично количество в нарастващ ред
    - метод, който премества всички модели мобилни устройства, произведени от един и същи
    производител в списък, записан в JSON файл

"""

# class GSMs:
#     def __init__(self, quantity, price, y_pr, pr, model):
#         self.quantity = quantity
#         self.price = price
#         self.y_pr = y_pr
#         self.pr = pr
#         self.model = model

#     def __str__(self):
#         return (" quantity :{} \n price: {} \n year of production: {} \n productor: {} \n model: {} \n".
#         format(self.quantity, self.price, self.y_pr, self.pr, self.model))


# class GSM_mobile_devices:
#     gsm_list = []

#     def insert_gsms(self, *x):
#         for i in x:
#             self.gsm_list.append(i)

#     def sorting(self): # bubble sort
#         for i in range(len(self.gsm_list)):
#             for j in range(i+1, len(self.gsm_list)):
#                 if self.gsm_list[i].quantity > self.gsm_list[j].quantity:
#                     self.gsm_list[i], self.gsm_list[j] = self.gsm_list[j], self.gsm_list[i]


#     def put_json(self, prod):
#         import json

#         with open("json.txt", "w") as f:
#             for i in self.gsm_list:
#                 if i.pr == prod:
#                     f.write(json.dumps(i.__dict__))




# samsung = GSMs(14, 300, 2010, "SAMSUNG", "Yi8")
# huawei = GSMs(12, 450, 2014, "HUAWEI", "P9")
# alcatel = GSMs(20, 140, 2005, "ALCATEL2000", "JKW-800")
# alcatel1 = GSMs(10, 180, 2006, "ALCATEL2000", "JKW-801")

# gsms = GSM_mobile_devices()
# gsms.insert_gsms(samsung, huawei, alcatel, alcatel1)
# gsms.sorting()
# gsms.put_json("ALCATEL2000")

# for i in gsms.gsm_list:
#     print(i)