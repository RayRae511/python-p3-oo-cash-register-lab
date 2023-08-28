#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.item = []
    self.total = 0
  
  def add_item(self, title, price, quantity):
    self.total += price * quantity
    self.item.append([title] * quantity)
    
  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * self.discount / 100
      print(f"After the discount, the total comes to {self.total:.0f}.")
    else:
      print("There's no discount to apply.")
      
  def void_last_transaction(self):
    if self.item:
      last_item_price = self._get_last_item()
      self.total -= last_item_price
      self.item.pop()
      
  def get_last_item(self):
    title = self.item.pop()
    return self._get_last_item(title)
  
  def get_price_by_title(self, title):
    item_price = {}
    return item_price.get(title, 0)
  
  