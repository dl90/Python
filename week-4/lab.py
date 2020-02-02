from datetime import datetime
from enum import Enum


class Condition(Enum):
    NEW = 1
    GOOD = 0.8
    OK = 0.5
    BAD = 0.2


class Bike:

    def __init__(self, cost, make, model, year, condition):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year

        if(type(condition) == float):
            self.condition = condition
        else:
            condition = condition.upper()
            self.condition = Condition[condition].value

    @classmethod
    def original_price(cls, make = None, model = None):
        self.msrp = 1000

    def set_sale_price(self):
        current_year = datetime.now().year
        current_value = self.msrp * (1 - (current_year - self.year) * 0.015)
        current_value = current_value * self.condition
        self.saleprice = current_value

    def sold_bike(self):
        self.sold = True
        self.saleprice = self.saleprice - self.cost


bike1 = Bike(100, 'Univega', 'Alpina', 1999, "bad")
bike1.original_price()
bike1.set_sale_price()
print(bike1.saleprice)

bike1.sold_bike()
print(bike1.saleprice)
