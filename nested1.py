#sarah verburg 07-01

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)

print()

# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)


