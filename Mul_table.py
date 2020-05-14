m = int(input("Multiplication table of what number m ?: "))
n = int(input("Upto what range n ?: "))
for i in (1, n):
    for j in range(n+1):
        print(m," * ", j, " = ", m * j)
    break
