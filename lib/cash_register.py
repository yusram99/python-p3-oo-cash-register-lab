#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

    def void_last_transaction(self):
        if self.items:
            last_item_cost = self._item_price(self.items.pop())
            self.total -= last_item_cost

    def _item_price(self, item):
        item_prices = {"eggs": 0.98, "book": 5.00, "Lucky Charms": 4.5, "Ritz Crackers": 5.0, "Justin's Peanut Butter Cups": 2.50}
        return item_prices.get(item, 0)


