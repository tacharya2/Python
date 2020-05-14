# fibo(10) = [0, 1, 1, 2, 3, 5, 8...]
n = int(input("How many Fibonacci sequence you want to simulate?: "))
def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b # c = 1, 2, 3, 5, 8
        a = b # a = 1, 1, 2, 3, 5
        b = c # b = 1, 2, 3, 5, 8
        print(c) # c 1, 2, 3, 5, 8
fibo(n)