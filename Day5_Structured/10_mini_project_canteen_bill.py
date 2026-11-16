"""
==========================================================================
 Day 5 | Lesson 10 : Mini Project - The Canteen Bill
==========================================================================
 Every idea from Lessons 01 to 09 in one small program.

   parameters and defaults    -> make_bill(customer, ..., discount=0)
   *args                      -> any number of items
   **kwargs                   -> any extra notes for the bill
   recursion                  -> a combo meal can contain another combo
   lambda + map/filter/reduce -> change, keep, combine the prices
   module                     -> shop_tools.py does the GST and discount

 Run this file :  python 10_mini_project_canteen_bill.py
==========================================================================
"""
from functools import reduce

import shop_tools

# A price is a number. A combo is a list of prices and other combos.
TEA = 12
SAMOSA = 15
MEAL = [60, 20, [10, 5]]                # rice, curry, [curd, pickle]


def price_of(item):
    """Recursion: a number is its own price; a combo is the sum of its parts."""
    if type(item) != list:              # BASE CASE
        return item
    total = 0
    for part in item:
        total += price_of(part)         # RECURSIVE CASE
    return total


def make_bill(customer, *items, discount=0, **notes):
    """Print a bill and return the amount to pay."""
    prices = list(map(price_of, items))                         # CHANGE
    large = list(filter(lambda p: p >= 50, prices))             # KEEP
    subtotal = reduce(lambda a, b: a + b, prices, 0)            # COMBINE

    after_discount = shop_tools.apply_discount(subtotal, discount)
    to_pay = shop_tools.add_gst(after_discount)

    print("Customer :", customer)
    print("Prices   :", prices)
    print("Big items:", large)
    print("Subtotal :", subtotal)
    print("To pay   :", to_pay, f"(discount {discount}%, GST {shop_tools.GST_RATE}%)")
    for key, value in notes.items():
        print(f"Note     : {key} = {value}")
    print("-" * 40)
    return to_pay


make_bill("Asha", TEA, SAMOSA)
make_bill("Ravi", MEAL, TEA, discount=10)
make_bill("Meena", MEAL, MEAL, SAMOSA, discount=20, table=4, paid_by="UPI")
make_bill("Nobody")                     # no items at all still works


# ==========================================================================
# PREDICT before you run!
#   What is price_of(MEAL)?
#   What does Ravi pay?  (subtotal, then 10% off, then 5% GST)
#
# TRY IT YOURSELF
#   1. Add a new combo THALI = [MEAL, SAMOSA, TEA] and bill it.
#      Did price_of need any change? Why not?
#   2. Add a parameter tip=0 to make_bill.
#   3. Move price_of into shop_tools.py and import it from there.
#   4. Sort the prices highest first before printing. Use sorted with key
#      or reverse.
# ==========================================================================
