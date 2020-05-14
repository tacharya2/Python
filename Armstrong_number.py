# if 123 = 1^3+2^3+3^3, then 123 is an Armstrong number
# Check if a given 3 digit number is an Armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp>0:
    digit = temp % 10 # digit = 3, 5, 1^3
    sum += digit**order # sum = 3^3+5^3+1^3
    temp //= 10 # temp = 15, 1, 0<-terminates
if num == sum:
    print(num, " is an Armstrong number")
else:
    print(num, " is not an Armstrong number")