#resturn the largest of three numbers.
num1 = 2
num2 = 3
num3 = 4
if (num1>=num2) and (num1>=num3):
    largest = num1
elif (num2>=num3) and (num2>=num1):
    largest = num2
else:
    largest = num3
print(largest)