#sarah verburg 07-01

# for x in range(1, 31):
#     fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(fizzbuzz)

# challenge 1

fizbuz = [("fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)) for x in range(1,31)]
print(fizbuz)

for buzz in fizbuz:
    print(buzz.center(12, ' '))
