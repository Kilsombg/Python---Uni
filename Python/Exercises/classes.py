###################################### Exercise 9 #################################
# Задача 1:
# Съставете програма на Python с използването на клас за превръщане на число за преобръщането му
# от десетичен вид в римския му еквивалент и обратно

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
# Да се състави програма на Python с използването на клас за обръщането на низ дума по дума

# class RevSt:
#     def rev_sentence(self,sentence): 
#         words = sentence.split(' ') 
#         reverse_sentence = ' '.join(reversed(words)) 

#         return reverse_sentence 
  
# print(RevSt().rev_sentence(input))


##################################### Exercise 11 ################################

# Задача 1:
# Създайте клас, който представя студентите от вашата група.
# Напишете метод, който по дадено име създава само студенти, които не са създадени от списъка от студенти.

# Задача 2:
# и напишете метод remove за триене на студент с оценка слаб

# Задача 3:
# и напишете метод за намиране на среден успех

# class Group:
#     def __init__(self):
#         self.list = {
#             "Peter" : 5,
#             "George" : 4,
#             "Alicia" : 6,
#             "Patric" : 3,
#             "Sandra" : 2
#         }

#     def add_st(self,name,grade):
#         if name not in self.list.keys():
#             self.list[name] = grade

#     def remove(self):
#         self.list = {key:val for key, val in self.list.items() if val != 2}

#     def avg_score(self):
#         grades = self.list.values()
#         print(sum(grades)/self.list.__len__())

# group = Group()
# print(group.list)
# group.add_st("Silvia", 2)
# group.add_st("Peter", 2)
# print(group.list)

# group.remove()
# print(group.list)

# group.avg_score()