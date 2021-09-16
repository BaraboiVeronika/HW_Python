# Задача № 4.
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
# 1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
# 2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
# 3. Потом Скрипт выводит "Введите сумму"
# 4. Пользователь вводит сумму int
# 5. Скрипт выводит:
# "Вы ввели сумму int и валюту "Валюта" "
# "конвертированная сумма в "Валюта" = int"
# 6. Скипт должен выдать сообщение
# "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#  7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
#  8. Валюту пользователя определите сами.

while True:
    input_currency = input("Выберите номер валюты: 1 - USD, 2 - EUR, 3 - CHF, 4 - GBP, 5 - CNY:  ")
    sum_BYN = input("Введите сумму: ")
    if sum_BYN == "":
        print("Вы ввели пустое поле. Введите число.")
    elif not sum_BYN.isalnum():
        print("Введите положительное число.")
    elif not sum_BYN.isnumeric():
        print("Вы ввели не число. Введите число.")
    if sum_BYN.isnumeric() and input_currency == "1":
        print("Вы ввели сумму BYN =", sum_BYN, "и валюту - USD.")
        print("Конвертированная сумма BYN в USD =", int(sum_BYN) / 2.4981)
    elif sum_BYN.isnumeric() and input_currency == "2":
        print("Вы ввели сумму BYN =", sum_BYN, "и валюту - EUR.")
        print("Конвертированная сумма BYN в EUR =", int(sum_BYN) / 2.9527)
    elif sum_BYN.isnumeric() and input_currency == "3":
        print("Вы ввели сумму BYN =", sum_BYN, "и валюту - CHF.")
        print("Конвертированная сумма BYN в CHF =", int(sum_BYN) / 2.7094)
    elif sum_BYN.isnumeric() and input_currency == "4":
        print("Вы ввели сумму BYN =", sum_BYN, "и валюту - GBP.")
        print("Конвертированная сумма BYN в GBP =", int(sum_BYN) / 3.4629)
    elif sum_BYN.isnumeric() and input_currency == "5":
        print("Вы ввели сумму BYN =", sum_BYN, "и валюту - CNY.")
        print("Конвертированная сумма BYN в CNY =", int(sum_BYN) / 3.8760)
