"""
A small module used by Lesson 08 and Lesson 10.

A module is just a .py file. Other files can import it and use what is inside.
"""

GST_RATE = 5                            # percent


def add_gst(price, rate=GST_RATE):
    """Return the price with GST added."""
    return round(price * (100 + rate) / 100, 2)


def apply_discount(price, percent=10):
    """Return the price after a discount."""
    return round(price * (100 - percent) / 100, 2)


# This block runs only when you run THIS file directly:
#     python shop_tools.py
# It does not run when another file imports shop_tools.
if __name__ == "__main__":
    print("Testing shop_tools")
    print(add_gst(100))                 # 105.0
    print(apply_discount(200))          # 180.0
