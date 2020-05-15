# algorithm to find lcm using gcd
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number"))
def compute_gcd(num1, num2):
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1
def compute_lcm(num1, num2):
    lcm = (num1 * num2)//compute_gcd(num1, num2)
    return lcm
result = compute_lcm(num1, num2)
print(result)