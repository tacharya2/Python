n = int(input("Multiplication table of what number n ?: "))
m = int(input("Upto what range m ?: "))
for i in (1, n):
    for j in range(m+1):
        print(n," * ", j, " = ", n * j)
    break
