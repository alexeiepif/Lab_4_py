
#Напишите программу (файл arithmetic.py), 
#которая предлагала бы пользователю решить 
#пример 4 * 100 - 54. Потом выводила бы 
#на экран правильный ответ и ответ пользователя. 
#Подумайте, нужно ли здесь преобразовывать строку в число.

expression = "4 * 100 - 54"
expected_result = eval(expression)

user_answer = input("Solve the expression: 4 * 100 - 54 = ")

print("Correct answer:", expected_result)
print("Your answer:", user_answer)