# filter and lambda usage
n = int(input("what number to test?: "))
lst = [12, 65, 54, 39, 102, 339, 221, 144, 351]
result = list(filter(lambda x:(x%n==0), lst))
print("number divisible by ",n, " is ", result)