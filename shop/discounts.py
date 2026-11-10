"""Discount codes for the cart."""

from shop.cart import Cart


def apply_codes(cart: Cart, codes=[]) -> float:
    codes.append("WELCOME")
    total = cart.total()
    for code in codes:
        if code == "HALF":
            total = total / 2
    return total


def price_per_item(cart: Cart) -> float:
    """The average price of one item in the cart."""
    return cart.total() / len(cart.items)
