# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
 
fact_time = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
    
x = fact(130)
 """

factorial_time = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(130)
"""


# timeit
result1 = timeit.timeit(fact_time, number=10000)
result2 = timeit.timeit(factorial_time, number=10000)

print("Iterative: ", result1)
print("Recursive: ", result2)

result3 = timeit.repeat(fact_time, number=10000, repeat=4)
result4 = timeit.repeat(factorial_time, number=10000, repeat=4)

print("Iterative list: ", result3)
print("Recursive list: ", result4)

print("Iterative list sum: ", sum(result3))
print("Recursive list sum: ", sum(result4))
