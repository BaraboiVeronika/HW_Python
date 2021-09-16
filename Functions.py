
def get_money():
    while True:
        money = input("Введите сумму денег в BYN: ")
        if money == "":
            print("Вы ввели пустое поле. Введите число.")
        elif not money.isalnum():
            print("Введите положительное число.")
        elif not money.isnumeric():
            print("Вы ввели не число. Введите число.")
        else:
            return money


def exchange_USD(money):
    USD = int(money) / 2.4981
    return USD

def exchange_EUR(money):
    EUR = int(money) / 2.9527
    return EUR

def exchange_CHF(money):
    CHF = int(money) / 2.7094
    return CHF

def exchange_GBP(money):
    GPB = int(money) / 3.4629
    return GPB

def exchange_CNY(money):
    CNY = int(money) / 3.8760
    return CNY

def get_currency():
    currency = int(input("Выберите номер валюты: 1 - USD, 2 - EUR, 3 - CHF, 4 - GBP, 5 - CNY:"))
    return currency