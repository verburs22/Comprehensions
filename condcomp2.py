#sarah verburg 07-01

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

meals = []

for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("meal was skipped")
print(meals)

meals = [meal if "spam" not in meal else "meal was skipped" for meal in menu]
print(meals)

x = 12
exp = "twelve" if x == 12 else "unknown"
print(exp)
