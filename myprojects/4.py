# # 4

from moneyfmt import moneyfmt
from decimal import *
def dollarize(d):
    # if isinstance(dollar, float):
    # dollar = abs(d)
    new_d = Decimal(str(d))
    dollars = moneyfmt(abs(new_d), curr='$')
    return dollars

    # return f"python${str(dollar).rjust(3, ',')}"
dollarize(123456.78901)
dollarize(-123456.7801)
dollarize(1000000)

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, new_money):
        # self.amount = dollarize(Decimal(new_money))
        self.amount = new_money
        return self.amount

    def __repr__(self):
        return repr(self.amount)

    # @dollarize
    def __str__(self):
        return f'{dollarize(self.amount)}'

cash = MoneyFmt(12345678.021)
print(cash) #-- returns "$12,345,678.02"
cash.update(100000.4567)
print(cash) #-- returns "$100,000.46"
cash.update(-0.3)
print(cash) #-- returns "-$0.30"
print(repr(cash)) #-- returns -0.3