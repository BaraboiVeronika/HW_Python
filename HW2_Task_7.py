# 7) Сделать скрипт, используя функцию input().
# 1. Функция должна на вход принимать целое число.
# 2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
age = int(input("Введите свой возраст:"))
if age > 30:
    print("Вы ввели число =", age, ", которое больше 30")
elif age < 30:
    print("Вы ввели число =", age, ", которое меньше 30")
elif age == 30:
    print("Вы ввели число =", age, ", которое равно 30")