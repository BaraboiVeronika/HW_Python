# Задача № 4 через функции.
from Functions import get_money, exchange_USD, exchange_GBP, exchange_EUR, exchange_CNY, exchange_CHF, get_currency

def main2():
    input_money = get_money()
    input_currency = get_currency()
    if input_currency == 1:
        print("Ты ввёл", input_money, "BYN")
        print("Конвертированная сумма в USD =", exchange_USD(input_money))
    elif input_currency == 2:
        print("Ты ввёл", input_money, "BYN")
        print("Конвертированная сумма в EUR =", exchange_EUR(input_money))
    elif input_currency == 3:
        print("Ты ввёл", input_money, "BYN")
        print("Конвертированная сумма в CHF =", exchange_CHF(input_money))
    elif input_currency == 4:
        print("Ты ввёл", input_money, "BYN")
        print("Конвертированная сумма в GBP =", exchange_GBP(input_money))
    elif input_currency == 5:
        print("Ты ввёл", input_money, "BYN")
        print("Конвертированная сумма в CNY =", exchange_CNY(input_money))

main2()
