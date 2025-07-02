# sarah verburg 07-01

import timeit

set_up = """\
gc.enable()
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
"""

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


def nested_loop():
    result = []
    for loc in sorted(locations):
        exit_destination1 = []
        for ex in exits:
            if loc in exits[ex].values():
                exit_destination1.append((ex, locations[ex]))
        result.append(exit_destination1)

    #print result before returning
    for x in result:
        pass

    return result


def loop_comp():
    result = []
    for loc in sorted(locations):
        exit_destination2 = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
        result.append(exit_destination2)

    #print result before returning
    for x in result:
        pass

    return result


def nested_comp():
    exit_destination3 = [[(ex, locations[ex]) for ex in exits if loc in exits[ex].values()] for loc in sorted(locations)]

    #print result before returning
    for x in exit_destination3:
        pass

    return exit_destination3

def nested_generator():
    exit_destination3 = ([(ex, locations[ex]) for ex in exits if loc in exits[ex].values()] for loc in sorted(locations))

    #print result before returning
    for x in exit_destination3:
        pass

    return exit_destination3


print(nested_comp())
print(nested_loop())
print(loop_comp())

# timeit testing
result1 = timeit.timeit(nested_loop, set_up, number=10000)
result2 = timeit.timeit(loop_comp, set_up, number=10000)
result3 = timeit.timeit(nested_comp, set_up, number=10000)
result4 = timeit.timeit(nested_generator, set_up, number=10000)

print("Nested loop: ", result1)
print("loop comp:   ", result2)
print("Nested comp: ", result3)
print("Nested gen:  ", result4)

