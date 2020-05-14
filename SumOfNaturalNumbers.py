# add all natural numbers up to a user given number.
n = int(input("Up to what number do you want to get sum of?: "))
sum = 0
while n>0:
    for num in range(n+1):
        sum+=num
    print(sum)
    break
else:
    print("0")