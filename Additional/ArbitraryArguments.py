def order_pizza(size, *toppings, **details):
  print(f"Ordered a {size} pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")
  print("\nDetails of the order are:")
  for key, value in details.items():
    print(f"- {key}: {value}")

order_pizza("large", "pepperoni", "oloves", delivery=True, tip=5)