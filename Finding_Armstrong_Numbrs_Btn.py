# A program to find Armstrong Numbers between a given range
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for num in range(lower, upper+1):
    ord = len(str(num))
    sum = 0
    temp = num
    while temp>0:
        digit = temp%10
        sum+=digit**ord
        temp//=10
    if num == sum:
        print(num)