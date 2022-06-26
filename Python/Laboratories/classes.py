#################### Лабораторно упражнение 8 ########################

# създаване на клас с име и свойство:
# class MyFirstClass:
# x=5

# създаване на обект, базиран на създадения клас:
# MyFirstObject = MyFirstClass()

# достъпване елементите на класа:
# print(MyFirstObject.x)

# функция конструктур __init__()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# MyPerson = Person("Ivan", 35)
# print(MyPerson.name)
# print(MyPerson.age)

# Методи

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def greetings(self):
#         print("Hello, my name is " + self.name)

# MyPerson = Person("Ivan", 35)
# MyPerson.geretings()

# параметър self

# промяна стойностите на свойства на обекти:
#     MyPerson.age = 40

# изтриване свойства на обекти с del:
#     del MyPerson.age

# изтриване на цели обекти с del:
#     del MyPerson

# дефиниране на клас без съдържание (pass)
#     class Person:
#         pass



# Наследяване:

# Shape - base class (родител - parent)
# child - Triangle and Rectangle

# Родител, parent (Shape) - задава общи характеристики
# Наследник, child (Triangle and Rectangle) - задава специфични характеристики


# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname,self.lastname)

# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(self,fname,lname)







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

#     def print(self):
#         print(self.name, self.family, self.nationality, self.age)
    
# John = Person("John","Deretski",25,"bulgarian")
# Polia = Person("Polia","Gesheva",22,"bulgarian")
# John.print()
# Polia.print()


# Задача 2:
# Да се добави към кода от Задача 1 клас Student, наследник на класа Person с две нови полета
# – университет (university) и година на обучение (yearofstudy). Да се предифинира за него методът print,
#  така, че да отпечатва и тези две полета. Да се създадат инстанции на новия клас и за тях да се извика
#  методът print.

# class Student(Person):
#     def __init__(self, name, family, age, nationality, university, yearofstudy):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.yearofstudy = yearofstudy

#     def print(self):
#         print(f"{self.name} {self.family} {self.age} {self.nationality} {self.university} {self.yearofstudy}")

# Georgi = Student("Georgi","Bankov", 19, "bulgarian", "Tehnical University" , 2001 )
# Georgi.print()


# Да се добави: class Lecturer, наследник на Person
#  с две нови полета university, experience - брой години, преподавателски стаж 
# да  се направи print, така че да отпечатва тези две полета

# class Lecturer(Person):
#     def __init__(self, name, family, age, nationality, university, experience):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.experience = experience

#     def print(self):
#         print(f"{self.name} {self.family} {self.age} {self.nationality} {self.university} {self.experience}")

# Kaloqn = Lecturer("Kaloqn","Petrov", 35, "bulgarian", "Tehnical University" , 15 )
# Kaloqn.print()