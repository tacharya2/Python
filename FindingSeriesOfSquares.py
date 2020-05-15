# Use lambda function to find a series of n raised to pow x
# lambda is a very important function
a = int(input("enter up what number n do you need squares of?:"))
n = int(input("What raised to pow?: "))
result = list(map(lambda x: n**x, range(a+1)))
for i in range(a+1):
    print(n, "raised to power", i, "is", result[i])