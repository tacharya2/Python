m = int(input("Enter lower limit for prime finding: "))
n = int(input("Enter a upper limit for prime finding: "))
for num in range(m,n+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)