"""Practice instantiating Pizza class."""

from lessons.pizza import Pizza

my_pizza: Pizza = Pizza("large", 1, True)
skys_pizza: Pizza = Pizza("small", 1, False)


# def price(pizza_order: Pizza) -> float:
#     """Calculate and return cost of pizza."""
#     cost: float = 0.0
#     if pizza_order.size == "large":
#         cost = 6.0
#     else:
#         cost = 5.0
#     # charge .75 per topping
#     cost += 0.75 * pizza_order.toppings
#     # charge 1.00 for gluten free
#     if pizza_order.gluten_free:
#         cost += 1.0
#     return cost

print(my_pizza.price)
print(skys_pizza.price)
print(my_pizza.gluten_free)