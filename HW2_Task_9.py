# 9) Сделать скрипт используя функцию input().
# 1. Функция должна на вход принимать целое число.
# 2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100))
# 3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

import random
your_number = int(input())
random1 = random.randint(1, 100)
random2 = random.randint(1, 100)
if your_number > random1:
    if your_number > random2:
        print("Вы ввели число =", your_number, ", которое больше", random1, "и", random2)
    elif your_number == random2:
        print("Вы ввели число =", your_number, ", которое больше", random1, "и =", random2)
    else:
        print("Вы ввели число =", your_number, ", которое больше", random1, "и меньше", random2)
elif your_number < random1:
    if your_number < random2:
        print("Вы ввели число =", your_number, ", которое меньше", random1, "и", random2)
    elif your_number == random2:
        print("Вы ввели число =", your_number, ", которое меньше", random1, "и =", random2)
    else:
        print("Вы ввели число =", your_number, ", которое меньше", random1, "и больше", random2)
else:
    if your_number < random2:
        print("Вы ввели число =", your_number, ", которое равно", random1, "и меньше", random2)
    elif your_number == random2:
        print("Вы ввели число =", your_number, ", которое равно", random1, "и", random2)
    else:
        print("Вы ввели число =", your_number, ", которое равно", random1, "и больше", random2)