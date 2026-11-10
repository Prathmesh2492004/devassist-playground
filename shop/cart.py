"""A tiny shopping cart, used to try out DevAssist's pull request reviews."""

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    quantity: int = 1


@dataclass
class Cart:
    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        self.items.append(item)

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def average_price(self) -> float:
        if not self.items:
            return 0.0
        return self.total() / len(self.items)
