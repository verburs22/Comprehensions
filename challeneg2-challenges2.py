#sarah verburg 07-01

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

print("nested for loop")
print('-' *30)

for loc in sorted(locations):
    exit_destination1 = []
    for ex in exits:
        if loc in exits[ex].values():
            exit_destination1.append((ex, locations[ex]))
    print("Locations leading to {}".format(loc), end='\t')
    print(exit_destination1)

print()

print("list comprehension inside a for loop")
print('-' *30)

for loc in sorted(locations):
    exit_destination2 = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
    print("Locations leading to {}".format(loc), end='\t')
    print(exit_destination2)

print()

print("nested comprehension ")
print('-' *30)

exit_destination3 = [[(ex,locations[ex]) for ex in exits if loc in exits[ex].values()] for loc in sorted(locations)]
print(exit_destination3)

print()
for index, loc in enumerate(exit_destination3):
    print("Locations leading to {}".format(index), end='\t')
    print(loc)

