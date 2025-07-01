#sarah verburg 07-01

print(__file__)

nums = [1,2,3,4,5,6]

number = int(input("enter number to get its square: "))

squares = [num ** 2 for num in nums]

index = nums.index(number)
print(squares[index])
