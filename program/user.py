
# Напишите программу (файл user.py),
# которая запрашивала бы у пользователя:
# его имя (например, "What is your name?")
# возраст ("How old are you?")
# место жительства ("Where are you live?")
# После этого выводила бы три строки:
# "This is `имя`"
# "It is `возраст`"
# "(S)he live in `место_жительства`"

name = input("What is your name?\n")
age = input("How old are you?\n")
location = input("Where are you live?\n")
print("This is " + name)
print("It is " + age)
print("(S)he lives in " + location)
