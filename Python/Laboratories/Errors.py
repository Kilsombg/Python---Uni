############################# Лабораторно упражнение 10 ####################

# #SyntaxError: invalid syntax
# while True print("Hello world")
#     File "<stdin>", line 1
#         while True print("Hello world")

#SyntaxError: Invalid syntax

#изключвания:
#1: ZeroDivisionError
# >>> 10 * (1/0)
# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>

# #try, except, finally
# try:
#     print(x)
# except:
#     print("An exception occured")

# ключова дума else
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")

# # ключова дума finally
# # try:
# #     print(x)
# # except:
# #     print("Something went wrong")
# # finally:
# #     print("The 'try except' is finished")

# # въвеждане на цяло число като вход от страна на потребителя:
# while True:
#     try:
#         x = int(input("Please enter a number:"))
#         break
#     except ValueError:
#         print("Oops! That was not a vlaid number. Try again...")

# # #
# # except(RuntimeError,TypeError, NameError):
# #     pass

# # ситуация на изключение при функция
# def this_fails():
#     x = 1/0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print("Handing run-time error: ", err)
#     #Handing run-time error: division by zero

# # ключова дума false
# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# # грешка TypeError, ако типът на x не е int
# x = "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# # грешка, върната от интерпретатора при генериране на ситуация HiThere:
# raise NameError("HiThere")