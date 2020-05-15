# find hcf or gcd using Euclidean Algorithm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def compute_hcf(x,y):
    while(y): # greater
        x,y = y,x % y
    return x
hcf = compute_hcf(num1,num2)
print(hcf)