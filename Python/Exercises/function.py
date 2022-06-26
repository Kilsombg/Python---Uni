# FUNCTIONS

# def <function_name([<parameters>]):
#     <statement(s)>
# <function_name>([<arguments>])


# Задача 1:
# Напишете програма, която намира лицето на геометрична фигура, като първо се въвежда вида на фигурата. 
# Първо квадртат, след това правоъгълник и правоъгълен триъгълник. За пресмятането на лицето на съответните
# фигуре да се запишат подходящи формули.

# # square
# def square():
#     a = int(input("a = "))
#     return a*a

# # rect
# def rect():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return a * b

# # right triangle
# def right_triangle():
#     a = int(input("a = "))
#     b = int(input("b = "))
#     return (a*b) / 2

# # usporednik
# def usporednik():
#     a = int(input("a = "))
#     ha = int(input("ha = "))
#     return a * ha

# # romb
# def romb():
#     a = int(input("a = "))
#     h = int(input("h = "))
#     return a * h

# while type != "":
#     type = input("What is the type of the figure: ")

#     if type == "square":
#         print(square())
#     elif type == "rect":
#         print(rect())
#     elif type == "right triangle":
#         print(right_triangle())
#     elif type == "usporednik":
#         print(usporednik())
#     elif type == "romb":
#         print(romb())