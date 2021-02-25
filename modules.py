# №1
# Внутри my_module.py создайте вызваннную print 
# которая выводит текст "Я функция из my_module.py". 
# А затем импортируйте my_module.py в другой файл.
# print("Я функция из my_module.py")

# №2
# Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", 
# "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] 
# и вытащите 4 рандомных имени оттуда и сохраните в другой список.
# 1)import random
# imena = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# imena2 = []
# i = 0
# random.choice(imena)
# while i < 4:
#     print(random.choice(imena))
#     i += 1
# imena2.append(random.choice(imena))
# print(imena2)

# 2)import random
# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# names2 = []
# i = 0
# random.choice(names)
# while i < 4:
#     print(random.choice(names))
#     i = i+1
# names2.append(random.choice(names))
# print (names2)


# №3
# Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.
# import sys
# print(sys.platform)
# OS name is "Linux"

# import os
# print(os.name)
# 
# №4
# Через терминал передайте Python несколько аргументов, а затем выведите их на экран.

# import sys
# print("hi {}. how are you?. {}".format(sys.argv[1],sys.argv[2]))
# # import sys
# print("Привет {}. Как дела?. {}".format(sys.argv[1],sys.argv[2]))


# №5
# Через Python у себя на рабочем столе создайте директорию, 
# а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
# import os
# import random

# os.mkdir('/home/azim/Desktop/modulesprob5')
# i = 0
# while i < 5:
#     a = random.randint(1, 1000)
#     os.mknod(f'/home/azim/Desktop/modulesprob5/file{a}.txt')
#     i +=1
# print(i)

# №6
# Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.
# import random
# list1 = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", 
#  "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# listTeam = 3
# l = []
# l1 = []
# l2 = []
# l3 = []
# i = 1
# while i <= listTeam:
#     h = random.choice(list1)
#     l.append(h)
    

#     for x in range(int(len(list1))):
#         if list1 == l:
#             del list1[x]
#             break

#     i += 1
# print(l)
# i = 1
# while i <= listTeam:
#     h = random.choice(list1)
#     l1.append(h)
    

#     for x in range(int(len(list1))):
#         if list1 == l1:
#             del list1[x]
#             break

#     i += 1
# print(l1)
# i = 1
# while i <= listTeam:
#     h = random.choice(list1)
#     l2.append(h)
    

#     for x in range(int(len(list1))):
#         if list1 == l2:
#             del list1[x]
#             break

#     i += 1
# print(l2)
# i = 1
# while i <= listTeam:
#     h = random.choice(list1)
#     l3.append(h)
    

#     for x in range(int(len(list1))):
#         if list1 == l3:
#             del list1[x]
#             break

#     i += 1
# print(l3)

# №2.1
# Напишите программу которая будет принимать аргументы sys.argv
# и выводить на экран оттуда всё что передал пользователь.


# №2.2
# Спросите у пользователя 2 значения через input() а затем через модуль sys 
# проверьте какое из 2-х значений занимает больше памяти.

# a = int(input("Bishkek"))

# 3. Определить дату, которая наступит через 1000 дней от текущей даты
#