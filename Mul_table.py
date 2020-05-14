m = int(input("Multiplication table of what number n ?: "))
n = int(input("Upto what range m ?: "))
for i in (1, n):
    for j in range(n+1):
        print(m," * ", j, " = ", m * j)
    break
