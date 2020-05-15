num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
def compute_lcm(num1, num2):
    largest = max(num1, num2)
    while True:
        if largest % num1 == 0 and largest % num2 == 0:
            lcm = largest
            break
        largest += 1
    return lcm
result = compute_lcm(num1, num2)
print(result)