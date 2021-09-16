# Задача № 3 через функции.
from Functions import get_money, exchange_CNY, exchange_CHF, exchange_EUR, exchange_GBP, exchange_USD

def main():
    input_money = get_money()
    USD_money = exchange_USD(input_money)
    EUR_money = exchange_EUR(input_money)
    CHF_money = exchange_CHF(input_money)
    GBP_money = exchange_GBP(input_money)
    CNY_money = exchange_CNY(input_money)
    print("Ты ввёл", input_money, "BYN")
    print("Конвертированная сумма в USD =", USD_money)
    print("Конвертированная сумма в EUR =", EUR_money)
    print("Конвертированная сумма в CHF =", CHF_money)
    print("Конвертированная сумма в GBP =", GBP_money)
    print("Конвертированная сумма в CNY =", CNY_money)

main()