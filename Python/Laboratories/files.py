# from os import linesep


# Понятие за плосък файл
# 1. разделяне на записите чрез запетая
# Пример1:
# Name, Address, Email
# ABC, Citty, A, abc.@xyz.com
# LMN, Citty, B, abc.@xyz.com
# PQR, Citty, C, abc.@xyz.com

# 2. разделяне на запсиите чрез разделител от вида \t или символ (#,&,||):
# Пример2:
# Name | ADDRESS | EMAIL
# ABC || CITY A || abc.@xyz.compile

# Понятие за текстов файл
# End-of-Line (EOL) \n

# 1. Отваряне на файл
# open(file,access mode)

# Пример3:
# my_file_handle = open ("mynewtextfile.txt")
# или:
# my_file_handle = open("D://test.txt")

# 2. четене на файл
# - read()
# - readline()
# - 

# Пример 5:
# my_file = open("test1.txt", "r")
# print(my_file.readLine())
# print(my_file.readLine(2))

# Резултат:
# 1st linesep

# 2n


# 3. Затваряне на файл:

# my_file.close()

# Пример 7: извеждането съдържанието на файла ред по ред чрез for цикъл:
# my_file = open("test1.txt","r")
# for line in my_file:
#     print(line)
# my_file.close()

# Резултат:

# 1st line

# 2nd line 

# 4rd line

# 5th line 

# with open(file.access mode) as f:

# 4. Запис във файл

# -write(string) (за текст)
# -write(byte_string) (за двоични данни)
# -writelines(list)

# Пример 8:
# new_file = open("newfile.txt", mode="w", ecoding="utf=8")
# new_file.write("Writing to a new file\n")
# new_file.write("Writing to a new file\n")
# new_file.write("Writing to a new file\n")
# new_file.close()

# 5. Режим на добавяне (а+):
# Пример 9:
# fruits = ["Orange\n", "Banana\n", "Apple\n"]
# new_file = open("newfile.txt", mode="a+",encoding = "utf-8")
# new_file.writelines(fruits)
# for line in new_file:
#     print(line)
# new_file.close()

# 6. Позициониране на курсора (seek())
# Пример 10:
# cars=["Audi\n","Bentley\n","Toyota\n"]
# new_file = open("newfile.txt",mode="a+")
# for car in cars:
#     new_file.write(car)
# print("Tell the byte at which the file cursor is:",new_file.tell())
# new_file.seek(0)
# for line in new_file:
#     print(line)

# Резултат:

# ##################################
# 7.Двоични файлове
# Пример 11:
# binary_file = open("binary_file.bin", mode="wb+")
# text = "Hello 123"
# encoded = text.encode("utf-8")
# binary_file.write(encoded)
# binary_file.seek(0)
# binary_data = binary_file.read()
# print("binary:", binary_data)
# text = binary_data.decode("utf-8")
# print("Decoded data:", text)

# Резултат:

# binary: b'Hello 123'
# Decoded data: Hello 123

# Пример 12:
# for byte in binary_data:
#     print(byte)

# Резултат:
# 72
# 101
# 108
# 108
# 111
# 32
# 49
# 50
# 51