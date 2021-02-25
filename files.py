# №1С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога. 
# Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir.
# В итоге у вас на рабочем столе должен появиться файл directories.txt. 
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

# d = open('/home/azim/directories.txt', 'w')
# d.write('''Desktop/ Public/ Videos/ Documents/ Music/ 
# snap/ Рабочий стол/ Downloads/ Pictures/Template''')
# d.close

# №2Создайте файл users.txt. 
# Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.

# a = open('/home/azim/users.txt',  'w')
# login = input("login: ")
# password = input("password: ")
# a.write(f"login: {login},password: {password:}") 
# a.close()

# №3Создайте программу, которая считает из файла текст, и если в тексте содержится буква
#  “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. 
#  Подсказка: используйте ключевое слово in.

# s = open('exersice3.txt', 'r')

# if "T" or "t" in s.read():
#     print("yes")
# else:
#     print("no")

# №4 Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom:
# Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит
# букву “t” или “T”, то запишите его в список t_words = [ ]. После окончания списка,
# выведите на экран все полученные слова. Подсказка: используйте for.   
# a = open('python.txt', 'r')

# a.write('''Python is a widely used high-level programming language for general-purpose
# programming, created by Guido van Rossum and first released in 1991. An interpreted
# language, Python has a design philosophy that emphasizes code readability (notably
# using whitespace indentation to delimit code blocks rather than curly brackets or
# keywords), and a syntax that allows programmers to express concepts in fewer lines of
# code than might be used in languages such as C++ or Java.''')
# t_words = []
# c = a.read().split()
# for x in c:
#     if "t" in x:
#         t_words.append(x)
#     if "T" in x:
#         t_words.append(x)
# print(t_words)
# a.close()

# №2.1Создайте database.txt файл с несколькими логинами и паролями. 
# Затем попросите пользователя войти или зарегистрироваться.
# Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль.
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.
# 
# g = open('database.txt', 'w')
# a = input('login: ')
# b = input('password: ')
# c = input('login: ')
# d = input('password: ')
# g.write("login: {azim}, password: {azim}, login:{azim}, password:{123}")
# g.close()

# g = open('database.txt', 'r')
# if 'azim' in g:
#     print('такой логин уже существует.Зареистрируйтесь еще раз!')
# else:
#     print('nothing')
# g.close()

# g = open('database.txt', 'w')
# g.write("name: {a}, password: {b}")
# g.close()

# tryyy#2

# g = open('datebase.txt', 'w')
# a = input('login: ')
# b = input ('password: ')
# g.write('login:{azim}, password:{az123}')
# g.close()

# №2.2Создайте database.txt файл с несколькими логинами и паролями. 
# Затем попросите пользователя войти или зарегистрироваться.
# Спросите его логин и пароль. Если такой логин уже есть скажите ему что логин уже существует и предложите зарегистрироваться спросив пароль. 
# Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.



# №3.1Напишите программу которая спрашивает от пользователя 2 вещи:
# 1.Путь до картинки которую нужно изменить.
# 2.Путь до картинки НА которую нужно изменить.
# Если оба пути существуют перепишите первую картинку на вторую, 
# если нет скажите пользователю какой картинке не существует.


# №3.2озьмите текст #2 из Classroom и вставьте его в текстовый файл. 
# Возьмите данные из файла и сложите зарплату за
#  Май, Июль, Сентябрь и Ноябрь и посчитайте среднее арифмитечское за эти месяца.



# №4.1Создайте текстовый файл с целыми числами -> 
# а)Найти максимальное и минимальное число и записать в другой файл.

num_bers = open('numbers.txt', 'r')
num_bers.read()
# num_bers.write(f"[1, 2, 3, 4, 5]")
# num_bers.close()
# for x in num_bers:
#     if x == 5:
#         print("5-max")
#     if x == 1:
#         print("1-min")
# num_bers.close()
# print(max(num_bers))
# print(min(num_bers))
num_bers.close()
# №4.2Создайте текстовый файл -> 
# 1:Записать в него построчно данные, которые вводит пользователь
# 2:Окончание ввода должен принимать пустую строку
