# 1. Да се състави програма, която намира всички числа в интервала [1,1000], които
# завършват на 7.

# for i in range(1,1001):
#     if i % 10 == 7:
#         print(i);
###########################################

# 2. Да се състави програма, която изчислява сумата и произведението на всички
# числа от 1 до дадено число n.

# S = 0
# P = 1
# n = int(input("How much is n: "))

# for i in range(1,n+1):
#     S += i
#     P *= i

# print("S = ", S)
# print("P = ", P)
###########################################

# 3. Да се състави програма, която отпечатва таблицата за умножение за дадено
# число.

# n = int(input("Whrite a digit: "))

# for i in range(1,10):
#     print(f"{n} * {i} = ", n * i)
###########################################

# 4. Да се състави програма, която извежда числата от -10 до -1.

# for i in range(-10, 0):
#     print(i,end = " ")
###########################################

# 5. Да се състави програма, която извежда всички прости числа в диапазона от 25
# до 50.

# for i in range(25,50):
#     for j in range(2,i // 2 + 1):
#         if(i % j == 0):
#             break;
#     else:
#         print(i);

# for j in range(25,50):
#     for i in range(2, j // 2 + 1):
#         if j % i == 0:
#             break;
#         elif i == j//2:
#             print(f"j = {j}")
###########################################

# 6. Да се състави програма, която извежда следния модел:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#     print("*" * i)
# for i in range(4,0,-1):
#     print("*"*i)
###########################################

# 7. Да се състави програма, която обръща цифрите на дадено число:

# Пример: Дадено е числото 76542
# Да се изведе: 24567

# x = 76542
# #x = int(input("Write the number"))

# x = str(x)
# for i in range(len(x)-1,-1,-1):
#     print(x[i], end = "")
###########################################

# 8. Да се състави програма, която въвежда от клавиатурата n числа и сумира
# поотделно всички четни и нечетни числа. Програмата да извежда общата
# сума и за двата случая.

# SUM_EVEN = 0
# SUM_ODD = 0
# N = int(input("Write n: "))

# for i in range(N):
#     x = int(input(f"x{i}= "))
#     if x % 2 == 0 :
#         SUM_EVEN += x
#     else: 
#         SUM_ODD += x

# print(f"sum of even = {SUM_EVEN}")
# print(f"sum of odd = {SUM_ODD}")
###########################################

# 9. Да се състави програма, която въвежда n числа от клавиатурата и намира
# средноаритметичната им стойност (1≤n≤1000).

# COUNT = 0
# SUM = 0
# n = int(input("n= "))
#  if n < 1  or n > 1000:
#      n = int(input("n must be 1 <= n <= 1000"))

# for i in range(n):
#     x = int(input("x= " ))
#     COUNT+=1
#     SUM += x

# print("AVG = ", SUM / COUNT)


# 10. Да се състави програма, която въвежда n числа (n≤10) на брой реални числа
# по-малки от 1000 и намира тяхното произведение.

# n = int(input("How much numbers? "))
# if n > 10 :
#     print("n must be less than 10! ")
#     n = int(input("n = "))

# p = 1

# for i in range(n):
#     num = float(input("num = "))
#     p *= num

# print(p)
###########################################

# 11. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са отрицателни.

# sum = 0
# n = int(input("n = "))
# for i in range(n):
#     num = int(input("write a number: "))
#     if num < 0:
#         sum += num
# print(sum)
###########################################

# 12. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са по-големи от предварително
# зададено число k.

# n = int(input("n= "))
# k = int(input("k= "))
# sum = 0

# for i in range(n):
#     num = int(input("num = "))
#     if num > k:
#         sum += num
# print(sum)
###########################################

# 13. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира сумата само на онези от тях, които са по-малки от предварително
# зададено число u и по-големи от предварително зададено число v (u&gt;v).

# # v < x < u
# n = int(input("n= "))
# v = int(input("u= "))
# u = int(input("v= "))
# sum = 0

# for i in range(n):
#     x = int(input("X = "))
#     if x > v and x < u:
#         sum += x
# print(sum)
###########################################

# 14. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичното само на онези от тях, които са по-големи от
# предварително зададено число k.

# n = int(input("n = "))
# k = int(input("k= "))
# count = 0
# sum = 0

# for i in range(n):
#     num = int(input("num = "))
#     if num > k:
#         sum += num
#         count += 1
# print(sum / count)
###########################################

# 15. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичното само на онези от тях, които са по-малки от
# предварително зададено число u и по-големи от предварително зададено
#число v (u&gt;v).

# n = int(input("n = "))
# v = int(input("v = "))
# u = int(input("u = "))
# count = 0
# sum = 0

# for i in range(n):
#     num = int(input("num = "))
#     if num > v and num < u:
#         sum += num
#         count += 1
# print(sum / count)
###########################################

# 16. Да се състави програма, която въвежда n на брой числа от клавиатурата и
# намира средноаритметичната стойност на всички четни числа и
# произведението на всички нечетни числа.

# n = int(input("n = "))
# sum = 0
# p = 1
# count = 0

# for i in range(n):
#     num = int(input("num = "))
    
#     if num % 2 == 0:
#         sum += num
#         count += 1
#     else:
#         p *= num

# print("Average of even numbers is: ", sum / count)
# print("Product of odd numbers is: ", p)
###########################################

# 17. Да се състави програма, която въвежда две цели числа и извежда
# произведението им само ако произведението е по-голямо от 1000. В
# противен случай да се изведе тяхната сума.

x = int(input("x = "))
y = int(input("y = "))
p = x * y

if p > 1000:
    print(p)
else:
    print(x + y)
###########################################