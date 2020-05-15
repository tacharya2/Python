def fibo_recur(n):
    if n<=1:
        return n
    else:
        return (fibo_recur(n-1) + fibo_recur(n-2))
nterms = int(input("How many fibonacci number are you looking for?: "))
for i in range(nterms):
    print(fibo_recur(i))