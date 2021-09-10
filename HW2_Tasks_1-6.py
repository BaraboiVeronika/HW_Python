# 1) Создать 2 переменных типа String с разными значениями:
name1 = str("Hello")
name2 = str("World!")

# 2) Создать 4 переменных типа Integer с разными значениями:
num1 = 3
num2 = 4
num3 = 10
num4 = 125

# 3) Создать 3 переменных типа Float с разными значениями:
fl1 = 3.6
fl2 = 7.25
fl3 = 98.69

# 4) Реализовать 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты высвести в консоль:
if num1 > num2:
    print("4)", num1, ">", num2)
if num1 < num2:
    print("4)", num1, "<", num2)
if num1 >= num2:
    print("4)", num1, ">=", num2)
if num1 <= num2:
    print("4)", num1, "<=", num2)
if num1 != num2:
    print("4)", num1, "!=", num2)
if num2 > num3:
    print("4)", num2, ">", num3)
if num2 < num3:
    print("4)", num2, "<", num3)
if num2 >= num3:
    print("4)", num2, ">=", num3)
if num2 <= num3:
    print("4)", num2, "<=", num3)
if num2 != num3:
    print("4)", num2, "!=", num3)
if num3 > num4:
    print("4)", num3, ">", num4)
if num3 < num4:
    print("4)", num3, "<", num4)
if num3 >= num4:
    print("4)", num3, ">=", num4)
if num3 <= num4:
    print("4)", num3, "<=", num4)
if num3 != num4:
    print("4)", num3, "!=", num4)

# 5) Реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты высвести в консоль:
if fl1 > fl2:
    print("5)", fl1, ">", fl2)
if fl1 < fl2:
    print("5)", fl1, "<", fl2)
if fl1 >= fl2:
    print("5)", fl1, ">=", fl2)
if fl1 <= fl2:
    print("5)", fl1, "<=", fl2)
if fl1 != fl2:
    print("5)", fl1, "!=", fl2)
if fl2 > fl3:
    print("5)", fl2, ">", fl3)
if fl2 < fl3:
    print("5)", fl2, "<", fl3)
if fl2 >= fl3:
    print("5)", fl1, ">=", fl2)
if fl2 <= fl3:
    print("5)", fl2, "<=", fl3)

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль:
if num1 < num2 and num2 < num3:
    print("6)", num1, "<", num3)
if num1 > num2 and num2 > num3:
    print("6)", num1, ">", num3)
if num1 == num2 and num2 == num3:
    print("6)", num1, "=", num3)
if num2 > num1 or num3 > num2:
    print("6)", num3, ">", num1)
if num1 != num2 and num2 < num4:
    print("6)", num1, "не равен", num2, 'и', num1, "меньше чем", num4)
if not num1 == num2 or not num2 == num3:
    print("6)", num1, "не равен", num3)
if num1 + num4 > num2 + num3:
    print("6)", "сумма num1 и num4 > чем сумма num2 и num3")
if num1 <= num4 and num4 != num2:
    print("6)", num1, "<=", num4, ", которое не равно", num2)
if not num3 / num2 == num4 / num2:
    print("6)", "Деление num3 на num2 не равно делению num4 на num2")
if num1 <= num2 and num2 <= num3 and num3 <= num4:
    print("6)", num1, "меньше чем", num4)
